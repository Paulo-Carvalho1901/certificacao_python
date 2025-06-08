def get_averege(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    averege = sum / len(input_numbers)
    return averege

# print('The averege is. ', get_averege([5.0, 3.5, 7.8, 9.9, 10.0]))

averege = get_averege([5.0, 3.5, 7.8, 9.9, 10.0])
if averege > 5.0:
    print('The averege is too hight.')


def get_averege(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    averege = sum / len(input_numbers)
    return averege
    print('Show me')

get_averege([2])

def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 40, 10]))
print(is_first_last_equal([20, 20, 30, 40, 10]))
