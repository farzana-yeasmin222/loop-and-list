readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]
# Cleaner
for i in range (len(readings)):
  if readings [i] == "Error":
     readings [i] = 0.0
     #print (readings)
# Multipyer
for i in range (len(readings)):
   readings [i] = readings [i] * 1.1
   print (readings)
   # low_quality_log = []
   # Filter
   i = 0
   #commit