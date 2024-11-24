grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Переводим множество студентов в список
students = list(students)
# Сортируем студентов по алфавиту
students = sorted(students)
# Считаем средний бал
gpa = (sum(grades[0])/len(grades[0]),
      sum(grades[1])/len(grades[1]),
      sum(grades[2])/len(grades[2]),
      sum(grades[3])/len(grades[3]),
      sum(grades[4])/len(grades[4]))
# Собираем словарь
gpa_dict = {students[0]: gpa[0],
            students[1]: gpa[1],
            students[2]: gpa[2],
            students[3]: gpa[3],
            students[4]: gpa[4],}
print(gpa_dict)


