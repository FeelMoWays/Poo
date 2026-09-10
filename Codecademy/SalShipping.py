weight = 41.5
ground_shipping_cost = 0
ground_premium = 125
drone_shipping_cost = 0
#Ground Shipping
if weight <= 2:
    ground_shipping_cost += (weight * 1.50) + 20
elif weight > 2 and weight <= 6:
    ground_shipping_cost += (weight * 3.00) + 20 
elif weight > 6 and weight <= 10:
    ground_shipping_cost += (weight * 4.00) + 20 
else:
    ground_shipping_cost += (weight * 4.75) + 20 
#Drone Shipping
if weight <= 2:
    drone_shipping_cost += (weight * 4.50) 
elif weight > 2 and weight <= 6:
    drone_shipping_cost += (weight * 9.00) 
elif weight > 6 and weight <= 10:
    drone_shipping_cost += (weight * 12.00) 
else:
    drone_shipping_cost += (weight * 14.25)
