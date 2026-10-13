# Q6. Student Mark Conversion & Result Analyzer

students = int(input("Students: "))

print()
print(f"{'Student':<12}{'Total':<10}{'Average':<12}{'Grade'}")

for i in range(students):

    name = input("Student name: ")
    marks_input = input("Enter 3 marks: ").split()

    try:

        marks = []

        for value in marks_input:
            mark = float(value)

            if mark < 0 or mark > 100:
                raise ValueError

            marks.append(mark)

        if len(marks) != 3:
            raise ValueError

        total = sum(marks)
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 50:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print(f"{name:<12}{total:<10.0f}{average:<12.2f}{grade}")

    except ValueError:
        print(f"{name:<12}Invalid marks")