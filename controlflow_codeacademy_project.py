premium_gs = 125.00
weight = float(input('What is the weight that you want to ship? ' ))


def normal_ground_shipping(weight):
    if weight <= 2:
        cost = weight*1.5 +20.00
    if weight >= 2 and weight <= 6:
        cost = weight * 3 + 20.00
    if weight >= 6 and weight <= 10:
        cost = weight * 4.00 + 20.00
    if weight > 10:
        cost = weight * 4.75 + 20.00
    return cost

# print('cost for normal ground shipping is: ' + str(normal_ground_shipping(weight)

def drone_shit(weight):
    if weight <= 2:
        cost = weight*4.50
    if weight >= 2 and weight <= 6:
        cost = weight * 9.00
    if weight >= 6 and weight <= 10:
        cost = weight * 12.00
    if weight > 10:
        cost = weight * 14.25
    return cost

def cheapest_option(weight):
    if normal_ground_shipping(weight) > drone_shit(weight) and normal_ground_shipping(weight) > premium_gs :
        which_var = 'you should use drone shipping'
    if normal_ground_shipping(weight) < drone_shit(weight) and normal_ground_shipping(weight) < premium_gs :
        which_var = 'you should use normal ground shipping'
    if premium_gs < drone_shit(weight) and premium_gs < normal_ground_shipping(weight) :
        which_var = 'you should use premium ground shipping'
    return which_var
print(cheapest_option(weight))
print(normal_ground_shipping(weight))
print(drone_shit(weight))
print(premium_gs)
