**Prerequisites:**  
Install PostgreSQL https://www.postgresql.org/download/  
Install Django  
`pip install django`  
Install Django Rest Framework  
`pip install djangorestframework`  
Install PostgreSQL database adapter for the Python  
`pip install psycopg2`  

**Database setup:**  
Inside pgAdmin create a database named "restapi".  
Create a user named "challange" with password "pass" and inside properties give it privilage to login.  
Change the owner of the database to the newly created user  

**Run server:**  
In the root folder type prompts:  
`python manage.py makemigrations userapi`  
`python manage.py migrate`  

**Use api:**  
Requests will work on localhost:'portnumber'/api/user/  
***This is the structure of a user profile in JSON:***  
localhost:8000/api/user/1  
```
{
    "id": 1, /auto generated
    "name": "",
    "surname": "",
    "profession": "",
    "interests": "",
    "pros": "",
    "cons": ""
}
```