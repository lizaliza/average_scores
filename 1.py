def print_grades(grades): # Procedure output the evaluation on the screen
    for grade in grades:
        print grades


def grades_sum(grades): # Function calculates the sum of the estimates
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades): # Function calculates the average rating
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


def grades_variance(grades): # Function calculates the measurement error
    average = grades_average(grades)
    variance = 0
    for grade in grades:
        variance += (average - grade) ** 2
    return variance / len(grades)


def grades_std_deviation(variance): #  Function to calculate the standard deviation
    return variance ** 0.5


grad = [120, 39, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 45, 76, 56]
var = grades_variance(grad)

for grade in grad:
    print grade

print "Summa scores =", grades_sum(grad)
print "Average scores =",str(grades_average(grad))
print "Variance scores =",grades_variance(grad)
print "Std_deviation =",grades_std_deviation(var)
