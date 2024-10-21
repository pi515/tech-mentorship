# # *** Lists ***
# Python lists store multiple items in a single variable. They are created using square brackets [ ]. Lists are ordered, changeable, and allow duplicate values. They are defined with the data type “list”.

# They are also indexed like strings: the first item has index [0], the second item has index [1], and so on.

# Lists have a defined order that will not change. If a new item is added to the list, it will be placed at the end.


# # *** Exercise - Lists
# myList = ["spring", "summer", "fall", "winter"]
# print(myList)

# # To determine how many items a list has, use the len() function.

# print(len(myList))

# # Lists can be of an contain any data types.

# L1 = ["October", 31, "Halloween", True]
# print(L1)

# # You can also use the constructor list() to make a list. (tuple)

# months = list(("June", "July", "August"))
# print(months)


# *** Exercise - Access Lists -
# List items can be accessed by referencing their index number.

# numList = [1, 1, 2, 3, 5, 8, 13, 21]
# print(numList[2])

# # You can also access a range of items by specifying their indexes.

# print(numList[0:3])
# print(numList[4:])

# # To determine if a specific item is present in a list, use the in keyword

# print(34 in numList)


# # *** Exercise - Change Lists -
# # To change the value of a specific item, refer to the index number.

# colorList = ["red", "yellow", "blue"]
# colorList[0] = "green"
# print(colorList)

# # You can also use this method to change a range of items within a list. The already existing items in the list will move accordingly.

# colorList[0:1] = ["purple", "gray", "orange"]
# print(colorList)

# # To insert a new item without replacing any existing values, you can use the insert() method.

# colorList[1:4] = ["brown"]
# print(colorList)


# # *** Exercise - Add List Items -
# # To add an item to the end of a list, use the append() method.

# flavors = ["chocolate", "vanilla"]
# flavors.append("strawberry")
# print(flavors)

# # You can append items from one list to another using the extend() method

# flavors2 = ["mint", "caramel"]
# flavors.extend(flavors2)
# print(flavors)


# # *** Exercise - Remove List Items -
# # The remove() method removes a specified item.

# months = ["Sep", "Oct", "Nov", "Dec", "Jan"]
# months.remove("Nov")
# print(months)

# #The pop() method and the del keyword both remove a specified index.

# months.pop(1)
# print(months)
# del months[2]
# print(months)

# #The clear() method clears the content of a list.
# months.clear()

# print(months)


# *** Exercise - Sort Lists -
# Lists have a sort() method that will sort the list ascending alphanumerically by default. This method will not work on lists that contain mixed data types.

# someList = [19, 5, 46]
# someList.sort()
# print(someList)

# #To sort by descending order, use the keyword argument reverse = True

# someList.sort(reverse = True)
# print(someList)


# # *** Exercise - Copy Lists-
#To copy a list, you can use the copy() method. Typing list2 = list1 will not work because list2 will only be a reference to list1, and any changes made on one list will reflect on the other.

# list1 = [5, 10, 15]
# list2 = list1.copy()
# print(list2)

# # You can also use the list() method to copy a list.

# list3 = list(list2)
# print(list3)

# list2.clear()
# print("list2:", list2)
# print("list3:", list3)


# # *** Exercise - Reference to list vs copy of list -

# list4 = list1
# print("list4:", list4)
# list1.clear()
# print("list4:", list4)


# # *** Exercise - Join -
# # The + operator can be used to join two or more lists.

# L1 = ["a", "b", "c"]
# L2 = [1, 2, 3]
# L3 = L1 + L2
# print(L3)

# # You can also use the append() method to add all items from L1 to L2.

# for x in L2:
#   L1.append(x)
# print(L1)

# # Or you can use the extend() method.

# L1.extend(L2)
# print(L1)
