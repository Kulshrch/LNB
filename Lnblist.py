L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
L3=list()
odd_elements=L1[0::2]
even_elements=L2[1::2]

L3.extend(odd_elements)
L3.extend(even_elements)
print("L3:",L3)