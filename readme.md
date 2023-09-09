Create a folder

example BCload

cd BCLoad

 

 

 

Install python3

 

sudo apt update && upgrade

 

NOTE: USE

apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

Note: you can use

source venv/bin/de-activate

 

 

Go to https://locust.io

 

or install locust

pip install locust

NOTE: it wil install locust in the local module

To verify if locust is installedd type

locust -h

enter
CREATE a new file
Go to the Project root
Go to New file
Right click
Select python file
name your file
app
NOTE: a new app.py is created
Next,

Import all the development packages and class

example: from locust import User, task
> hit enter
class MyFirstTest(User):

> hit enter

Go to terminal

locust -f app.py
>hit enter

 

 

NEXT configure the HTTP User Class

will use

https://reqres.in/

to the the call test

wll use some of the methods for the test.

Create a ne python file example regres.py

NOTE SAME way app was created.

