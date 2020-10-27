x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")


is_hungry = True
has_freckles = False


# Tuples 
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])
# dog[1] = 'dachshund'
# print(dog)


# List 
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

# dictionaries

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        


# Common Functions

print(type(2.63))
print(type(new_person))
print(len(new_person)) # (The number of key-value pairs)
print(len('Coding Dojo '))

# Type Casting or Explicit Type Conversion

print("Hello " + str(42))

total = 35
user_val = "26"
# total = total + user_val
total = total + int(user_val)
print(total)


# Conditional 

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   




# Loops

# for x in range(0, 10, 1): # First Value : Loop start, Second Value : Loop end , Thrid value : how to increment the iterator
# for x in range(0, 10):	# increment of +1 is implied
# for x in range(10):	# increment of +1 and start at 0 is implied


for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


my_list = ["abc", 123, "xyz"]
for v in my_list:
    print(v)

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
    print(k + ":" + my_dict[k])
# output: name, language


# another way to iterate through the keys
capitals = {"name": "title"}
for key in capitals.keys():
    print(key)
#to iterate through the values
for val in capitals.values():
    print(val)
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)


# While Loops

# for count in range(0, 5):
#     print("Looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1


y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


# break

for val in "String":
    if val == "i":
        break
    print(val)

# Continue

for val in "String":
    if val == "i":
        continue
    print(val)


y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1
