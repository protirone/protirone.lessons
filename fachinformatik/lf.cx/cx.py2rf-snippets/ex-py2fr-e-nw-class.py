# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

import sys
import mod_py2fr_nw as dnw

# main:

start_ia_str="192.168.2.42"
start_nm_str="255.255.255.0"

if ((len(sys.argv)>1)) : start_ia_str=sys.argv[1]
if ((len(sys.argv)>2)) : start_nm_str=sys.argv[2]

nw=dnw.ProTiCo_Network(start_ia_str,start_nm_str)
nw.describe()

tia="127.0.0.13"
if ((len(sys.argv)>3)) : tia=sys.argv[3]

print(f"{tia} + {nw.get_ia_str()} in same net?: <{nw.is_member(tia)}>")


