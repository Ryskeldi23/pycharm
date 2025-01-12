name = input()
price = float(input())
weight = float(input())
money = int(input())

ret = price * weight
result = money - ret

print("Чек")
print(f"{name} - {int(weight)}кг - {int(price)}руб/кг")
print(f"Итого: {int(ret)}руб")
print(f"Внесено: {int(money)}руб")
print(f"Сдача: {int(result)}руб")
print("Hello")