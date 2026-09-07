# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
import ipaddress
import sys
# set the default values and overload them by cmdline arguments
IP_AD1='10.75.65.222'
NT_MSK='255.255.224.0'
IP_AD2='10.75.70.108'
if ((len(sys.argv)>1)) : IP_AD1=sys.argv[1]
if ((len(sys.argv)>2)) : NT_MSK=sys.argv[2]
if ((len(sys.argv)>3)) : IP_AD2=sys.argv[3]

# decider: check by comparing 2 results of 'netmask & ipadress'
def in_the_same_network(ip_addr1,net_mask,ip_addr2):
  return(  ( (int)(ipaddress.ip_address(ip_addr1)) 
              & (int)(ipaddress.ip_address(net_mask)))
        == ( (int)(ipaddress.ip_address(ip_addr2)) 
             & (int)(ipaddress.ip_address(net_mask))))
# main
print("Is ", IP_AD1, " in the same network as ", IP_AD2, "? ",
  (in_the_same_network(IP_AD1,NT_MSK,IP_AD2)))