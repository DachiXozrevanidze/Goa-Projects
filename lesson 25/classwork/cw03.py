# 3) შექმენი list, numbers = [10, 20, 30, 40, 50], მომხმარებელს ჰკითხე ინდექსი და pop()-ით წაშალე შესაბამისი ელემენტი
# დაბეჭდე:
# წაშლილი ელემენტი
# განახლებული list

numbers = [10, 20, 30, 40, 50]

index = int(input(" 5 "))

removed_element = numbers.pop(index)

print("წაშლილი ელემენტი:", removed_element)
print("განახლებული list:", numbers)