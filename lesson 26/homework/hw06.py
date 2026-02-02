# 6) მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში, უარყოფითი რიცხვები კი პირიქით
positives = []
negatives = []

while True:
    value = input()
    if value.lower() == "stop":
        break
    num = int(value)
    if num > 0:
        positives.append(num)
    elif num < 0:
        negatives.append(num)

print("Positive numbers:", positives)
print("Negative numbers:", negatives)

