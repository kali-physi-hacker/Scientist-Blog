# Kali Scientist Blog

>This is a simple blog project written in Django (A python web application development
> framework)
>
>This Blog was written with functionality test in mind. It was written to 
>demonstrate the CRUD functionality of web applications. Kali Scientist Blog
>is a simple blog that contains the simple features every blog should have.
>This project could be the starting point for beginners who want to level up their skills
>in **Django Web Application Development**

### Project Level Structure
>Included in this project are:
> ##### Apps (2)
>* posts
>* users
 
##### Templates
.
>* index.html
>* about.html
>* contact.html
>* base.html

posts
>1. list.html 
>2. edit_post.html
>3. detail_post.html
>4. new_post.html

registration
>* login.html
>* signup.html
>
>
### App Level Structure
#### posts 
default files (model, view, admin, form, urls, apps, etc)>

### Installation
>```bash
>(root)$ mkdir blog  ### Create A Folder For Your Project
>(root)$ git clone https://github.com/kali-physi-hacker/Scientist-Blog.git ### Obtain a copy of the project into your local drive
>(root)$ cd Scientist-Blog  ### Change into the projects directory
>(root)$ pip install -r requirements.txt  ### Install the dependencies
>(root)$ python manage.py migrate  ### Run the migrations (Create Tables in your db)
>(root)$ python manage.py runserver  ### Start Your Local Server (Access using localhost:8000 in your browser)
>```