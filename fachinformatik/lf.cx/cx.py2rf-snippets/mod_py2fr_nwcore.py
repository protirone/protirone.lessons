# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
import ipaddress, numpy

class ProTiCo_Network_Data:
  def __init__(self,ia_str='192.168.0.2',nm_str='255.255.255.0'):
    self._ia_str, self._nm_str=ia_str, nm_str
    self._ip_addr=int(ipaddress.ip_address(ia_str))
    self._net_mask=int(ipaddress.ip_address(nm_str))
    self._net_addr=(self._ip_addr&self._net_mask)
    # BCAddr = all bits of net-address o all bits of inverse net-mask 
    self._bc_addr=( numpy.array(~(self._net_mask))
                    .astype(numpy.int32).item() | (self._net_addr))
    self._gw_addr=(self._net_addr+1)
  def get_ia_str(self): return self._ia_str
  def get_nm_str(self): return self._nm_str

if __name__ == "__main__":
  mnw=ProTiCo_Network_Data()
  print(f"given: {mnw.get_ia_str()}/{mnw.get_nm_str()}")
  print(f"→ na:{mnw._net_addr}, bc:{mnw._bc_addr}, gw:{mnw._gw_addr}")