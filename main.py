import streamlit as st
import pyrebase #pip install pyrebase4
import time
from datetime import datetime
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

firebaseConfig = {
  'apiKey': st.secrets["apikey"],
  'authDomain': "remote-temperature-20726.firebaseapp.com",
  'databaseURL': "https://remote-temperature-20726-default-rtdb.firebaseio.com",
  'projectId': "remote-temperature-20726",
  'storageBucket': "remote-temperature-20726.appspot.com",
  'messagingSenderId': "221631060825",
  'appId': "1:221631060825:web:9c416c5a2b2e7c0b75ca48",
  'measurementId':"G-MWMF1EPKBB"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
users = db.child("DHT").get()
df = pd.DataFrame(users.val()).T
df.index = df.index.astype(int)
main_df = df[df.index > 1600000000]
 #(30968, 2)

last_update = main_df.tail(1).index[0]
# st.header(last_update)
# print(last_update)

dttime = datetime.utcfromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')

#-----------------------------------------------------#

st.header('Hello 🌎! Here is the chart: of your temperature and humidity:')
if st.button('Update'):
    st.header(dttime)
    st.balloons()
    st.line_chart(main_df)




