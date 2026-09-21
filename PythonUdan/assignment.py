#-----task 1---
text = "  Hello, World!  "
cleaned = text.strip()
print(cleaned)

#------task 2-----
name = "***Welcome"
print(name.strip('*'))

#-----task 3----
name2 = "Goodbye!!!"
cleaned2 = name2.rstrip("!")
print(cleaned2)

#------task 4----
name3 = "python is fun"
result = name3.capitalize()
print(result)

#------task 5-------
name4 = "john doe"
result2 = name4.title()
print(result2)

#-------task 6------
names = ["  Alice", "Bob  ", "  Charlie  "]
result3 = [n.strip() for n in names]
print(result3)

#--------task 7----
name5 = "#hello$"
result4 = name5.strip("#$")
print(result4)
#-------task 8 -------
names = ["alice", "bob", "charlie"]
result5 = [name.capitalize() for name in names]
print(result5)

#----------task 9------
data ={"name": "Alice ", "city": "London  "}
cleaned ={k: v.rstrip() for k, v in data.items()}
print(cleaned)

#----------task 10-------
sentences = ["hello world", "python is fun"]
result6 = [s.title() for s in sentences]
print(result6)

#----------task 11-----
name6 = "  hello PYTHON world   "
result7 = name6.title().strip()
print(result7)

#-------task 12--------
emails = ["  alice@example.com", "bob@example.com  "]
result8 = [e.strip() for e in emails]
print(result8)

#-------task 13------
text1 = ("12345abc")
result9 = text1.lstrip("12345")
print(result9)

#-----task 14------
nested = [["  apple", "banana  "], ["  cherry  "]]
result10 =[[n.strip() for n in sublist] for sublist in nested]
print(result10)

#--------task 15--------
text2 = "  hello world  "
result11 = text2.strip().capitalize()
print(result11)

#---------task 16--------

data = {"name_": "Alice", "age_": 30}
result12 = {k.rstrip("_"): v for k, v in data.items()}
print(result12)
#--------task 17-----------

name3 = [" alice ", "Bob", "bob", "ALICE"]
result13 = list(set(n.strip().capitalize() for n in name3))
print(result13)

#-----task 18--------
text = "***-hello-***"
result14 = text.strip("*-")
print(result14)

#---------task 19----------

tags = ["#python", "java", "#c++"]
result15 = [t.lstrip("#") if t.startswith("#") else t for t in tags]
print(result15)

#------task 20-----

products = ["  apple", " -Banana", "apricot", "banana  " ]
result16 = [p.strip(" -").capitalize() for p in products ]
grouped = {}
for p in result16:
    key = p[0].upper()
    grouped.setdefault(key, []).append(p)
    print(grouped)

#------task 21 -----
raw = {"***Alice***", "@Bob@", "  Carol  "}
result17 = {s.strip("*@ ").capitalize() for s in raw}
print(result17)

#------task 22-----------
data1 = {"fruits": ["  apple", "banana  "], "veggies" : ["carrot  ", "  pea"]}
result18 = {k: [v.strip().title() for v in data1] for k, vals in data1.items()}
print(result18)

#-----task 23------
def custon_title(s):
    return ' '.join([w.capitalize() for w in s.split()])
print(custon_title("hello world"))

#------task 24-------
email2 = ["  ALICE@Example.com", "bob@EXAMPLE.COM  "]
result25 = [e.strip().split("@")[0].capitalize() + "@" + e.strip().split("@")[1].lower() for e in email2]
print(result25)

#-------task 25---------
text3 = "123hello world!!!"
result26 = text3.lstrip("123").rstrip("!").title()
print(result26)

#--------task 26

names = ["  alice ", "BOB", " charlie"]
for i in range(len(names)):
    names[i] = names[i].strip().title()
    print(names)
#------task 27----------

sentence = ["  hello world  ", "Hello python "]
words = set()
for s in sentence:
    words.update(s.strip().capitalize().split())
    print(words)

#------task 28---------

data2 = {"msg1": "  hello world  ", "msg2" : "python is fun"}
result29 = {k: v.strip().capitalize() for k, v in data2.items()}
print(result29)

#------task 29---------

text3 = "_-example-_"
cleaned3 = text3.strip("-_")
print(cleaned3)

#--------task 30---------
codes = [" code1 ", "CODE2", " code3"]
cleaned1 = sorted([c.strip().title() for c in codes])
print(cleaned1)