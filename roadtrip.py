def roadtrip(distance, efficiency, gas_cost):
    cost = gas_cost*(distance/efficiency)
    return cost

print (roadtrip(60, 20, 5))