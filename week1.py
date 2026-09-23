# DPLMS Student Registration System


print("Welcome to DPLMS Student Registration System\n")

# 2. Create a list containing these courses
courses = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]

# 3. Use a for loop to display all available courses
for course in courses:
    print(course)
# 4. Ask the user to enter Student Name, Email, Age, and Selected Course.
name = input("Enter Student Name: ")
email = input("Enter Email: ")
age = input("Enter Age: ")
selected_course = input("Enter Selected Course (name exactly as listed or number): ")

# 5. Store the entered information inside a Python dictionary.
student = {
        "Name": name,
        "Email": email,
        "Age": age,
        "Selected Course": selected_course
    }

    # 6. Use an if...else statement to check whether the selected course exists in the course list.
if selected_course in courses:
        # 7. If the course exists, display registration success
    print("\nRegistration Successful!")
else:
        # otherwise display course not available
    print("\nCourse Not Available.")

    # 8. Print the student's registration details in a clean, formatted output.
    print("\n--- Student Registration Details ---")
    print(f"Name           : {student['Name']}")
    print(f"Email          : {student['Email']}")
    print(f"Age            : {student['Age']}")
    print(f"Selected Course: {student['Selected Course']}")
    print("------------------------------------")

#week2
# inspect_json.py
import pandas as pd

# --- User configuration ---
json_filename = "data.json"   # change to your filename/path
orient = None                 # set if JSON uses a specific orient (e.g., 'records', 'index'); None lets pandas infer
lines = False                 # set True if file is in JSON lines (one JSON object per line)
# --------------------------


    # 1. Import pandas (done above)
    # 2. Read the JSON file
    if lines:
        df = pd.read_json(json_filename, orient=orient, lines=True)
    else:
        df = pd.read_json(json_filename, orient=orient)

    # 3. Display first 5 rows
    print("First 5 rows (head):")
    print(df.head(5))
    print("\n" + "-"*60 + "\n")

    # 4. Display last 3 rows
    print("Last 3 rows (tail):")
    print(df.tail(3))
    print("\n" + "-"*60 + "\n")

    # 5. Find the shape of dataset
    print("Shape (rows, columns):", df.shape)
    print("\n" + "-"*60 + "\n")

    # 6. Display column names
    print("Column names:")
    print(list(df.columns))
    print("\n" + "-"*60 + "\n")

    # 7. Display data types
    print("Data types:")
    print(df.dtypes)
    print("\n" + "-"*60 + "\n")

    # 8. Show complete information using info()
    print("Complete info:")
    # Use a buffer capture to show info() output cleanly
    df.info(verbose=True, null_counts=True)
    print("\n" + "-"*60 + "\n")

    # 9. Generate statistical summary using describe()
    # For numeric columns
    print("Statistical summary (numeric):")
    print(df.describe(include=[pd.np.number]).T)  # .T for easier reading
    print("\n" + "-"*60 + "\n")

    # Include summary for object (string) and categorical columns as well
    print("Statistical summary (object / categorical):")
    print(df.describe(include=['object', 'category']).T)
    print("\n" + "-"*60 + "\n")

