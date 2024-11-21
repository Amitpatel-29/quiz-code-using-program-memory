login_status = False
login_user = ''
login_name = ''
login_city = ''
login_enroll = ''
login_college = ''
# Function to register new user

def registration():
    global login_name, login_city, login_enroll
    print("Registration: Please enter the following details.")
    
    
    name  = input("Enter your name: ")
    city = input("Enter your city: ")
    enroll = input("Enter your enrollment number: ")
    college = input("Enter your college name: ")
    pwd = input("Enter your password: ")

    #  registration.txt file
    with open('registration.txt', 'a') as file:
        file.write(f"{name},{city},{enroll},{college}, {pwd}\n")
        
    # (enrollment number and password) in a separate file
    
    with open('login_details.txt', 'a') as file:
        file.write(f"{enroll},{pwd}\n")
    
    # Update the global variables with the entered details
    login_name = name
    login_city = city
    login_enroll = enroll
    login_college = college
  
    print("Registration successful! You can now log in.")

# Function to log in an existing user
def login():
    global login_status, login_user, login_name, login_city, login_enroll
    en = input("Enter Enrollment Number: ")
    users = []
    uspw = {}

    # Read the login details from the file
    with open('login_details.txt', 'r') as file:
        log = file.readlines()
        for i in log:
            u, p = i.split(',')
            p = p.replace('\n', '')  # Clean up newline character
            users.append(u)
            uspw[u] = p

    # Check if the entered enrollment number exists
    if en in users:
        pw = input("Enter Password: ")
        # Check if the entered password matches the one stored in the file
        if pw == uspw[en]:
            print(f"Welcome {en}")
            login_status = True
            login_user = en
            # Retrieve the user's details from the registration file
            with open('registration.txt', 'r') as file:
                for i in file.readlines():
                    name, city, enroll, _ = i.split(',')
                    if enroll == en:
                        login_name = name
                        login_city = city
                        login_enroll = enroll
            print("Login successful!")
        else:
            print("Wrong Password")
    else:
        print("User not registered.")
        choice = input("Do you want to register (y/n): ").lower()
        if choice == 'y':
            registration()  # Call registration function
        else:
            exit()

# Function to attempt the quiz
def attemptQuiz():
    global login_status, login_user
    if login_status:
        print(f"Starting quiz for {login_user}...")

        # Define quiz questions for DSA, DBMS, and Python
        dsa_quiz = [
            {"question": "Which of the following is a linear data structure?", "options": ["A) Stack", "B) Tree", "C) Graph"], "correct_answer": "A"},
            {"question": "Which of the following sorting algorithms has the best time complexity in the worst case?", "options": ["A) Bubble Sort", "B) Merge Sort", "C) Selection Sort"], "correct_answer": "B"},
            {"question": "Which data structure uses LIFO (Last In First Out) order?", "options": ["A) Queue", "B) Stack", "C) Linked List"], "correct_answer": "B"},
            {"question": "Which of the following is an example of a non-linear data structure?", "options": ["A) Array", "B) Linked List", "C) Tree"], "correct_answer": "C"},
            {"question": "In a binary search tree (BST), the left child of a node must be ____.","options": ["A) Greater than the node", "B) Less than the node", "C) Equal to the node"], "correct_answer": "B"}
        ]
        
        dbms_quiz = [
            {"question": "Which of the following is the primary key of a table used for?", "options": ["A) To uniquely identify each record", "B) To store data in the table", "C) To create a relationship between tables"], "correct_answer": "A"},
            {"question": "What does SQL stand for?", "options": ["A) Structured Query Language", "B) Simple Query Language", "C) Standard Query Language"], "correct_answer": "A"},
            {"question": "In a relational database, a table is also known as a:", "options": ["A) Relation", "B) Query", "C) Attribute"], "correct_answer": "A"},
            {"question": "Which of the following is not a type of JOIN in SQL?", "options": ["A) INNER JOIN", "B) LEFT JOIN", "C) RIGHT JOIN", "D) LINK JOIN"], "correct_answer": "D"},
            {"question": "Which of the following is used to prevent duplication of records in a table?", "options": ["A) FOREIGN KEY", "B) UNIQUE constraint", "C) CHECK constraint"], "correct_answer": "B"}
        ]
        
        python_quiz = [
            {"question": "Which of the following data types is immutable in Python?", "options": ["A) List", "B) Dictionary", "C) Tuple"], "correct_answer": "C"},
            {"question": "What is the output of the following Python code? print(3 * 2 + 1)", "options": ["A) 7", "B) 8", "C) 6"], "correct_answer": "A"},
            {"question": "Which of the following is the correct way to create a function in Python?", "options": ["A) def function_name():", "B) function function_name():", "C) function_name def():"], "correct_answer": "A"},
            {"question": "Which of the following is used to create an empty list in Python?", "options": ["A) []", "B) {}", "C) ()"], "correct_answer": "A"},
            {"question": "Which of the following is the correct syntax to access the first element of a list in Python?", "options": ["A) list[1]", "B) list(1)", "C) list[0]"], "correct_answer": "C"}
        ]
        
        # Choose quiz category
        print("\nChoose a quiz category:")
        print("1. DSA")
        print("2. DBMS")
        print("3. Python")
        ch = input("Enter your choice (1/2/3): ")

        if ch == '1':
            quiz = dsa_quiz
        elif ch == '2':
            quiz = dbms_quiz
        elif ch == '3':
            quiz = python_quiz
        else:
            print("Invalid choice. Exiting quiz.")
            return

        score = 0

        # Loop through the quiz questions
        for q in quiz:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Your answer: ").upper()  
            
            if answer == q["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {q['correct_answer']}\n")
        
        # Show the quiz score
        print(f"You scored {score} out of {len(quiz)}.")
    else:
        print("You need to log in first.")

# Function to show the result of the quiz (currently a placeholder)
def showResult():
    global login_status, login_user
    if login_status:
        print(f"Displaying quiz result for {login_user}")
        print(score)
        
    else:
        print("You need to log in first.")

# Function to show user profile (currently displays basic details)
def showProfile():
    global login_status, login_user, login_name, login_city, login_enroll, login_college
    if login_status:
        print(f"\nProfile of {login_user}:")
        print(f"Name: {login_name}")
        print(f"City: {login_city}")
        print(f"Enrollment Number: {login_enroll}")
        print(f"college: {login_college}")
        
    else:
        print("You need to log in first.")

# Main menu loop
def main():
    while True:
        print("""
        1. Registration
        2. Login
        3. Attempt Quiz
        4. Show Profile
        5. Show Result
        6. Exit
        """)

        choice = input("Choose an option (1/2/3/4/5/6): ")

        if choice == '1':
            registration()
        elif choice == '2':
            login()
        elif choice == '3':
            attemptQuiz()
        elif choice == '4':
            showProfile()
        elif choice == '5':
            showResult()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
main()
