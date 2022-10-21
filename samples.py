diction_pep = {
    "pizza_name": "pepperoni",
    "amount": 5,
    "price": 10
}

diction_haw = {
    "hawaii": 10
}

diction = {}
diction = diction_pep| diction_haw    

print("Printing final dictionary:", diction)

for key, value in diction_pep.items():
    if key == "pizza_name":
        print("BLALA")
    else:
        print(0)
    # print("Item:", key)
    # print("Value:", value)