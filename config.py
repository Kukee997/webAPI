import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://"username":"password"@localhost/project_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
