import sys

studentName = ["Terry", "John", "Susan", "Rondell", "Aaron", "Kalifa"]
studentGrade = [[79, 85, 82], [65, 69, 73], [91, 93, 80], [45, 70, 81], [83, 85, 80], [90, 93, 82]]

def calculateAverage(dataset, studentName):
    if studentName in dataset.keys():
        average_grade = 0.0
        for i in range(len(dataset[studentName])):
            average_grade += dataset[studentName][i]

        return average_grade / len(dataset[studentName])

    else:
        return None

def lowestGrade(dataset, studentName):
    if studentName in dataset.keys():
        lowest_grade = sys.maxsize
        for i in range(len(dataset[studentName])):
            if lowest_grade > dataset[studentName][i]:
                lowest_grade = dataset[studentName][i]
        return lowest_grade
    else:
        return None

def highestGrade(dataset, studentName):
    if studentName in dataset.keys():
        highest_grade = -sys.maxsize
        for i in range(len(dataset[studentName])):
            if highest_grade < dataset[studentName][i]:
                highest_grade = dataset[studentName][i]
        return highest_grade
    else:
        return None


def main():
    data = {}
    for i in range(len(studentName)):
        data[studentName[i].lower()] = studentGrade[i]

    student_name = input("Student's name:").lower()
    print('Lowest Grade: %s' % lowestGrade(data, student_name))
    print('Highest Grade: %s' % highestGrade(data, student_name))
    print('Average Grade: %s' % calculateAverage(data, student_name))


if __name__ == '__main__':
    main()