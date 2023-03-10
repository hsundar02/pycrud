from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "hash_02"

