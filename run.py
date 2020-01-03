from app import app
# from config import DEBUG, APP_PORT

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")