print(5 - 3 ** 4 / 4)
"""
Exponentiation has the highest priority, so we start with 3 ** 4, which is 3 * 3 * 3 * 3 = 81. This
leaves us with 5 - 81 / 4. Division has higher priority than subtraction, so 81 / 4 = 20.25. Finally, 
5 - 20.25 = -15.25.
"""