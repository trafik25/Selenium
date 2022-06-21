

my_dictionary = {} #init empty dictionary

#init dictionary with some key-value pair
another = {
            #key    : value,
            'man'   : 'Bob',
            'woman' : 'Alice',
            'other' : 'Trudy'
        }

#print initial dictionaries
print(my_dictionary)
print(another)

#insert value
my_dictionary['day']='Monday'
my_dictionary['color']='REd'
my_dictionary['woman']='Tammy'
my_dictionary['other']='Tommy'
#print updated dictionaries
print('Updated Dictionaries:')
print(my_dictionary)
print(another)

#update values
my_dictionary['day']='Friday'
another['day']='Friday'
my_dictionary['color']='Black'
another['color']='Black'
print("After updated values are added")
print(my_dictionary)

#printing a single element
print(my_dictionary['day'])
print(another['color'])