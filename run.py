# -*- encoding: utf-8 -*-
from api import app
from dotenv import load_dotenv
from api.config import PORT, HOST, DEBUG

if __name__ == "__main__":
    load_dotenv()
    app.run(host=HOST, port=PORT, debug=DEBUG)
