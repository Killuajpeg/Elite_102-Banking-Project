#Possibly add user passwords and a limit so the user cant just withdrawl


from bank_account import BankAccount

user_id = input("Enter your user ID: ")
account = BankAccount(user_id)
account.create_account()

while True:
    print('\nChoose an option:')
    print('1.) Check Balance')
    print('2.) Deposit')
    print('3.) Withdraw')
    print('4.) Exit')
    print('5.) Delete Account')

    choice = input('Enter your choice (1-5): ')

    if choice == '1': #RETURN BALANCE    
        account.get_balance()

    elif choice == '2': #TAKE IN DEPOSIT
        try:
            amount = float(input('Enter the amount to Deposit: ')) #Turn the users input into a float data type & then equate it to the amount var
            if amount <= 0: #If the amount that the user wants to deposit is 0:
                print ('Deposit amount must be greater than zero.')
            else: #Deposit the users requested amount into their account
                account.take_deposit(amount)
        except ValueError:
            print ('Invalid input. Please enter a valid number.')

    elif choice == '3':
        try:
            amount = float(input('Enter the amount to Withdrawl: ')) #Turn the users input into a float data type & then equate it to the amount var
            if amount <= 0: #If the amount that the user wants to withdrawl is 0:
                print ('Withdrawl amount must be greater than zero.')
            else: #Withdrawl the users requested amount from their account
                account.pull_withdrawl(amount)
        except ValueError:
            print ('Invalid Input. Please enter a valid number.')

    elif choice == '4':
        print("\nGoodbye!\nThank you for banking with us!\n")
        break

    elif choice == '5':
        print ('\nDanger Zone!')
        decision = input(f'Are you sure you would like to delete the account "{user_id}"? (Y/N): ').upper()
        if decision == 'Y':
            account.del_account()
            print (f'\nThe account "{user_id}" has now been deleted.\nThank you for banking with us!')
            exit()
        elif decision == 'N':
            pass
        else:
            print ('Please enter a valid input. ("Y" or "N")')

    else:
        print("Invalid choice. Try again.")
