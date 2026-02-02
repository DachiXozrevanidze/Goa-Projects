#6) შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი, ყველა დაამატე list-ში და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში
numbers = []

for _ in range(5):
    num = int(input())
    numbers.append(num)

total = 0
for n in numbers:
    total += n

print(total)