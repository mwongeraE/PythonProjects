def grades_average(grades):
    grades_sum(grades)
    avrg = grades_sum(grades) / float(len(grades))
    print avrg
    return avrg

grades_average(grades)
