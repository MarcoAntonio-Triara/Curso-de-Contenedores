# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hola desde Docker-landia, Humano!'
 
if __name__ == "__main__":
    app.run()