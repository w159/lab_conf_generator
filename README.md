# Genesis Configuration Generator

This tool is used to generate configurations for numerous types of devices and services. The goal of this service is to
provide users the ability to quickly define their own configuration definition to later be used for rapid and consistent
configuration generation. This tool also supports the ability to store configurations to an AWS S3 cloud. 


Both the docker-cli and API utilize JSON models for input.  There are required model keys for each configuration request type. 




```text
usage: __main__.py [-h] [--run] [--json JSON]
                   [--template_type {ios_base_node,ios_te_tunnels,ios_bgp_policy,ios_bgp_session,ios_explicit_path,ios_vpls,ios_evpn,xr_base_config,linux_netplan_base}]
                   [--store_aws] [--store_local]
                   [--aws_access_key AWS_ACCESS_KEY]
                   [--aws_secret_key AWS_SECRET_KEY]
                   [--save_location SAVE_LOCATION] [--config_name CONFIG_NAME]

Genesis Configuration Generator

optional arguments:
  -h, --help            show this help message and exit
  --run                 Runs Development HTTP server used to deploy Genesis
                        Configuration Generator

Commands for running the GCG CLI tool:
  --json JSON           Specify the JSON file you would like to generate.
  --template_type {ios_base_node,ios_te_tunnels,ios_bgp_policy,ios_bgp_session,ios_explicit_path,ios_vpls,ios_evpn,xr_base_config,linux_netplan_base}
  --store_aws           Flag to store rendered config to AWS
  --store_local         Flag to store rendered config to local file system
  --aws_access_key AWS_ACCESS_KEY
                        Access Key used for AWS Boto3 session
  --aws_secret_key AWS_SECRET_KEY
                        Secret Key used for AWS Boto3 session
  --save_location SAVE_LOCATION
                        Specify location to save the generated config
  --config_name CONFIG_NAME
                        Specify the name of the Generated configuration .txt
                        file

Process finished with exit code 0


```

# ENV options
Enviornment Vars can be declared in multuple methods. 

1. Create a file env.py in the main directory after cloning this repo. 


```python
import os 

APP_PORT = os.getenv("APP_PORT", 5002)
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
DB_HOST = os.getenv("DB_HOST", "192.168.1.182")
DB_PORT = os.getenv("DB_PORT", 27017)
DB = os.getenv("DB", "LCG_API")
DEBUG = os.getenv("DEBUG", True)
```
  
2. Docker envs.  
