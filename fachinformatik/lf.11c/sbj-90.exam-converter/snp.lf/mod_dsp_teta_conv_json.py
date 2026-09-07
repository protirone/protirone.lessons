# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# function for converting a csv file of planking data into a json file: VP-1.0 

# (3) adapter to write planking into a json file
def write_as_json(filename,planking_data):
  print(f"writing into json file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  ouf.write("[\n")
  successor=False
  for ds in planking_data:
    if successor: ouf.write(",\n\t{\n")
    else: 
      ouf.write("\t{\n")
      successor=True
    ouf.write(f"\t\t\"set\": {ds["set"]},\n\t\t\"day\": {ds["day"]},\n"
      f"\t\t\"shall1\" : {ds["shall1"]},\n\t\t\"is1\" : {ds["is1"]},\n"
      f"\t\t\"shall2\" : {ds["shall2"]},\n\t\t\"is2\" : {ds["is2"]},\n"
      f"\t\t\"shall3\" : {ds["shall3"]},\n\t\t\"is3\" : {ds["is3"]}"
    )
    ouf.write(" }")
  ouf.write("\n]\n")
  return ouf.close()