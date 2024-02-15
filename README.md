This Django project provides basic CRUD (Create, Read, Update, Delete) operations using HTML, CSS, Bootstrap for styling, and SQLite for database storage. 
Additionally, it includes a messaging feature for communication between users, with robust error handling and form validation.

Features:-
1.CRUD Operations: Allows users to create, read, update, and delete student records.
2. Messaging Feature: Enables users to send messages to each other within the system.
3. Error Handling: Provides comprehensive error handling for various scenarios to ensure smooth operation.
4. Form Validation: Implements form validation to ensure data integrity and accuracy.
5. Student Model: Includes a custom student model to manage student information efficiently.
6. Custom Model Form: Utilizes custom model forms for handling user input and data validation.

Technologies Used
1. Django: A high-level Python web framework for rapid development.
2. HTML: Used for structuring the web pages.
3. CSS: Used for styling the HTML content.
4. Bootstrap: Used for enhancing the design and layout of the application.
5. SQLite: A lightweight, serverless, relational database management system used for data storage.

Installation:-
create a python virtual enviroment folder
follow the step
1.git clone <repo_url>
2.pip install -r requirements.txt
3.python manage.py migrate
4.python manage.py runserver
5. copy http://localhost:8000/ paste in browser

Usage
Upon accessing the application, you'll see the list of existing student records.You can add new student records by clicking on the "Add Student" button and filling out the required information in the form.
Existing records can be edited or deleted by clicking on the respective buttons next to each record.
