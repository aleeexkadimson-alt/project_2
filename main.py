students = ["Anna", "Mark", "Ali"]
grades = [90, 75, 85]
name = ""

# def add_student():
    
        # name = input("Enter new student:")
        # if name in students:
        #  raise ValueError("Студент уже существует")
        # else:
        #     students.append(name)
        #     show_all_students()
def add_student(students, grades):
            name = input("Ввелите нового студента:")
            grade = int(input("Оценка этого студента:"))
            if name in students:
                raise ValueError("Студент уже существует")
            if not 0 <= grade <= 100:
                raise ValueError("Оценка должна быть от 0 до 100")
            students.append(name)
            grades.append(grade)
            show_all_students()
    
      
def show_all_students():
      print("STUDENTS:")
      for i in range(len(students)):
            print(students [i], "-" , grades[i])
      

def find_student(students, grades, name):
    name = input("Давай найдем студента!:")
    if name not in students:
        raise ValueError("Студент не найден")
    index = students.index(name)
    print(name, "-", grades[index])

     
def change_score():
      name = input("Введите имя студента:")
      if name in students:
            index = students.index(name)
            new_grade = int(input("Введите новую оценку:"))
            grades[index] = new_grade
      else:
            print("Студент не найден")      

      pass
def delete_student():
    name = input("Введите имя студента:")
    if name in students:
        students.remove(name)
        show_all_students()
    elif name not in students:
        raise ValueError("Студент не существует")
      
def average_score():
      if len(grades) > 0:
            average = sum(grades) / len(grades)
            print(f"Средний балл:", average)
      else:
            print("Нет оценок для расчета")
def exit():
      print("Пока пока")

def menu():
        while True:
            print(f"""
************Меню программы************        
1. Добавить студента
2. Показать всех студентов
3. Найти студента
4. Изменить оценку
5. Удалить студента
6. Средний балл
0. Выход""") 
            try:
                choice = int(input("Введите число 0-6:"))
                print(choice)
            except ValueError:
                  print("Ввели не число")
            try:      
                if choice == 1:
                      add_student(students, grades)
                elif choice == 2:
                  show_all_students()
                elif choice == 3:
                      find_student(students, grades, name)
                elif choice == 4:
                      change_score()
                elif choice == 5:
                      delete_student()
                elif choice == 6:
                      average_score()
                elif choice == 0:
                      exit()
                      break
                else:
                      print("Ошибка!!! Такого пункта нет в меню")
            except ValueError:
                 print("ОШИБКА" \
                 "ВЫ ЧТО ТО НЕ ПРАВИЛЬНО ВВЕЛИ")   




menu()