# Q23

if __name__=='__main__':
    N = int(input('학생 수 N 입력:'))

    array = []
    for i in range(N):
        input_data = input().split()
        array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

    student_list = sorted(array, key = lambda x: (-x[1], x[2], -x[3]))

    for student in student_list:
        print(student[0]+'\n')