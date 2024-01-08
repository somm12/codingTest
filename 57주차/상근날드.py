burger = 2000
drink = 2000
for _ in range(3):
    a = int(input())
    burger = min(burger,a)

for _ in range(2):
    a = int(input())
    drink = min(drink,a)
print(burger+drink-50)
