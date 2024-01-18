import math

list=[
    #['nome', 'radius', 'height', 'cost per can'],
['#1 Picnic', 6.83, 10.16, 0.28],
['#1 Tall', 7.78, 11.91, 0.43],
['#2',	8.73,	11.59,	0.45],
['#2.5',	10.32,	11.91,	0.61],
['#3 Cylinder',	10.79,	17.78,	0.86],
['#5',	13.02,	14.29,	0.83],
['#6Z',	5.40,	8.89, 0.22],
['#8Z short',	6.83,	7.62,	0.26],
['#10',	15.72,	17.78,	1.53],
['#211',	6.83,	12.38,	0.34],
['#300',	7.62,	11.27,	0.38],
['#303',	8.10,	11.11,	0.42]

]

def main():
    best_storage_efficiency_value = -1
    best_storage_efficiency_can_name = None
    best_cost_efficiency_value = -1
    best_cost_efficiency_can_name = None
    for row in list:
        name = row[0]
        radius = row[1]
        height = row[2]
        cost = row[3]
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        if storage_efficiency > best_storage_efficiency_value:
            best_cost_efficiency_value = storage_efficiency
            best_storage_efficiency_can_name = name
        if cost_efficiency > best_cost_efficiency_value:
            best_cost_efficiency_value = cost_efficiency
            best_cost_efficiency_can_name = name
        print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')
    print(f'The best storage efficiency can is: {best_storage_efficiency_can_name}')
    print(f'The best cost efficiency can is: {best_cost_efficiency_can_name}')

def comput_volume(radius, height):
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    volume = comput_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    return comput_volume(radius, height) / cost


main()