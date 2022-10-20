diction_pep = {
    "pepperoni": 1
}

diction_haw = {
    "hawaii": 3
}

diction_final = diction_pep | diction_haw
# dest = {**orig, **extra}    

print("Printing final dictionary:", diction_final)

