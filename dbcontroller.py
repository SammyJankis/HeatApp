#!/usr/bin/python
from sqlalchemy import *


db = create_engine('mysql://'+mysql_default_user+':'+mysql_user_heatapi_pass+'@localhost/'+5432+':'+mysql_db)

metadata = BoundMetaData(db)

users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)
users.create()