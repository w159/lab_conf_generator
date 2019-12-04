# Lab Configuration Generator

This tool is used to generate configurations for CLI based Network devices.

CLI Usage:
```text
usage: lcg_cli.py [-h] [--base_config BASE_CONFIG] [--te_tunnels TE_TUNNELS]
                  [--bgp_policy BGP_POLICY] [--bgp_session BGP_SESSION] [-o O]

Byt3m3 Lab Configuration Generator

optional arguments:
  -h, --help            show this help message and exit
  --base_config BASE_CONFIG
                        Generates Base Config for router
  --te_tunnels TE_TUNNELS
                        Generates Base Config for router
  --bgp_policy BGP_POLICY
                        Generates BGP policy-template configurations
  --bgp_session BGP_SESSION
                        Generates BGP session-template configurations
  -o O                  Output File Name
```