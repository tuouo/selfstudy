#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiomysql, asyncio, logging
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool ......')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host	= kw.get('host', 'localhost'),
        port	= kw.get('port', 3306),
        user	= kw['user'],
        password= kw['password'],
        db 		= kw['database'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        minsize	= kw.get('minsize', 1),
        maxsize	= kw.get('maxsize', 10),
        loop	= loop
        )

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

@asyncio.coroutine
def select(sql, args, size = None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:								# once yield from, need everywhere
        cur = yield from conn.curson(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())	# without write sql str byself incase attack
        if size:
            rs = yield from cur.fetchmany(size) 
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('Rows returned: %s' % len(rs))	
        return rs

@asyncio.coroutine
def execute(sql, args, autocommit = True):
    log(sql)		#log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        if not autocommit:
            yield from conn.begin()
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
            if not autocommit:
                yield from conn.commit()
        except BaseException as e:
            if not autocommit:
                yield from conn.rollback()
            raise 
        return affected


class Field(object):
    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.colum_type, self.name)

class StringField(Field):
    def __init__(self, name = None, primary_key = False, default = None, ddl = 'varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):
    def __init__(self, name = None, default = False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
    def __init__(self, name = None, primary_key = False, default = 0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):
    def __init__(self, name = None, primary_key = False, default = 0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):
    def __init__(self, name = None, default = None):
        super().__init__(name, 'text', False, default)

def creArgsStr(num):
    l = []
    for i in range(num):
        l.append('?')
    return ', '.join(l)

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':									# ignore Model self
            return type.__new__(cls, name, bases, attrs)	
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table %s)' % (name, tableName))	
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info("\tFound mapping: %s ==> %s" % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise StandardError("Duplicate primary key for field: %s" % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise StandardError("Primary key not found")	#RuntimeError
        for k in mappings.keys():
            attrs.pop(k)
        esacFields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = tableName
        attrs['__primarykey__'] = primaryKey
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(esacFields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, 
        	', '.join(esacFields), primaryKey, creArgsStr(len(esacFields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s` = ?' % (tableName, 
        	', '.join(map(lambda f: '`%s` = ? ' % mappings.get(f).name or f, fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s` = ?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)
        
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key ,value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getDefaultValue(self, key):
        value = getattr(self, key, None)
        if value is None:
            field  = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default	#?_?, unnessary
                logging.debug('using default value for %s:%s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    @asyncio.coroutine
    def find(cls, pk):						
        ' find object by primary key.'
        rs = yield from select('%s where `%s` = ?' % (cls.__select__, cls.__primarykey__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])
    # user = yield from User.find('123')

    @classmethod
    @asyncio.coroutine
    def findNumber(cls, selectField, where = None, args = None):
        ' find number by select and where'
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = yield from select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    @asyncio.coroutine
    def findAll(cls, where = None, args = None, **kw):
        ' find objects by "where clause"'
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get("orderBy", None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get("limit", None)
        if limit is not None:
            sql.append("limit")
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, truple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limti))
        rs = yield from select (" ".join(sql), args)
        return [cls(**r) for r in rs]

#user = User(id = 123, name = 'tuouo')
#user.insert()
#users = User.findAll()


    @asyncio.coroutine
    def save(self):
        args = list(map(self.getDefaultValue, self.__fields__))
        args.append(self.getDefaultValue(self.__primarykey__))
        rows = yield from execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)
    # user = User(id = 123, name = 'tuouo')
    # yield from user.save()

    @asyncio.coroutine
    def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primarykey__))
        rows = yield from execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update record: affected rows: %s' % rows)

    @asyncio.coroutine
    def remove(self):
        args = [self.getValue(self.__primarykey__)]
        rows = yield from execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key record: affected rows: %s' % rows)