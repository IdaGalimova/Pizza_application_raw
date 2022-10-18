# trying to make csv work:
import csv, time

header = ['ID', "table_number", "time", "order"]

order = {
    "pepperoni_amount": 15,
    "hawaii": 5
}

data = {'ID': '0', "table_number": '0', "time": "0", "order": "0"}

data["ID"] = '4'
data["table_number"] = '5'
data["time"] = '13:47:37'
data["order"] = order

csv_file = "order_data.csv"

with open(csv_file, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    # writer.writeheader()
    
    writer.writerow(data)

with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    general_data_list = []
    for line in reader:
        general_data_list.append(line)
        

for general_data in general_data_list:
    # print(line)   
    order = {}
    exec("data2 = " + general_data["order"]) 
    print(general_data["ID"], order["pepperoni_amount"])