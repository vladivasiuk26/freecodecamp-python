age = int(input('Enter your age: '))
show_time = input('Enter the show time you would like to book: ')
seat_type = input('Enter the seat type you would like to book: ')
if age >= 18:
    print('You are eligible to book a ticket')
else:
    print('You are not eligible to book a ticket')
if show_time == 'Evening' and age >=18:
    print('you are eligible to book an Evening ticket')
else:
    print('You are not eligible to book an Evening ticket')
if show_time == 'Afternoon' and age >=15:
    print('You are eligible to book an Afternoon ticket')
else:
    print('You are not eligible to book an Afternoon ticket')
charges = 0
if seat_type == 'Normal':
    charges = 0
    print('Charges:', charges)
if seat_type == 'Premium':
    charges = 5
    print('Charges:', charges)
if seat_type == "Luxury":
    charges = 10
    print('Charges:', charges)
is_member = input('Are you a member? (yes/no): ')
yes = True
no = False
discount = 0
if is_member:
    print('You are eligible for membership discount')
    discount = 3
    print('Discount:', discount)
else:
    print('You are not eligible for membership discount')

total_price = base_price + charges - discount
print('Your total price for ticket is:', total_price)
