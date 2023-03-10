import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#from st_aggrid import AgGrid

import plotly.express as px

from streamlit_option_menu import option_menu

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

#from germansentiment import SentimentModel

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time

col1,col2= st.columns(2)

with col1:
   #st.header("A cat")
   st.image("https://storymachine.mocoapp.com/objects/accounts/a201d12e-6005-447a-b7d4-a647e88e2a4a/logo/b562c681943219ea.png", width=200)
   
with col2:
   
   st.header("Data Team Dashboard")

#st.sidebar.success("Choose Category")



# # 2. horizontal menu
# selected2 = option_menu(None, ["CEOs Outreach", "Individual CEO Analysis", "Sentiment Analysis", 'Keyword Monitor'], 
#     icons=['graph-up-arrow', 'bar-chart', "emoji-smile", 'search'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")

# url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"




# if selected2 == 'Individual CEO Analysis':
#     st.title("you are dumb")
    
    #st.write("check out this [link](%s)" % url)
    #st.markdown("[![Foo](https://www.designtagebuch.de/wp-content/uploads/mediathek//2019/10/rwe-logo-2019.jpg)](https://loyidandrews-linkedinmonitoring2-linkedin-monitoring-app-cb4u9m.streamlit.app/)")
    

#st.markdown("check out this [link](%s)" % url)

# st.image(
#     "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
#     width=100,
# )
st.header('')
st.title('WELCOME to LinkedIn Monitoring Dashboard')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

st.header('')
st.header('Choose your Project to start Monitoring')
st.header('')

#url_rwe= 'https://storymachinedata-linkedinmonitor-rwe-linkedin-monitor-vavdv8.streamlit.app/'

col1, col2, col3, col4 = st.columns(4)

with col1:
   #st.header("[RWE](%s)" % url_rwe)
   st.header("RWE")
   st.markdown("[![Foo](data:image/jpeg;base64,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)](https://storymachinedata-linkedinmonitor-rwe-andereceos-mb4bf4.streamlit.app/)")

with col2:
   st.header("DOBNER")
   st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C560BAQFBl5k-bIrCvg/company-logo_200_200/0/1550337518830?e=1678320000&v=beta&t=_wF6uNGemXDwDdwlATUmDDPDMaWX7E3Ilykq_bHWtz4)](https://storymachinedata-linkedinmonito-linkedin-keyword-monitor-8iidyr.streamlit.app/)")

with col3:
   st.header("Lutzerath")
   st.markdown("[![Foo](https://www.autoservice-ewen.de/images/Logos/Ortsschild-Lutzerath-250.gif)](https://storymachinedata-lutzerath-lutzerath-mentions-i0cjd6.streamlit.app/)")



with col4:
   st.header("Palantir")
   st.markdown("[![Foo](https://ih1.redbubble.net/image.2259243696.4263/st,small,207x207-pad,200x200,f8f8f8.jpg)](https://storymachinedata-palantir-dash-main-i14y5q.streamlit.app/)")
