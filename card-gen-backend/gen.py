import time
from flask import Flask

app = Flask(__name__)

@app.route('/gen', methods = ['POST'])
def gen_contact_card():
    # If you have any other keys but don't want to include
    data = {'handle': request.form['handle'], 'tCount': request.form['tCount']}

    # If you only have two keys (handle and tCount)
    data = request.form
    newCardDataTypes=[]
    newCard = {}
    # For address we will offer Home, Work, and Other
    newCard['ADR']='' #Address
    newCard['BEGIN']='VCARD' #Begin
    newCard['VERSION']='3.0' #Version
    newCard['BDAY']='' #Birthday
    
    # Email Section
    # For email we will offer Personal, Work, and Other
    numEmails = 0
    if data['email_personal'] != '-1':
        numEmails+=1
        newCard['EMAIL']=''
    if data['email_work'] != '-1':
        numEmails+=1
        newCard['EMAIL']=''
    if data['email_other'] != '-1':
        numEmails+=1
        newCard['EMAIL']=''

    newCard['EMAIL']='' #Email
    newCard['END']='VCARD' #End
    newCard['FN']='' #Full Name
    newCard['N']='' #Name
    newCard['NOTE']='' #Note
    newCard['ORG']='' #Organization
    newCard['PHOTO']='' #Photo
    newCard['ROLE']='' #Org Role
    # For telephone we will offer Mobile, Home, Work, and Other
    newCard['TEL']='' #Telephone
    newCard['TITLE']='' #Org Title
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    newCard['']=''
    

    return jsonify(data)