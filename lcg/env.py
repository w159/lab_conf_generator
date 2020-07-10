import os

APP_PORT = os.getenv("APP_PORT", 5002)
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
DB_HOST = os.getenv("DB_HOST", "192.168.1.182")
DB_PORT = os.getenv("DB_PORT", 27017)
DB = os.getenv("DB", "LCG_API")
DEBUG = os.getenv("DEBUG", True)