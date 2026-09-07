# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]
# functions to write and to convert daydata (dsp-beta) csv files 

# (1) adapters to read daydata from a file
def fill_from_csv(filename) :
  print(f"reading from csv file <{filename}>")
  daydata=[]
  inf=open(filename,"r")
  # keep it simple: let the program crash if filename does not exist
  for line in inf:
    csv_str=line.strip()
    (dy,se,st,de)=csv_str.split(',')
    daydata.append({"day":str(dy).strip(),"sunrise":str(se).strip(),
                    "sunset":str(st).strip(),"durance":str(de).strip()})
  return daydata

# (1) adapters to write daydata into a file
def write_as_csv(filename,daydata):
  print(f"converting as csv file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  for ds in daydata:
    ouf.write(f"{ds["day"]},{ds["sunrise"]},{ds["sunset"]},{ds["durance"]}\n")
  return ouf.close()

def write_as_ini(filename,daydata):
  print(f"converting as ini file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  for ds in daydata:
    ouf.write(f"[ {ds["day"]} ]\nSunrise={ds["sunrise"]}\nSunset={ds["sunset"]}\nDurance={ds["durance"]}\n")
  return ouf.close()