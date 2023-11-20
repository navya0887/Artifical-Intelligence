def gcd(a, b):  
    if b == 0:  
        return a  
    else:  
        return gcd(b, a % b)  
  
def can_measure_water(jug1_cap, jug2_cap, target):  
    if target > jug1_cap + jug2_cap:  
        return False  
    if jug1_cap == 0 or jug2_cap == 0:  
        return target == 0 or target == jug1_cap + jug2_cap  
    return target % gcd(jug1_cap, jug2_cap) == 0  
  
def measure_water(jug1_cap, jug2_cap, target):  
    if not can_measure_water(jug1_cap, jug2_cap, target):  
        return []  
gcd_val = gcd(jug1_cap, jug2_cap)  
    a, b = jug1_cap // gcd_val, jug2_cap // gcd_val  
    if a > b:  
        a, b = b, a  
        jug1_cap, jug2_cap = jug2_cap, jug1_cap  
    q2 = target // gcd_val  
    while q2 > 0:  
        q1 = (target - b * q2) // a  
        yield ('fill', 1)  
        yield ('pour', 1, 2)  
        yield ('empty', 2)  
        yield ('pour', 1, 2)  
        yield ('fill', 1)  
        yield ('pour', 1, 2)  
        q2 -= 1  
        target -= a  
jug1_cap = 4  
jug2_cap = 3  
target = 2  
  
if can_measure_water(jug1_cap, jug2_cap, target):  
    print(list(measure_water(jug1_cap, jug2_cap, target)))  
else:  
print("Cannot measure the desired amount of water.")  
