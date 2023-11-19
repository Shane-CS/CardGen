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
        newCard['ADRh']='ADR'+';TYPE=HOME:'+data['address_home']
    if data['address_work'] != '':
        newCard['ADRw']='ADR'+';TYPE=WORK:'+data['address_work']
    if data['address_other'] != '':
        newCard['ADRo']='ADR'+';TYPE=OTHER:'+data['address_other']
        
    # vCard Required Fields
    newCard['BEGIN']='BEGIN'+':'+'VCARD' #Begin
    newCard['VERSION']='VERSION'+':'+'3.0' #Version
    
    # Birthday Section
    if data['bday'] != '':
        newCard['BDAY']='BDAY'+':'+(data['bday'].split('T'))[0] #Birthday
    
    # Email Section
    if data['email_personal'] != '':
        newCard['EMAILp']='EMAIL'+';TYPE=personal:'+data['email_personal']
    if data['email_work'] != '':
        newCard['EMAILw']='EMAIL'+';TYPE=work:'+data['email_work']
    if data['email_other'] != '':
        newCard['EMAILo']='EMAIL'+';TYPE=other:'+data['email_other']

    # vCard Required Fields
    newCard['END']='END'+':'+'VCARD' #End
    
    newCard['FN']='FN'+':'+data['full_name'] #Full Name
    newCard['N']='N'+':'+data['name'] #Name
    
    # Note Section
    if data['notes'] != '':
        newCard['NOTE']='NOTE'+':'+data['notes'] #Note
        
    # Organization Section
    if data['org'] != '':
        newCard['ORG']='ORG'+':'+data['org'] #Organization
        
    # Photo Section
    if data['photo'] != '':
        newCard['PHOTO']='PHOTO'+';'+data['photo'] #Photo

    # Role Section
    if data['role'] != '':
        newCard['ROLE']='ROLE'+':'+data['role']
        
    # For telephone we will offer Mobile, Home, Work, and Other
    if data['tel_mobile'] != '':
        newCard['TELm']='TEL'+';type=CELL;type=VOICE:'+data['tel_mobile']
    if data['tel_home'] != '':
        newCard['TELh']='TEL'+';type=HOME;type=VOICE:'+data['tel_home']
    if data['tel_work'] != '':
        newCard['TELw']='TEL'+';type=WORK;type=VOICE:'+data['tel_work']

    # Title Section
    if data['title'] != '':
        newCard['TITLE']='TITLE'+':'+data['title']
        
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
    
    vcf = ''
    vcf += newCard['BEGIN'] + '\n'
    vcf += newCard['VERSION'] + '\n'
    vcf += newCard['N'] + '\n'
    vcf += newCard['FN'] + '\n'
    if 'ORG' in newCard:
        vcf += newCard['ORG'] + '\n'
    if 'TITLE' in newCard:
        vcf += newCard['TITLE'] + '\n'
    if 'EMAILp' in newCard:
        vcf += newCard['EMAILp'] + '\n'
    if 'EMAILw' in newCard:
        vcf += newCard['EMAILw'] + '\n'
    if 'EMAILo' in newCard:
        vcf += newCard['EMAILo'] + '\n'
    if 'TELm' in newCard:
        vcf += newCard['TELm'] + '\n'
    if 'TELh' in newCard:
        vcf += newCard['TELh'] + '\n'
    if 'TELw' in newCard:
        vcf += newCard['TELw'] + '\n'
    if 'ADRh' in newCard:
        vcf += newCard['ADRh'] + '\n'
    if 'ADRw' in newCard:
        vcf += newCard['ADRw'] + '\n'
    if 'ADRo' in newCard:
        vcf += newCard['ADRo'] + '\n'
    if 'BDAY' in newCard:
        vcf += newCard['BDAY'] + '\n'
    # if 'PHOTO' in newCard:
    #     vcf += newCard['PHOTO'] + '\n'
    if 'ROLE' in newCard:
        vcf += newCard['ROLE'] + '\n'
    if 'NOTE' in newCard:
        vcf += newCard['NOTE'] + '\n'
    vcf += newCard['END'] + '\n'
    print(vcf)
    with open('card.vcf', 'w') as f:
        f.write(vcf)
    f = open('card.vcf', 'r')
    return make_response(jsonify(f.read()))
    return jsonify(newCard)