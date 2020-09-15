# Import Flask dependency
from flask import Flask
# Create Flask app using magic method
app = Flask(__name__)
# Create root route starting point
@app.route('/')
# Add function to route
def hello_world():
    return 'Hello World'

