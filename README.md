# Lab Configuration Generator

This tool is used to generate configurations for CLI based Network devices.

**CLI Usage:**
```text
u****sage: lcg_cli.py [-h] [--base_config BASE_CONFIG] [--te_tunnels TE_TUNNELS]
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

##Examples
The json/examples director contains some JSON examples that should be used to demonstrate the Configuraiton
generations

IOS BGP Policy:
```json
{
  "node_type": "ios",
  "policy_name": "L3VPN_CE1",
  "send_community_both": true,
  "orf_bidir": true,
  "soft_reconfiguration": true,
  "maximum_prefix": 50,
  "route_map_in": "L3VPN_CE1_IN",
  "route_map_out": "L3VPN_CE1_OUT",
  "site_of_origin": "100:01"
}
```

Result:
```text
# Run Command
python lcg_cli.py -o output\example_bgp_policy.txt --bgp_policy json\examples\ios_bgp_policy.json

# Output File:
template peer-policy L3VPN_CE1
 route-map L3VPN_CE1_IN in
 route-map L3VPN_CE1_OUT out
 maximum-prefix 50
 capability orf prefix-list both
 soo 100:01
 send-community both
 soft-reconfiguration inbound
exit-peer-policy
```