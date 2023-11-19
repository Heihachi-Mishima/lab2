
# Online Python - IDE, Editor, Compiler, Interpreter

start_stovp = int(input("Введіть номер стовпця для першої клітинки (від 1 до 8): "))
start_riad = int(input("Введіть номер рядка для першої клітинки (від 1 до 8): "))
end_stovp = int(input("Введіть номер стовпця для другої клітинки (від 1 до 8): "))
end_riad = int(input("Введіть номер рядка для другої клітинки (від 1 до 8): "))

# Різниця між номерами стовпців і рядків повинна бути однаковою за модулем
stovp_difference = abs(end_stovp - start_stovp)
riad_difference = abs(end_riad - start_riad)

# Перевіряємо можливість ходу офіцера
if stovp_difference == riad_difference:
    print("Yes")
else:
    print("No")