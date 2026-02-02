#5) მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში და გამოითვალე ამ რიცხვების საშუალო არითმეტიკული.
numbers = []

while True:
    value = input()
    if value.lower() == "stop":
        break
    numbers.append(int(value))

average = sum(numbers) / len(numbers)
print(average)