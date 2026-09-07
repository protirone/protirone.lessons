# (C) 2026 K.Reincke: proTirone snippet [CC-BY-4.0]

# - loads a set of blood pressure measurements given as CSV file in format
#   id:str, day:str, time:str, systole:str, diastole:str, pulse:str
# - writes the set of measurements as CSV and JSON file
#
# Note: in intermediate representation systole, diastole, pulse are ints!

# compiled from preliminary work delivered by pupils of the class 12ip/iv23

import sys

class BP_Measurements:
  
  def __init__(self):
    self.series={}
  
  def fill_by_hardcoded_test_data(self):
    self.series={
      "1" : {"day": "2024-05-13","time": "07:00", "systole": 182, "diastole": 116, "pulse": 66},
      "2" : {"day": "2024-05-14","time": "06:30", "systole": 158, "diastole": 110, "pulse": 75},
    }

  # input adapter: read data from a csv file, containing only strings
  def fill_by_csv(self,filename):
    print(f"reading from csv file <{filename}>")
    self.series={}
    inf=open(filename,"r",encoding="utf-8")
    # keep it simple: let the program crash if filename does not exist
    for line in inf:
      csv_str=line.strip()
      (id,day,time,syst,diast,pulse)=csv_str.split(',')
      self.series[id]={"day": day, "time" : time, 
        "systole" : syst, "diastole" : diast, "pulse" : pulse  }

  # output adapter: write data into a csv file, containing only strings
  def write_as_strcsv(self,filename):
    print(f"writing to string csv file <{filename}>")
    ouf=open(filename,"w")
    # keep it simple: let the program crash if filename does not exist
    for id, ds in self.series.items():
      ouf.write(f"{id},{ds['day']},{ds['time']},"\
                f"{ds['systole']},{ds['diastole']},{ds['pulse']}\n")
  
  # output adapter: write data into a csv file containing strings and ints
  def write_as_intcsv(self,filename):
    print(f"writing to int csv file <{filename}>")
    ouf=open(filename,"w")
    # keep it simple: let the program crash if filename does not exist
    for id, ds in self.series.items():
      ouf.write(f"{id},{ds['day']},{ds['time']},"\
                f"{chr(ds['systole'])},{chr(ds['diastole'])},{ds['pulse']}\n")
  
  # output adapter: write data into a json file
  def write_as_json(self,filename):
    print(f"writing to json file <{filename}>")
    ouf=open(filename,"w")
    # keep it simple: let the program crash if filename does not exist
    jobo="{"
    jobc="}"
    succ=False
    ouf.write("[\n")
    for id, ds in self.series.items():
      if (succ):
        ouf.write(f",\n")
      else:
        succ=True
      ouf.write(f"  {jobo} \"{id}\" : {jobo}\n"\
        f"      \"day\" : \"{ds['day']}\",\n"\
        f"      \"time\" : \"{ds['time']}\",\n"\
        f"      \"systole\" : {(ds['systole'])},\n"\
        f"      \"diastole\" : {ds['diastole']},\n"\
        f"      \"pulse\" : {ds['pulse']}\n"\
        f"  {jobc}{jobc}")
    ouf.write("\n]")
  
if __name__=="__main__":

  bpm=BP_Measurements()

  # determine input data 
  if (len(sys.argv)>=2):
    if (sys.argv[1]=="test"): # file coded test data
      bpm.fill_by_csv("dsp.lf/dsp.alpha-t.csv")
    elif (sys.argv[1]=="real"): # file coded real data
      bpm.fill_by_csv("dsp.lf/dsp.alpha.csv")    
    else: 
      bpm.fill_by_hardcoded_test_data()
  else:
    bpm.fill_by_hardcoded_test_data()

  # write data using the selected output format
  if (len(sys.argv)==3):
    if sys.argv[2]=='csv2csv':
      bpm.write_as_strcsv("res.lf/bpm.alpha.csv")
    elif sys.argv[2] == 'csv2csv_with_ints':
      bpm.write_as_intcsv("res.lf/bpm.alpha.int.csv")
    elif sys.argv[2]=='csv2json':
      bpm.write_as_json("res.lf/bpm.alpha.json")
    else:
      bpm.write_as_strcsv("res.lf/bpm.alpha.csv")
  else:
    bpm.write_as_strcsv("res.lf/bpm.alpha.csv")
