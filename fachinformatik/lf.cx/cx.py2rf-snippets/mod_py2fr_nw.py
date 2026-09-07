# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

import ipaddress
import mod_py2fr_nwcore as nwc

class ProTiCo_Network(nwc.ProTiCo_Network_Data):

  def __init__(self,ia_str='192.168.0.13',nm_str='255.255.255.128'):
    super().__init__(ia_str,nm_str)

  def _show_address(self,type,address):
    addr_str=ipaddress.ip_address(address)
    print(f"{type} hat den Wert <{addr_str}> = <{address:b}>")

  def describe(self):
    self._show_address("ipv4-addr",self._ip_addr)
    self._show_address("net-mask",self._net_mask)
    self._show_address("net-addr",self._net_addr)
    self._show_address("bc-addr",self._bc_addr)
    self._show_address("gw-addr",self._gw_addr)

  def is_member(self,ipv4_str):
    test_ip=(int)(ipaddress.ip_address(ipv4_str))
    return ((test_ip&self._net_mask)==self._net_addr)

if __name__ == "__main__":
  print("starting the module self test:")
  nw=ProTiCo_Network()
  print(f"nw-data: {nw.get_ia_str()}/{nw.get_nm_str()}")
  nw.describe()
  print(f"Is 127.0.0.1 in mnw? {nw.is_member('127.0.0.1')}")