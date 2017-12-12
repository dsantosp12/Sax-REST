import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

HOST = "0.0.0.0"
PORT = 9432

DEBUG = True

SECRET_KEY = "c024be396990a710b1b20f31e77b527ef25df851f3e9afa4033c639188e399c7"

DATABASE_URI = os.getenv("HOME") + "/.config/sax/sax-rest.db"


# SAX Config
EMITTER_PORT = 4028
