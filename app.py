import streamlit as st
from firebase_admin import auth
from googleapiclient.discovery import build
from google.cloud.firestore import Client
from google.oauth2 import service_account
from firebase_admin import firestore, credentials, initialize_app
import pyrebase
from secret import access_secret
import json
from settings import project_id, firebase_database, fx_api_key, firestore_api_key, google_sheets_api_key, schedule_function_key, firebase_auth_api_key


### retrieving secrets from gcp 
firestore_db_api_key = access_secret(firestore_api_key, project_id)
firebase_auth_api_key = access_secret(firebase_auth_api_key, project_id)
google_sheets_api_key = access_secret(google_sheets_api_key, project_id)



def main():
    st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide") #layout can be centered

    ### Testing connection to firebase database
    firestore_db_api_key_dict = json.loads(firestore_db_api_key)
    fbcredentials = service_account.Credentials.from_service_account_info(firestore_db_api_key_dict)
    db = Client(firebase_database, fbcredentials)
    docs = db.collection('fx').where("currency", "==", "JPY").get()[0]
    rate = docs._data['rate'] 
    print(rate)
    st.write(rate)

    ### Testing connection to firebase auth
    firebase_auth_api_key_dict = json.loads(firebase_auth_api_key)
    firebase = pyrebase.initialize_app(firebase_auth_api_key_dict)
    auth = firebase.auth()
    email = "test@gmail.com" 
    password = "123456"
    user = auth.sign_in_with_email_and_password(email, password)
    idtoken = user['idToken']
    userinfo = auth.get_account_info(idtoken)
    print (userinfo)
    st.write(userinfo)

    ### Testing connection to google sheets
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
    st.write(values)


    ### Testing connection to alpha vantage
    alphavantage_api_key = access_secret(fx_api_key, project_id)
    print (alphavantage_api_key)
    st.write(alphavantage_api_key)
    
    cloud_run_apikey = access_secret(schedule_function_key, project_id)
    print (cloud_run_apikey)
    st.write(cloud_run_apikey)


if __name__ == '__main__':
    main()