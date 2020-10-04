# Lab Configuration Generator

This tool is used to generate configurations for CLI based Network devices. The motivation for this tool came from the 
need to rapidly generate configurations for devices that i use during my lab sessions. I have built a docker base CLI 
as well as an RestFUL API interfaces that can interact with LCG tool.

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
    
