# REST_web_app
A web application that allows to create, store and list messages.

This README explains two things: HOW TO RUN the application and WHAT IS INSIDE this folder.
------------------------------------------------------------
HOW TO RUN:
1. Move to the folder:
cd  .../REST_web_application

2. Install virtualenv:
py -m pip install virtualenv

3. Create the virtual environment:
py -m venv test_Virt_Env

4. Activate the virtual environment:
source test_Virt_Env/Scripts/activate

5. Install the packages:
py -m pip install -r requirements.txt

6. Run the main file:
py main.app
(browser will open automatically)
... crtl+C to quit

7. Deactivate the virtual environment:
deactivate

------------------------------------------------------------
HOW TO RUN (other times):

1. enter your working folder:
cd C/../REST_web_application

2. Activate the virtual environment:
source test_Virt_Env/Scripts/activate

3. Run the main file:
py main.app
(browser will open automatically)
... crtl+C to quit

4. Deactivate the virtual environment:
deactivate

------------------------------------------------------------
WHAT IS INSIDE:
The main files(not automatically generated):

- static: folder, it contains:
-- style.css: a simple style file, its used has been commented

- templates: folder, it contains:
-- _formhelpers.html: to help create forms
-- index.html: main page
-- new_message.html: page where to add a new message
-- show_messages.html: page where to show the basic version of the messages (which does not provide interactions)
-- show_messages_pro.htmo: page where to show the advanced version of the messages (which does provide interactions)

- README.md: this file.
- requirements.txt: contains the requirements for the virtual environment.

- app.py: basic starting python file.
- forms.py: contains form classes used in the main file.
- main.py: contains the heath of the code.
- table.py: contains table classes used in the main file.

- list_messages.json: the .json file where one can download all messages.
- list_messages.xml: the .xml file where one can download all messages.









