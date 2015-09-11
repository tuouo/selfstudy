#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiomysql, asyncio, logging
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool ......')
    global __pool
    __pool = yield from aiomysql.create_pool(
    	host	= kw.get('host', 'localhost'),
    	port	= kw.get('port', '3306'),
    	user	= kw['user'],
    	password= kw['password'],
    	db 		= kw['db'],
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
        logging.info('Rows returned is %s' % len(rs))	
        return rs

@asyncio.coroutine
def execute(sql, args, autocommit = True):
    log(sql)
    global __pool
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.curson(aiomysql.DictCursor)
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowconut
        except BaseException as e:
            raise 
        return affected


class Field(object):
    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, slef.colum_type, self.name)

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


class ModelMetaclass(type):
    def __new__(class, name, bases, attrs):
        if __name__ = 'Model':									# ignore Model self
            return type.__new(class, name, bases, attrs)	
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table %s)' % (name, tableName))	
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs:
            if isinstance(v, Field):
                logging.info("\tFound mapping: %s ==> %s" % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise RuntimeError("Duplicate primary key for field: %s" % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError("Primary key not found")
        for k in mappings.keys():
            attrs.pop(k)
        esacFields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mapping__'] = mappings
        attrs['__table__'] = tableName
        attrs['__primaryKey__'] = primaryKey
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primary, ', '.join(esacFields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, 
        	', '.join(esacFields), primary, creArgsStr(len(esacFields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s` = ?' % (tableName, 
        	', '.join(map(lambda f: '`%s` = ? ' % mappings.get(f).name or f, fields)), primary)
        attrs['__delete__'] = 'delete from `%s` where `%s` = ?' % (tableName, primary)
        return type.__new(class, name, bases, attrs)
        




class Model(dict, metaclass = ModleMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
    	try:
    	    return slef[key]
    	except keyError:
    	    raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key ,value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getDefaultValue(self, key):
        value = getattr(self, key, None)
        if Value is None:
            field  = self._mappings_[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default()	#?_?, unnessary
                logging.debug('using default value for %s:%s' % (key, str(value)))
                setattr(self, key, value)
        return value

    






from orm import Model, StringField, IntegerField
class User(Model):
    __tables__ = 'users'
    id = IntegerField(primary_key = True)
    name = StringField()

user = User(id = 123, name = 'tuouo')
user.insert()
users = User.findAll()