# Lab Configuration Generator

This tool is used to generate configurations for CLI based Network devices. The motivation for this tools came from the 
need to rapibly generate Configurations for devices that i use in my Lab environment 

## Models 
### base_config
Use this model to generate new configurations for nodes. the "node_type" key is used to tell the application
what kind of configuration must be generate.
- Supported Node Types:
    - ios
    - ios_xr 
```text
{
  "node_type": "ios",
  "hostname": "",
  "management": {
    "link_id": "",
    "ip_address": "",
    "netmask": ""
  },
  "interfaces": [
    {
      "link_id": "",
      "description": "",
      "ip_address": "",
      "netmask": ""
    }
  ]
}
```