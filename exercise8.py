def sum_list(any_list):
    sum = 0
    for x in any_list:
        sum += x
    return sum
    
expenses = [250, 7.99, 30.95, 16.50]    
print(sum_list(expenses))

brand = [1, 2, 3]
print(sum_list(brand))
