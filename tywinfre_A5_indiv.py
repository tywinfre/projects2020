#1 %B

#2 1. import csv and datetime 2. use DictReader in order to read in the csv file 3. create an empty list 4. use a for loop to iterate over date column 5. create an if statement that shows only the items sold on the weekend


#3 
import csv
import datetime

data = csv.DictReader(open("ShopRecords.csv", "r"))





empty_list = []

for item in data:
    shop_list = item['Date'].split("/")
    
    date = datetime.date(int(shop_list[2]), int(shop_list[0]), int(shop_list[1]))
    if date.strftime("%A") == "Saturday" or date.strftime("%A") == "Sunday":
        empty_list.append(item["Item"])


print(*empty_list, sep = "\n")

