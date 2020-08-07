# Lab Configuration Generator

This tool is used to generate configurations for CLI based Network devices. The motivation for this tool came from the 
need to rapidly generate configurations for devices that i use during my lab sessions. I have built a docker base CLI 
as well as an RestFUL API interfaces that can interact with LCG tool.

Both the docker-cli and API utilize JSON models for input.  There are required model keys for each configuration request type. 


## Actions  
### config
This action generates configurations based on the "template_type" var. 
- Supported Node Types:
    - ios_base_node
    
