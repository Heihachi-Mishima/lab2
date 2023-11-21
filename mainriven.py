"""
1. Напишіть програму виведення текстового варіанта шкільних
оцінок: 1, 2, 3 (початковий рівень - initial level), 4, 5, 6 (середній
рівень - average level), 7, 8, 9 (достатній рівень - sufficient
level), 10, 11, 12 (високий рівень - high level).
Автор: Стерпул Юрій 
"""
grade = int(input("Enter grade: "))
        
match grade:
    case 1 | 2 | 3:
        print("initial level")
    case 4 | 5 | 6:
        print("average level")
    case 7 | 8 | 9:
        print("sufficient level")
    case 10 | 11 | 12:
        print("high level")
    case _:
        print("Grade is below or over the grading system")
