print('Hello', 'How are you', end='.', sep='-')

def print_letter_count(text='This is the default string to search', letter='a'):
    count = 0
    for char in text:
        if char ==  letter:
            count += 1
    
    print('Number of', letter, 'is', count)

print_letter_count()
