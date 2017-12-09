from flask import Flask
from peewee import SqliteDatabase

import config


app = Flask(__name__)

db = SqliteDatabase(config.DATABASE_URI)
