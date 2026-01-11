# Task 21
def check_failing(grades_grid):
    
   for i, scores in enumerate(grades_grid):
     for score in scores:
        if score <50:
           print(f"student {i} failed a subject")

all_grades = [
        [88, 92, 70],   # Student 0 
        [45, 80, 77],   # Student 1 (Has a 45!)  
        [99, 100, 95]   # Student 2
     # ]


 # Task 2
def active_row(screen, row_index):
      for i in range(len(screen[row_index])):
        screen[row_index][i]= 1 
        
monitor = [
           [0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]
]
active_row(monitor,1)
print (monitor)
   