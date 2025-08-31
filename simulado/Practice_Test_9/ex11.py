# what will be the output of the following snippet?

def show_truth():
    global mysterious_var # setando como variavel global
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
mysterious_var = 'Surprise'
print(mysterious_var) # # surprise: 
show_truth() # new surprise: 
print(mysterious_var) # new surprise: 
