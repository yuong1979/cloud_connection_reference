from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.cloud.firestore import Client
from secret import access_secret
import pyrebase
import json

### if running on local the access from local service account needs to be created before you can connect to google cloud

### Go to credentials and create a new service account
### Select the new service account -> keys -> add keys -> download key as json file
### Go to IAM -> add -> paste the address of the new service account into "new principal" and under select a role select "secret manager secret accessor"
### Move the json file into your local drive (change the path below) and run the below command before running python codes to connect to google cloud

# export GOOGLE_APPLICATION_CREDENTIALS="/home/yuong/work/pyproj/Keys/blockmacro_local_access.json"


### To start a new firebase database connection
### Start a new firebase project
### Go to project overview -> Project Settings ->  service Accounts -> select Python under firebase admin sdk -> generate key private key
### Go to google cloud select the project
### Go to security -> Secret manager -> Create secret -> Upload the json file downloaded from firebase
### Change the projectid(secret) / secretname / projectid(firebase)

### Testing connection to firebase database
firestore_db_api_key = access_secret("blockmacro_firebase_db")
firestore_db_api_key_dict = json.loads(firestore_db_api_key)
fbcredentials = service_account.Credentials.from_service_account_info(firestore_db_api_key_dict)
db = Client("python-firestore-52cfc", fbcredentials)
docs = db.collection('fx').where("currency", "==", "JPY").get()[0]
print(docs._data['rate'])

### To start a new firebase auth connection
### Start a new firebase project
### Go to project overview -> Project Settings -> General -> Scroll down and select config copy the config
### Add "databaseURL": "" at the end of config and save as json file (need to make changes to fit json)
### Go to google cloud select the project
### Go to security -> Secret manager -> Create secret -> Upload the json file downloaded from firebase
### Change the projectid(secret) / secretname

### Testing connection to firebase auth
firebase_auth_api_key = access_secret("blockmacro_firebase_auth")
firebase_auth_api_key_dict = json.loads(firebase_auth_api_key)
firebase = pyrebase.initialize_app(firebase_auth_api_key_dict) 
auth = firebase.auth()
email = "test@gmail.com"
password = "123456"
user = auth.sign_in_with_email_and_password(email, password)
idtoken = user['idToken']
userinfo = auth.get_account_info(idtoken)
print (userinfo)


### To start a new google sheets connection
### Go to search for google sheets api on google cloud and enable it / or manage
### Go to credentials and create a new service account
### Select the new service account -> keys -> add keys -> download key as json file
### Go to security -> Secret manager -> Create secret -> Upload the json file downloaded from creating service account
### Go to google sheets that you are connecting with -> Share -> Share the email of the service account
### Change the projectid(secret) / secretname / required_spreadsheet_id - from the url of the spreadsheet itself

### Testing connection to google sheets
google_sheets_api_key = access_secret("blockmacro_googlesheets")
google_sheets_api_key_dict = json.loads(google_sheets_api_key)
gscredentials = service_account.Credentials.from_service_account_info(google_sheets_api_key_dict)
REQUIRED_SPREADSHEET_ID = '1_lobEzbiuP9TE2UZqmqSAwizT8f2oeuZ8mVuUTbBAsA'
service = build('sheets', 'v4', credentials=gscredentials)
sheet = service.spreadsheets()
sheetinfo = "Sheet1"
result = sheet.values().get(spreadsheetId=REQUIRED_SPREADSHEET_ID, 
    range=sheetinfo+"!A2").execute()
values = result.get('values', [])
print (values)


### Go to security -> Secret manager -> Create secret
### Change the secretname
### Testing connection to alpha vantage
alphavantage_api_key = access_secret("blockmacro_alpha_vantage_api")
print (alphavantage_api_key)
 



## Required pkgs
# pip install pyrebase4
# pip install firebase-admin
# pip install google-cloud-secret-manager