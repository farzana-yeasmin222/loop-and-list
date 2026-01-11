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
   # Filter
   low_quality_log = []
   # Separate readings into two lists
for value in readings:
      if value <15.0:
       low_quality_log.append(value)
       # Keep only values >=15.0
       readings = [item for item in readings if item >=15.0 ]
       print(readings)
       print(low_quality_log)
