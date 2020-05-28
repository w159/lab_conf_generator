from app import app
from config import DEBUG, APP_PORT, APP_HOST

if __name__ == "__main__":
    app.run(debug=DEBUG, port=APP_PORT, host=APP_HOST)
