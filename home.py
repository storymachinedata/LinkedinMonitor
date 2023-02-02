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
   st.image("https://www.storymachine.de/assets2/img/storymachine.png", width=200)
   
with col2:
   
   st.header("Data Team Dashboard")


st.header('')
st.title('WELCOME to LinkedIn Monitoring Dashboard')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)

st.header('')
st.header('Choose your Project to Start Monitoring')
st.header('')

#url_rwe= 'https://storymachinedata-linkedinmonitor-rwe-linkedin-monitor-vavdv8.streamlit.app/'

col1, col2, col3 = st.columns(3)
col4,col5,col6  = st.columns(3)

with col1:
   #st.header("[RWE](%s)" % url_rwe)
   st.header("RWE")
   st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C4D0BAQHcUAokOSCKEg/company-logo_200_200/0/1569830150461?e=1678320000&v=beta&t=wkDnvFshAFE6-aDdqm3xoAjnb32JwfrHhiY1unvjWnQ)](https://storymachinedata-linkedinmonitor-rwe-andereceos-mb4bf4.streamlit.app/)")

with col2:
   st.header("DOBNER")
   st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C560BAQFBl5k-bIrCvg/company-logo_200_200/0/1550337518830?e=1678320000&v=beta&t=_wF6uNGemXDwDdwlATUmDDPDMaWX7E3Ilykq_bHWtz4)](https://storymachinedata-linkedinmonito-linkedin-keyword-monitor-8iidyr.streamlit.app/)")

with col3:
   st.header("Lutzerath")
   st.markdown("[![Foo](https://www.autoservice-ewen.de/images/Logos/Ortsschild-Lutzerath-250.gif)](https://storymachinedata-lutzerath-lutzerath-mentions-i0cjd6.streamlit.app/)")



with col4:
   st.header("Palantir")
   st.markdown("[![Foo](https://ih1.redbubble.net/image.2259243696.4263/st,small,207x207-pad,200x200,f8f8f8.jpg)](https://storymachinedata-palantir-dash-main-i14y5q.streamlit.app/)")


with col5:
   st.header("Niko Warbanoff")
   st.markdown("[![Foo](https://img.swapcard.com/?u=https%3A%2F%2Fcdn-api.swapcard.com%2Fpublic%2Fimages%2Fd2eef7c4b1a14a7d9972d5490b27fa8d.jpeg&q=0.8&m=fit&w=400&h=200)](https://storymachinedata-nikowarbanoff-linkedin-keyword-monitor-xl9e8l.streamlit.app/)")


with col6:
   st.header("Goldbeck")
   st.markdown("[![Foo](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/vujochtfl55m7mvsrvdd)](https://storymachinedata-goldbeck-linkedin-keyword-monitor-8xqh3w.streamlit.app/)")
