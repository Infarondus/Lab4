supplies = [['r', 3, 25], ['p', 2, 15], ['a', 2, 15], ['m', 2, 20], ['k', 1, 15], ['x', 3, 20], ['t', 1, 25], ['f', 1, 15], ['s', 2, 20], ['c', 2, 20], ['i', 1, 5]]
pack_size = 3 * 3
base_points = 15
mandatory = ['d', 1, 10]
total_value = sum([i[2] for i in supplies]) + mandatory[2]
remaining_capacity = pack_size - mandatory[1]
dynamique = [[['', 0] for _ in range(remaining_capacity + 1)] for _ in range(len(supplies) + 1)]
for i in range(len(supplies)):
    name, weight, value = supplies[i]
    for j in range(remaining_capacity + 1):
        if weight <= j:
            if value + dynamique[i][j - weight][1] > dynamique[i][j][1]:
                dynamique[i + 1][j][0] = dynamique[i][j - weight][0] + name * weight
                dynamique[i + 1][j][1] = dynamique[i][j - weight][1] + value
            else:
                dynamique[i + 1][j] = dynamique[i][j][:]
        else:
            dynamique[i + 1][j] = dynamique[i][j][:]

best_solution = dynamique[len(supplies)][remaining_capacity]
final_items = best_solution[0] + mandatory[0]
living_points = (best_solution[1] + mandatory[2]) * 2 - total_value
table = [[] for i in range(pack_size)]
for i in range(pack_size):
    table[i].append(final_items[i])
print(f'Текущий счёт: {living_points + base_points}')
print(f'Инвентарь:')
for r in range(0, pack_size, 3):
    print(*[table[i + r] for i in range(3)])

