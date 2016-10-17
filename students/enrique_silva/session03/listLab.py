#list lab, working with lists.

#create a list of fruits and print the list
fruits=['Apples','Pears','Oranges','Peaches']

print(fruits)
print()

#request input from user to add a fruit to the list
new_fruits=input('What fruits would you like to add to the list? ')

fruits.append(new_fruits)

print(fruits)
print()

#display the fruit based on the number the customer chooses.
number_fruits=int(input('Pick a number: '))

print("You picked #", number_fruits, "which means your fruit is: ", fruits[number_fruits-1])
print()

#add fruits to the list using several different methods.
fruits=['watermelon'] + fruits

print(fruits)
print()

fruits.insert(0,'cantelope')

print(fruits)
print()

#create a loop that iterates on the list and prints out in a new list all
#the fruits tha start with a P
fruits_with_p=[]

for name in fruits:
	if name.startswith('p') or name.startswith('P'):
		fruits_with_p.append(name)

print(fruits_with_p)











