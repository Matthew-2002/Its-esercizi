def convert_temperature(temp: float, to_fahrenheit: bool = None) -> float:
    if to_fahrenheit == False:
        temp = ((temp - 32) * 5/9)
    else:
        temp = (temp * 9/5) + 32
    return temp