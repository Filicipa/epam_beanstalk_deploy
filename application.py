from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from 9muunkkm Elastic Beanstalk CI-CD"