import time
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/gen', methods = ['POST'])
@cross_origin()
def gen_contact_card():
    '''
    Notes On Data Structure:
    - Code will start by creating a dictionary with all the keys that are available for a vCard
    - Then if a value is assigned from the react frontend, it will be added to the dictionary
    - If a value is not assigned, it will be left blank
    - For fields that have multiple values (i.e. email, phone, address), we will add to the number of that field we need
    - Then the field will add labels for each value (i.e. email1, email2, email3)
    - Then we will convert to a vCard format
    - Then we will return the vCard to the frontend
    '''
    # If you have any other keys but don't want to include
    # data = {'handle': request.form['handle'], 'tCount': request.form['tCount']}

    # If you only have two keys (handle and tCount)
    data = request.json
    print(data)
    newCardDataTypes=[]
    newCard = {} # Create a new dictionary for the vCard
    
    # Address Section
    # For address we will offer Home, Work, and Other
    if data['address_home'] != '':
        newCard['ADR']=';TYPE=HOME:'
    elif data['address_work'] != '':
        newCard['ADR']=';TYPE=WORK:'
    elif data['address_other'] != '':
        newCard['ADR']=';TYPE=OTHER:'
        
    # vCard Required Fields
    newCard['BEGIN']='VCARD' #Begin
    newCard['VERSION']='3.0' #Version
    
    # Birthday Section
    if data['bday'] != '':
        newCard['BDAY']=':'+data['bday'] #Birthday
    
    # Email Section
    # For email we will offer Personal, Work, and Other
    # numEmails = 0
    # if data['email_personal'] != '-1':
    #     numEmails+=1
    #     newCard['EMAIL']=''
    # if data['email_work'] != '-1':
    #     numEmails+=1
    #     newCard['EMAIL']=''
    # if data['email_other'] != '-1':
    #     numEmails+=1
    #     newCard['EMAIL']=''
    # if numEmails == 1:
    #     if data['email_personal'] != '-1':
    #         newCard['EMAIL']='TYPE=personal:'
    #     elif data['email_work'] != '-1':
    #         newCard['EMAIL']='TYPE=work:'
    #     elif data['email_other'] != '-1':
    #         newCard['EMAIL']='TYPE=other:'
    # elif numEmails > 1:
    if data['email_personal'] != '':
        newCard['EMAIL']=';TYPE=personal:'+data['email_personal']
    if data['email_work'] != '':
        newCard['EMAIL']=';TYPE=work:'+data['email_work']
    if data['email_other'] != '':
        newCard['EMAIL']=';TYPE=other:'+data['email_other']

    # vCard Required Fields
    newCard['END']='VCARD' #End
    
    newCard['FN']=':'+data['full_name'] #Full Name
    newCard['N']=':'+data['name'] #Name
    
    # Note Section
    if data['notes'] != '':
        newCard['NOTE']='' #Note
        
    # Organization Section
    if data['org'] != '':
        newCard['ORG']='' #Organization
        
    # Photo Section
    if data['photo'] != '':
        newCard['PHOTO']=''

    # Role Section
    if data['role'] != '':
        newCard['ROLE']=''
        
    # For telephone we will offer Mobile, Home, Work, and Other
    if data['tel_mobile'] != '':
        newCard['TEL']=';type=CELL;type=VOICE;'+data['tel_mobile']
    if data['tel_home'] != '':
        newCard['TEL']=';type=HOME;type=VOICE;'+data['tel_home']
    if data['tel_work'] != '':
        newCard['TEL']=';type=WORK;type=VOICE;'+data['tel_work']

    # Title Section
    if data['title'] != '':
        newCard['TITLE']='' #Org Title
        
    # Template Section
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    # newCard['']=''
    print(newCard)

    return jsonify(data)