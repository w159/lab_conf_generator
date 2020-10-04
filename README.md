# Genesis Configuration Generator

This tool is used to generate configurations for numerous types of devices and services. The goal of this service is to
provide users the ability to quickly define their own configuration definition to later be used for rapid and consistent
configuration generation. This tool also supports the ability to store configurations to an AWS S3 cloud. 


Both the docker-cli and API utilize JSON models for input.  There are required model keys for each configuration request type. 


# ENV options
Create a file env.py in the main directory after cloning this repo. 

```python
import os 

APP_PORT = os.getenv("APP_PORT", 5002)
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
DB_HOST = os.getenv("DB_HOST", "192.168.1.182")
DB_PORT = os.getenv("DB_PORT", 27017)
DB = os.getenv("DB", "LCG_API")
DEBUG = os.getenv("DEBUG", True)
```
    
