def print_grades(grades): # ????????? ?????? ?????? ?? ?????
    for grade in grades:
        print grades


def grades_sum(grades): # ??????? ??????? ????? ??????
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades): # ??????? ??????? ??????? ??????
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


def grades_variance(grades):
    average = grades_average(grades)
    variance = 0
    for grade in grades:
        variance += (average - grade) ** 2
    return variance / len(grades)


def grades_std_deviation(variance):
    return variance ** 0.5


grad = [120, 39, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 45, 76, 56]
var = grades_variance(grad)

for grade in grad:
    print grade

print "Summa scores ", grades_sum(grad)
print "Average scores " + str(grades_average(grad))
print grades_variance(grad)
print grades_std_deviation(var)
