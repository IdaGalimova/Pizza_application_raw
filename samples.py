diction_pep = {
    "pep": 5,
    "haw": 10,
}

# diction_haw = {
#     "pizza name": "hawaii",
#     "amount": 5,
#     "price": 15,
#     "description": "mozarella, bla, bla"
# }

diction = {}
# diction = diction_pep | diction_haw
# diction["pep"] = diction_pep["amount"]
# diction["haw"] = diction_haw["amount"]
# print("Printing dictionary:", diction)

print(sum(diction_pep.values()))

# for key, value in diction_pep.items():
#     if key == "pizza_name":
#         print("BLALA")
#     else:
#         print(0)
    # print("Item:", key)
    # print("Value:", value)