def check_failing(grades_grid):
    for i, scores in enumerate(grades_grid):
        for score in scores:
            if score < 50:
                print(f"Student {i} failed a subject")

grades = [
    [88, 92, 70],
    [45, 80, 77],
    [99, 100, 95]
]

check_failing(grades)
