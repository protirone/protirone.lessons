# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# functions for reading and converting a csv file of planking data: VP-1.0 

# (1) adapter to read planking data from a csvfile
def fill_from_csv(filename) :
  print(f"reading from csv file <{filename}>")
  planking_data=[]
  inf=open(filename,"r")
  # keep it simple: let the program crash if filename does not exist
  for line in inf:
    csv_str=line.strip()
    (id,dy,s1,i1,s2,i2,s3,i3)=csv_str.split(',')
    planking_data.append({ "set": id, "day":dy,
      "shall1":s1,"is1":i1,"shall2":s2,"is2":i2,"shall3":s3,"is3":i3,})
  return planking_data

# (2) adapter to write planking into a csvfile
def write_as_csv(filename,planking_data):
  print(f"writing into csv file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  for ds in planking_data:
    ouf.write(f"{ds["set"]},{ds["day"]},{ds["shall1"]},{ds["is1"]},"
      f"{ds["shall2"]},{ds["is2"]},{ds["shall3"]},{ds["is3"]}\n")
  return ouf.close()
