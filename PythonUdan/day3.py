'''
lstrip()
rstrip()
strip()
replace()
split()
captalize()
title()
'''

# name = "   ---rojesh @@ adhikari 123 ___  "
#result ="Rojesh Adhikari"

# name = "   ---rojesh @@ adhikari 123 ___  "
# newname = name.strip(" -123_")
# print(newname)

# newname2 = newname.replace(" @@ "," ")
# print(newname2)

# newname3 = newname2.title()
# print(newname3)

# # first_name = Rojesh and Last_name = Adhikari
'''
 after breaking 
 fist part -> first name 
 last part -> last name
'''
# first_name, last_name = newname3.split()
# print(first_name)
# print(last_name)

#----------------------------------practice-----------------

# name = "Rojesh#Bahadur#Adhikari"
# first, middle, last = name.split("#")

# print(first)
# print(middle)
# print(last)

# name = "rojesh adhikari"
# new_name = name.capitalize()
# print(new_name)

# -------------------------Task 1---------

# name = "  __-- rojesh ##&&  adhikari 123 @@"
# new_name = name.strip(" _-123@@").replace(" ##&& ","").title()

# first_name, last_name = new_name.split()
# print(first_name)
# print(last_name)

'''
output:
  Rojesh 
  Adhikari
'''

#----------------------------task 2 -------------------

# name = "  __--&*) rojesh ##&& adhikari 123 @@("
# new_name = name.strip(" _-&*)123@(").replace(" ##&& "," ").capitalize()
# print(new_name)
# first_name,last_name = new_name.split()
# print(first_name)
# print(last_name)


'''
output:
  Rojesh 
  adhikari
'''

#------------task 3--------------

# ph_no = "(+977)9808250812"
# ph_no1 = ph_no.replace("(+977)", "")
# ph_no2 = "(+977)" + ph_no1
# print(ph_no2)

#---------------task 4----------s

text = "$$ Samip ** % (+977)9808250812"
#first_name = Samip
#ph_no = 9808250812
clean_text = text.strip(" $").replace(" ** % ", " ")
first_name, nonclean_ph = clean_text.split()
ph_no = nonclean_ph.replace("(+977)","")
print(first_name)
print(ph_no)

#-----------task 5----------
name = "SamriDdha prasad Pathak"
new_name = name.title()
print(new_name)
# output: Samriddha Prasad Pathak

#---------------task 6-------------------
name = "   --- ### rojesh @@321 Ahikari 123 *"
new_name = name.title().strip(" -#123*").replace("@@321 ","")
print(new_name)
# output: Rojesh Ahikari

