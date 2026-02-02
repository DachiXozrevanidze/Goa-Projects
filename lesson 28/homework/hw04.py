#4) მომხმარებელს შემოაყვანინე 5 რიცხვი, დაბეჭდე მათი ჯამი. გამოიყენე for loop და while loop.
numbers = []
for _ in range(5):
    numbers.append(int(input()))
total = 0
for n in numbers:
    total += n
print(total)

numbers = []
count = 0
while count < 5:
    numbers.append(int(input()))
    count += 1
total = 0
i = 0
while i < 5:
    total += numbers[i]
    i += 1
print(total)