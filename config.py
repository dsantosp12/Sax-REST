import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_token():
    with open("{}/.token".format(BASE_DIR)) as file:
        token = file.readline()
    return token


HOST = "0.0.0.0"
PORT = 9432

DEBUG = True

DATABASE_URI = os.getenv("HOME") + "/.config/sax/sax-rest.db"

# SAX Config
EMITTER_PORT = 4028
