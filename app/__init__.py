from flask import Flask
app = Flask(__name__)
from app import models
from app import evaluator
from app import views
