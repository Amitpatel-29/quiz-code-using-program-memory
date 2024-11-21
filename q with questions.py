# Lists to store registered usernames and passwords
usernames = []
passwords = []

# register new user..


def register():
    print("Register a new account.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    # adding username and password to list
    
    
    usernames.append(username)
    passwords.append(password)
    
    print("Registration successful! You can now log in.")

# Function to log in with existing cusers 

def login():
    print("Log in to your account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if the username exists and if the password matches
    if username in usernames:
        user_index = usernames.index(username)
        if passwords[user_index] == password:
            print("Login successful! Welcome,", username)
            return True  # Successful login
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found. Please register first.")
        return False

# Quiz categories: DSA, DBMS, and Python

# DSA Quiz Questions
dsa_quiz = [
    {"question": "Which of the following is a linear data structure?", "options": ["A) Stack", "B) Tree", "C) Graph"], "correct_answer": "A"},
    {"question": "Which of the following sorting algorithms has the best time complexity in the worst case?", "options": ["A) Bubble Sort", "B) Merge Sort", "C) Selection Sort"], "correct_answer": "B"},
    {"question": "Which data structure uses LIFO (Last In First Out) order?", "options": ["A) Queue", "B) Stack", "C) Linked List"], "correct_answer": "B"},
    {"question": "Which of the following is an example of a non-linear data structure?", "options": ["A) Array", "B) Linked List", "C) Tree"], "correct_answer": "C"},
    {"question": "In a binary search tree (BST), the left child of a node must be ____.","options": ["A) Greater than the node", "B) Less than the node", "C) Equal to the node"], "correct_answer": "B"}
]

# DBMS Quiz Questions
dbms_quiz = [
    {"question": "Which of the following is the primary key of a table used for?", "options": ["A) To uniquely identify each record", "B) To store data in the table", "C) To create a relationship between tables"], "correct_answer": "A"},
    {"question": "What does SQL stand for?", "options": ["A) Structured Query Language", "B) Simple Query Language", "C) Standard Query Language"], "correct_answer": "A"},
    {"question": "In a relational database, a table is also known as a:", "options": ["A) Relation", "B) Query", "C) Attribute"], "correct_answer": "A"},
    {"question": "Which of the following is not a type of JOIN in SQL?", "options": ["A) INNER JOIN", "B) LEFT JOIN", "C) RIGHT JOIN", "D) LINK JOIN"], "correct_answer": "D"},
    {"question": "Which of the following is used to prevent duplication of records in a table?", "options": ["A) FOREIGN KEY", "B) UNIQUE constraint", "C) CHECK constraint"], "correct_answer": "B"}
]

# Python Quiz Questions
python_quiz = [
    {"question": "Which of the following data types is immutable in Python?", "options": ["A) List", "B) Dictionary", "C) Tuple"], "correct_answer": "C"},
    {"question": "What is the output of the following Python code? print(3 * 2 + 1)", "options": ["A) 7", "B) 8", "C) 6"], "correct_answer": "A"},
    {"question": "Which of the following is the correct way to create a function in Python?", "options": ["A) def function_name():", "B) function function_name():", "C) function_name def():"], "correct_answer": "A"},
    {"question": "Which of the following is used to create an empty list in Python?", "options": ["A) []", "B) {}", "C) ()"], "correct_answer": "A"},
    {"question": "Which of the following is the correct syntax to access the first element of a list in Python?", "options": ["A) list[1]", "B) list(1)", "C) list[0]"], "correct_answer": "C"}
]

# Function to take the quiz based on category selection
def take_quiz():
    print("\nChoose a quiz category:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")
    
    ch = input("Enter your choice: ")

    if ch == '1':
        quiz = dsa_quiz
    elif ch == '2':
        quiz = dbms_quiz
    elif ch == '3':
        quiz = python_quiz
    else:
        print("Invalid choice. Exiting the quiz.")
        return
    
    score = 0

    # Loop through the selected quiz questions
    for q in quiz:
        print(q["question"])
        for option in ["options"]:
            print(option)
        answer = input("Your answer: ").upper()  # Convert to uppercase to match options
        
        if answer == q["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['correct_answer']}\n")
    
    # Print the final score
    print(f"You scored {score} out of {len(quiz)}.")
    # out of 5 bcz there are 5 question 
    #{len(quiz)} for length of quiz that is 5



# FRONT PAGE


def main():
    while True:
        print("\nWelcome to the system!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():  # Only proceed if login is successful
                take_quiz()  # Start quiz after successful login
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
    
main()
