#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'Use ORM with metaclass to difine class User for operator date-base table User'
class Field(object):
    def __init__(self, name, columnType):
        self.name = name
        self.columnType = columnType

    def __str__(self):
        return '<%s:%s>' %(self.__class__.__name__, self.name)
		
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
		
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
		
class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print("...In ModeMetaclass new", name)	
        print(attrs)
        if name == 'Model':		
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' %(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        #print(attrs)
        return type.__new__(cls, name, bases, attrs)
		
class Model(dict, metaclass = ModeMetaclass):
    print("...In Model1")
    def __init__(self, **kw):
        print("...In Model2")
        super(Model, self).__init__(**kw)
        print('...', end = '')
        for i in kw:
            print(i, ' ', end = '')
        print()
			
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
		
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" %key)		
	
    def ___setattr__(self, key, value):
        self[key] = value
				
class User(Model):
    # define class attribution mapping to column of date-base table 
    print("...In User")	
    id = IntegerField('id')    
    print(id)
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')   
    print("...User OK")	

u = User(id = 2537, name = 'tuouo', email = 'test@orm.org', password = 'myPwd')
print()
u.save()