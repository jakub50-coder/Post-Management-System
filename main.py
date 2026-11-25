#This program is a Post Management System that allows you to choose between three options, to get all the information from the API, to get a specific id from the API, and to create from the API.
#It also contains three methods, get_all_posts, get_post_by_id, and create_post

import requests
#This method gets the Post ID and Title of all the data in the url
def get_all_posts():
    try:
        request = requests.get("https://jsonplaceholder.typicode.com/posts")
        request.raise_for_status()
        data = request.json()
        for post in data:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print("----------------------------")
    except requests.exceptions.RequestException as error:
        print(f"An error has occured: {error}")
#This method gets the specific information from on json based on the Id
def get_post_by_id(post_id):
    try:
        request = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        request.raise_for_status()
        data = request.json()
        print(f"Post ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        print(f"User ID: {data['userId']}")
    except requests.exceptions.RequestException as error:
        print(f"An error has occured: {error}")
#This method gets creates a post by adding the title, body, and user_id
def create_post(title, body, user_id):
    try:
        new_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        request = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_data)
        request.raise_for_status()
        data = request.json()
        print(f"Post ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        print(f"User ID: {data['userId']}")
    except requests.exceptions.RequestException as error:
        print(f"An error has occured: {error}")
#The main menu that gives you the option by choose between Viewing all the posts, view a specfic post,
#creating a new post, and exiting
while True:
    try:
        print("Welcome to the Post Management Application\n")
        print("Enter a choice that you want to enter: \n")
        print("Choice 1: View all the posts: \n")
        print("Choice 2: View a specific post: \n")
        print("Choice 3: Create a new post: \n")
        print("Choice 4: Exit \n")
        answer = int(input("Enter a choice: "))
        #Get all posts 
        if(answer == 1):
            get_all_posts()
        #Get a specific id
        elif(answer == 2):
            try:
                id = int(input("Enter the ID of the post that you want to see: "))
                get_post_by_id(id)
            except ValueError:
                print("This is not a valid id number: \n")
        #Create a new post                
        elif(answer == 3):
            while True:
                title = input("Enter the title of the post: \n").strip()
                if title:
                    break
                print("Field can't be empty \n")
            while True:
                body = input("Enter the body of the post \n").strip()
                if body:
                    break
                print("Field can't be empty \n")
            while True:
                try:
                    user_id = int(input("Enter the user id: \n"))
                    break
                except ValueError:
                    print("Enter your id, an integer value")
            create_post(title, body, user_id)
        #Exit the program
        elif(answer == 4):
            print("Goodbye, see you soon!")
            break
        else:
            print("That is an invalid option. choose between option 1 - 4")
    except ValueError:
        print("This is not a valid choice")

    
