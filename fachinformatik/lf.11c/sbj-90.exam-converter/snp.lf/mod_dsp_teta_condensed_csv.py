# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# functions for reading and converting a csv file of planking data: VP-1.1 


# (4) adapter to write planking data into a condensed csv file

# Idea:  encode shall- and is-values into the same 2 byte integer:

def combine(shall_value, is_value) :
  return (shall_value << 8) + is_value

def write_as_condensed_csv(filename,planking_data):
  print(f"writing into condensed csv file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  for ds in planking_data:
    shis_1=combine(ds["shall1"],ds["is1"])
    shis_2=combine(ds["shall2"],ds["is2"])
    shis_3=combine(ds["shall3"],ds["is3"])
    ouf.write(f"{ds["set"]},{ds["day"]},{shis_1},{shis_2},{shis_3}\n")
  return ouf.close()



