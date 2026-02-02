# 1) შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ არ დაწერს "stop".დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია
numbers = []

while True:
    value = input()
    if value.lower() == "stop":
        break
    num = int(value)
    if num > 0:
        numbers.append(num)

print(numbers)

