import datetime

store_list =["Meat", "Cheese"]
#["apple", "oranges", "banana", "chicken" , "potatoes", "milk"]

date_time= datetime.datetime.now()
month = str(date_time.month)
day = str(date_time.day)
hour = str(date_time.hour)
minute = str(date_time.minute)


print("Welcome to the Grocery List App.""\n","Current Date and Time:", date_time)
print("You currently have ",store_list[0],"and", store_list[1], "in your list")
add_to_list1 = input("Type of food to add to the grocery list:")

store_list.append(add_to_list1.title())

add_to_list2 = input("Type of food to add to the grocery list:")
store_list.append(add_to_list2.title())

add_to_list3 = input("Type of food to add to the grocery list:")
store_list.append(add_to_list3.title())

print("\nHere is your grocery list: ""\n",store_list )
sort= sorted(store_list)
print("Here is your grocery list sorted:\n", sort, "\n")
#1
print("Simulating grocery shopping...\n")

print("Current grocery list: ", len(store_list), " items.\n", store_list)
grocery=input("what food did you buy: ")
store_list.remove(grocery.title())
print("Removing ",grocery, " from list...\n")

#2
print("Current grocery list: ", len(store_list), " items\n", store_list)
grocery=input("what food did you buy: ")
store_list.remove(grocery.title())
print("Removing ",grocery, " from list...\n")

#3
print("Current grocery list: ", len(store_list), " items.\n", store_list)
grocery=input("what food did you buy: ")
store_list.remove(grocery.title())
print("Removing ",grocery, " from list...\n")

#if list is less than two items ,store is out of an item prompt.....
if len(store_list) <= 2:
    print("Current grocery list:", len(store_list), "items")
    print(store_list,"\n")
    print("Sorry, the store is out of", store_list[0])
    replace_food= input("What food would you like instead: ")
    store_list.remove(store_list[0])
    store_list.append(replace_food.title())

print("\nHere is what remains on your grocery list: \n", store_list)
print("Testing something with git")
