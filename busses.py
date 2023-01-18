bus_cap = 52

def calc_bus(students):
    if students % bus_cap == 0:
        return (int(students / bus_cap))
    else:
        return (int(students / bus_cap) + 1)

print (calc_bus(521))