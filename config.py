import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxx'
    SERVICE_NAME = os.environ.get('SSA_SERVICE_NAME') or "say_something_app"
    AGENT_HOST_NAME = os.environ.get('SSA_AGENT_HOST_NAME') or "localhost"
    AGENT_PORT = os.environ.get('SSA_AGENT_POST') or 6831
