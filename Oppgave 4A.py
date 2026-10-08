import random as rand

def rand_num(a,b):
    return rand.randint(a, b)

def volume_box(l,b,h):
    return l * b * h

n_boxes = 10

for i in range(n_boxes):
    r_l = rand_num(1, 4)
    r_b = rand_num(2, 6)
    r_h = rand_num(1, 3)
    box = volume_box(r_l, r_b, r_h)
    print(f"{box}m^3")

"""
====================================
Kjøreeksempel:
====================================
12m^3
18m^3
8m^3
36m^3
12m^3
8m^3
8m^3
12m^3
4m^3
54m^3

Process finished with exit code 0
"""3
