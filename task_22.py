first_nabor = int(
    input("Введите кол-во элементов для первого набора чисел:  "))
second_nabor = int(
    input("Введите кол-во элементов для второго набора чисел:  "))

nabor_1 = []
nabor_2 = []

while len(nabor_1) < first_nabor:
    a = int(input("Элемент первого набора: "))
    nabor_1.append(a)
while len(nabor_2) < second_nabor:
    b = int(input("Элемент второго набора: "))
    nabor_2.append(b)
print(nabor_1, nabor_1, end=" ")

sort_nabor = set(nabor_1+nabor_2)
print(list(sorted(sort_nabor)))
