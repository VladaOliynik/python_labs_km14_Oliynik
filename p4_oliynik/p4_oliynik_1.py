#below we make variables for input
name = input('Enter your name: ')
surname = input('Enter your surname')
number = input('Enter your phone number: ')
street = input('Enter your street name:')
building = input('Enter your building number')
apartment = input('Enter your apartment number')
city = input('Enter your city name')
postcode = input('Enter your postcode:')
country = input('Enter the name of your country:')
#then the data entered in the variable will be displayed
print("{} {}\n{}\nStr.{} {},ap.{} {}\n{}\n{}".format(name,surname,number,street,building,apartment,city,postcode,country))