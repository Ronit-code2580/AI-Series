print ("my name")
print (123)

bucket = "water"
age = 24
isnepal = True

bucket = ["water", "juice", "milk", "tea", "coffee"] #list

print (bucket[0]) # water
print (bucket[-1]) 

countries = ["nepal", "india", "china", "japan"] #list
countries.pop() #pop() is used to remove the last value from the list
countries.append("pakistan")
countries.insert(1, "bhutan") #insert() is used to add new value in the list at specific index
countries.remove("china") #remove() is used to remove specific value from the list
print (countries)

animals = ("dog", "cat", "cow", "goat") #tuple
print (animals.count("dog")) #count() is used to count the number of specific value in the list
print (animals.index("cat")) #index() is used to find the index of specific value in the list

names = {"manish", "sanish", "rohan", "manish"} # set
print(names) #set is used to store unique values only


full_name = "Rojesh Adhikari"
college = "Kathmandu University"
address = "Kathmandu"
company = "loading "

personal_information = {
    
    "full_name": "Rojesh Adhikari",
    "college": "Kathmandu University",
    "address": "Kathmandu",
    "company": "loading ",
    "age"   : 24,
    "isnepal" : True
}

print(personal_information["full_name"])

personal_information["age"] = 25 #update the value of age
personal_information["color"] = "white" #add new key-value pair

perosnal_information.pop("college") #remove the key-value pair of college
 

print(personal_information)
# prediction ={
#     "image" : "image.jpg",
#     "class" : "cat",
#     "confidence" : 98.00
#  }
#----------------------------------- Data Cleaning -----------------------------------

'''
lstrip()
rstrip()
strip() -> combination of lstrip and rstrip
replace()
'''


# name = " --- MY---Sister's name is Suhata 1 2 3___" -> present data

# name - "My Sister's name is Sujata"

name = "  Samriddga"
newname = name.lstrip()
print(newname)

#----------------------
name = "Rojesh  "
newname = name.rstrip()
print(newname)
#----------------------


name = "Rojesh ** Adhikari"
newname = name.replace(" ** ", " ")
print(newname)

#----------------------

name = "__Rojesh Adhikari"
newname = name.lstrip("_")
print(newname)

#---------------------
name = "Rojesh Adhikari__"
newname = name.replace("__", "")
print(newname)

#-------------

name = "Rojesh Adhikari__"
newname = name.rstrip("__")
print(newname)

#---------------------
name = "--Rojesh Adhikari__"
newname = name.lstrip("--").rstrip("__")
print(newname)

#--------------------------

name = "  Rojesh  "
newname = name.strip()
print(newname)

#-----------------------

name = "1Rojesh2"
newname = name.strip("21")
print(newname)

#-----------------



# name = "   ---My --- Sister's name is Sujata 1 2 3 __  " -> present data

# name = "My Sister's name is Sujata"

name = "   ---My --- Sister's name is Sujata 1 2 3 __  "
# clear the front and rear part -> step 1
# clear the middle part by useing replace -> step 2

new_name = name.strip(" -123_")
print(new_name)

# new_name = My --- Sister's name is Sujata

new_name_final = new_name.replace(" --- "," ")
print(new_name_final)

#------------------ Data cleaning ------------------
name1 = "--- My name --- is Rojesh 123 Adhikari --"
# My name is Rojesh Adhikari

# new_name = name1.strip("- ").replace("123 ","").replace("--- ", "")


new_name = name1.strip("-, ").replace("123","").replace("--- ", "")
print(new_name)
