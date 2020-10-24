if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    totalMarks = 0
    for name in student_marks:
        if name == query_name:
            count = 0
            for marks in student_marks[name]:
                totalMarks += marks
                count += 1
            totalMarks /= count

    print ("%0.2f" % totalMarks)