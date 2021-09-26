#from flask import Flask

from app import create_app

#app = Flask(__name__)


#@app.route('/')
#def hello_world():  # put application's code here
#    return 'Hello World!'


if __name__ == '__main__':
#    app.run()
    server = create_app()
