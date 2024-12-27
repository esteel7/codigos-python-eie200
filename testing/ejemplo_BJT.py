r1 = 50e3
r2 = 50e3
rc = 2.7e3
re = 3.3e3
rth = r1*r2/(r1+r2)
vcc = 5
vth = vcc * r2/(r2 + r1)
vbe = 0.7
beta = 100
vce_min = 0.3

ib = (vth - vbe)/((beta + 1) * re + rth)
vb = vth - ib * rth
vc = vcc - rc * beta * ib
ve = (beta + 1) * ib * re

vce = vc - ve

print(f"vth = {vth} V\nib = {ib * 1000} mA\nvb = {vb} V\nvc = {vc} V\nve = {ve} V\nvce = {vce} > {vce_min} V? {vce > vce_min}")