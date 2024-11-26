from app import Config, create_app
from flask import Flask

app: Flask = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT)
