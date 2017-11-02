def grades_variance(grades):
    variance = 0
    for n in grades:
        variance += ((grades_average(grades) - n) ** 2)
    return variance / len(grades)
print grades_variance(grades)
