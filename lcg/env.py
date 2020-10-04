import os

APP_PORT = os.getenv("APP_PORT", 5002)
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
DB_HOST = os.getenv("DB_HOST", "192.168.1.182")
DB_PORT = os.getenv("DB_PORT", 27017)
DB = os.getenv("DB", "LCG_API")
DEBUG = os.getenv("DEBUG", True)

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY",'AKIA6MRXVMB5NBSTYHO2')
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", '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')

TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER', 'template')
