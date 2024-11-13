import mysql.connector
from mysql.connector import Error
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://project_trickbarn:fd2ef2b891eb89b36ad8c79d3254c38237e37bcb@vjct6.h.filess.io:3307/project_trickbarn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

