
def get_averege(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    averege = sum / len(input_numbers)
    print(averege)

get_averege([5.0, 3.5, 7.8, 9.9, 10.0])

def print_letter_count(text, letter):
    count = 0
    for char in text:
        if char ==  letter:
            count += 1
    
    print('Number of', letter, 'is', count)

print_letter_count('Paulo', 'P')
print_letter_count(letter='a', text='Paulo seja bem vindo')
