#!/usr/bin/python3
from flask import Flask


app = Flask(__name__) 
app.config.from_object(__name__)

"""
BASIC DB FUNCTIONS
init_db()
query_db()
connect_db
"""