# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hola humanos, desde Dockerlandia!'
 
if __name__ == "__main__":
    app.run()