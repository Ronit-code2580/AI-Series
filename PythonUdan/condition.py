email = "hello.gmail"
password = "nepal123"

logged_in = False

if not logged_in:
    print("User is not logged in.")
else:
    print("User is logged in.")

print("manish")
print("anish")
print("nish")

for i in range(5):
    print(i)

for j in range(5,10):
    print(j)

for k in range(2,11,2):
    print(k)

for l in range(10,0,-1):    
    print(l)

counrties = ["Nepal", "India", "China", "USA", "UK"]

for country in counrties:
    print(country) 

prediction_score = [77, 88, 99, 100, 90] 

for score in prediction_score:
   if score > 80:
       print(score,"good score")
else:
       print(score,"bad score")

email_lists = [
    "Bhatbheteni ma discount",
    "Yeti arilies free tickes",
    "What is project update"
    "Congratulations you won a lottery"
]

for email in email_lists:
    if "congrats" in email or "Congratulations" in email or "discount" in email or "free" in email:
        print("This is a spam email", email)
    else:
        print("This is a valid email", email)
    
        
    