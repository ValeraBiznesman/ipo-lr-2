import math
x= float (input("Введите x: "))
y= float (input("Введите y: "))
u=((8+math.fabs(x-y)**2 + 1)**(1/3)) / (x**2 + y**2 + 2) - math.exp(math.fabs(x-y))
print(f"Результат равен ={u}")