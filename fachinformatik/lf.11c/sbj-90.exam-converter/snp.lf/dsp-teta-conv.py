# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# for converting a csv file of planking data into a json file: VP-1.0
import sys
import mod_dsp_teta_conv_csv as csv_adapters
import mod_dsp_teta_conv_json as json_adapters

# intermediate representation and hard-coded testdata
td_hard_coded=[ 
  { "set": 1, "day": "2026-01-01", 
    "shall1": 30, "is1": 32, "shall2": 20, "is2": 18, "shall3": 15, "is3": 15}, 
  { "set": 2, "day": "2026-01-02", 
    "shall1": 30, "is1": 35, "shall2": 25, "is2": 22, "shall3": 20, "is3": 18} ]

planking_data_infile="dsp.lf/dsp.teta-c.csv"
pd_out_format="csv"

if ((len(sys.argv)>1)) : 
  match sys.argv[1]:
    case "JSON" | "json": pd_out_format="json"
    case "test": planking_data_infile="dsp.lf/dsp.teta-t.csv"
if ((len(sys.argv)>2)) : 
  match sys.argv[2]:
    case "JSON" | "json": pd_out_format="json"

# main
planking_data=csv_adapters.fill_from_csv(planking_data_infile)
#planking_data=td_hard_coded
if (planking_data):
  match pd_out_format:
    case "json": json_adapters.write_as_json("res.lf/planking_data.json",planking_data) 
    case _: csv_adapters.write_as_csv("res.lf/planking_data.csv",planking_data)