fev_band = 'Green Day'
print(fev_band[6])
print(fev_band[:6])

print()

text = 'Please capitalize me'
text_cap = text.upper()
text_low = text.lower()
print(text_cap)
print(text_low)

print()

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number.')
else:
    print('Sorry', user_number, 'is not a number.')
    