#Conditional Statements
balance = 100
price = 40

if balance >= price:
    answer = input('Do you want to continue? Enter Yes or No:')
    answer.lower()
    if answer == 'Yes':
        print('We will move on.')
    elif answer == 'No':
        print('We will stop')
    else:
        print('Invalid answer!')
    new_balance = balance - price
    print(f'if you can book the flight and your new balance will be: {new_balance}')
else:
    print(f'Insufficient funds! Please deposit {price - balance}.')


















