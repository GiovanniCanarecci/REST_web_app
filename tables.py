from flask_table import Table, Col, LinkCol

class Table_Messages_Basic(Table):
    title = Col('Title')
    content = Col('Content')
    sender = Col('Sender')

class Table_Messages(Table):
    title = Col('Title')
    content = Col('Content')
    sender = Col('Sender')
    url = Col('URL')



