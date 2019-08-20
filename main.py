# main.py

from flask import flash, render_template, request, redirect, Response
from app import app
from forms import First_Action_Form, Messages_Form, Basic_Form, Advanced_Form
from tables import Table_Messages, Table_Messages_Basic
import json
import xml.etree.ElementTree as ET
import webbrowser

#to open the browser
webbrowser.open_new('http://localhost') 

#working template message
#list_messages=[{'title': 'Issue', 'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a gall...', 'sender': 'Giovanni', 'url': 'http://hdgdhelsinki.fi'}]
list_messages=[]

@app.route("/", methods=['GET', 'POST'])
def index():
    #choose which action to take: write or see
    result = First_Action_Form(request.form)
    if request.method == 'POST':
        if result.data['selection'] == 'Write a New Message':
            new_message()
        elif result.data['selection'] == "See Saved Messages":
            show_messages()
    return render_template("index.html", form=result)

@app.route('/show_messages', methods=['GET', 'POST'])
def show_messages():
    if list_messages == []:
        #if to check if the list is empty
        flash('No messages yet!')
        return redirect('/')
    else:  
        #display messages basic
        #choose which action to take: advanced or back
        result = Basic_Form(request.form)
        if request.method == 'POST':
            if result.data['selection'] == "Show advance data and options":
                show_messages_pro()
            elif result.data['selection'] == "Back to mainpage":
                index()
        table = Table_Messages_Basic(list_messages)
        table.border = True
        return render_template('show_messages.html', table=table)

@app.route('/show_messages_pro', methods=['GET', 'POST'])
def show_messages_pro():
    #display messages pro
    result = Advanced_Form(request.form)
    if request.method == 'POST':
        #choose which action to take: basics or back
        if result.data['selection'] == "Show basic data":
            show_messages()
        elif result.data['selection'] == "Back to mainpage":
            index()
    table = Table_Messages(list_messages)
    table.border = True
    return render_template('show_messages_pro.html', table=table)

@app.route("/download_json")
def download_json():
    #write all messages in a .json file
    with open('list_message.json', 'w') as json_file:  
        json.dump(list_messages, json_file)
    table = Table_Messages(list_messages)
    table.border = True
    return render_template('show_messages_pro.html', table=table)

@app.route("/download_xml")
def download_xml():
    #write all messages in a .xml file
    def create_xml():
        usrconfig = ET.Element("usrconfig")
        usrconfig = ET.SubElement(usrconfig,"usrconfig")
        for item in range(len(list_messages)):
                usr = ET.SubElement(usrconfig,"usr")
                usr.text = str(list_messages[item])
        tree = ET.ElementTree(usrconfig)
        tree.write("list_messages.xml",encoding='utf-8', xml_declaration=True)
    create_xml()
    table = Table_Messages(list_messages)
    table.border = True
    return render_template('show_messages_pro.html', table=table)

@app.route('/new_message', methods=['GET', 'POST'])
def new_message():
    #Add a new message
    new_message = Messages_Form(request.form)
    if request.method == 'POST' and new_message.validate():
        # save the message
        #Every message is a dict into the following list
        list_messages.append(new_message.data)
        flash('Message created successfully!')
        return redirect('/')
    return render_template('new_message.html', form=new_message)

##########
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True, host="0.0.0.0", port=80)
##########