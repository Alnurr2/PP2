import re 

with open("Practice05/raw.txt", "r", encoding='utf-8') as file:
    data = file.read()

prices = re.findall(r"(Стоимость)\n(\d+.+)",data)

print(prices)