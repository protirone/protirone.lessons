# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# converts a csv file of day data into the respective ini file: VP-1.0

import sys
import mod_dsp_beta_conv_adapters as adapters

# intermediate representation and hard-coded testdata
dd_hard_coded=(
{ "day":"2026-01-01", "sunrise": "08:29","sunset": "16:31","durance": "08:02"},
{ "day":"2026-01-02", "sunrise": "08:29","sunset": "16:32","durance": "08:03"}) 

dd_in_file="dsp.lf/dsp.beta.csv"
dd_out_format="csv"

if ((len(sys.argv)>1)) : 
  match sys.argv[1]:
    case "INI" | "ini": dd_out_format="ini"
    case "test": dd_in_file="dsp.lf/dsp.beta-t.csv"
if ((len(sys.argv)>2)) : 
  match sys.argv[2]:
    case "INI" | "ini": dd_out_format="ini"

# main

daydata=adapters.fill_from_csv(dd_in_file)
#daydata=dd_hard_coded

if (daydata):
  if(dd_out_format=="csv"): 
    adapters.write_as_csv("res.lf/daydata.csv",daydata)
  else:
    adapters.write_as_ini("res.lf/daydata.ini",daydata) 