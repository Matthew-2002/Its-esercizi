def cal_charges(ore: float) -> float:
    
    if ore % 1 != 0:
        ore = ore // 1 + 1
    if ore <= 3:
        costo = 2
    elif ore == 24:
        costo = 10
    else:
        costo = (ore -3)*0.5 + 2

    return costo      

print(f"{'veicolo':<10} {'ore':<10} {'costo':<10}")
charge_1 = cal_charges(1.5)
charge_2 = cal_charges(4)
charge_3 = cal_charges(24)
print(f"{'Car 1':<8} {'1,5 h':<8} {charge_1:<8}")
print(f"{'Car 2':<8} {'4 h':<8} {charge_2:<8}")
print(f"{'Car 3':<8} {'24 h':<8} {charge_3:<8}")