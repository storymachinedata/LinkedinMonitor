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

col7,col8,col9  = st.columns(3)


with col1:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>RWE</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-linkedinmonitor-rwe-andereceos-mb4bf4.streamlit.app/' target='_blank'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxamGiLbLjQKWmaSTz38KxQkCroD3FFj-Lg2WxNgYf&s'  width='330'/></a></div>", unsafe_allow_html=True)


with col2:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>DOBNER</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-linkedinmonito-linkedin-keyword-monitor-8iidyr.streamlit.app/' target='_blank'><img src='https://media.licdn.com/dms/image/C560BAQFBl5k-bIrCvg/company-logo_200_200/0/1550337518830?e=1686787200&v=beta&t=W3QSd4a6MzBgPPOctix7KZREWjtdP99rAKCsoaeJZvc'  width='330'/></a></div>", unsafe_allow_html=True)


with col3:

   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>MUTARES</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-mutares-linkedin-mutares-linkedin-posts-gangz0.streamlit.app/' target='_blank'><img src='https://www.4investors.de/bilder480/medienpool/unternehmen/mutares/mutares-schriftzug.jpg'  width='330' height='330'/></a></div>", unsafe_allow_html=True)


with col4:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>PALANTIR</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-palantir-dash-main-i14y5q.streamlit.app/' target='_blank'><img src='https://ih1.redbubble.net/image.2259243696.4263/st,small,207x207-pad,200x200,f8f8f8.jpg'  width='330'/></a></div>", unsafe_allow_html=True)



with col5:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>NIKO WARBANOFF</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-nikowarbanoff-linkedin-keyword-monitor-zzeog9.streamlit.app/' target='_blank'><img src='https://img.swapcard.com/?u=https%3A%2F%2Fcdn-api.swapcard.com%2Fpublic%2Fimages%2Fd2eef7c4b1a14a7d9972d5490b27fa8d.jpeg&q=0.8&m=fit&w=400&h=200'  width='330'/></a></div>", unsafe_allow_html=True)


with col6:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>GOLDBECK</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-goldbeck-linkedin-keyword-monitor-8xqh3w.streamlit.app/' target='_blank'><img src='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/vujochtfl55m7mvsrvdd' width='330'/></a></div>", unsafe_allow_html=True)

    
with col7:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>FOM Real Estate</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://storymachinedata-fom-rea-fom-keyword-monitoring-linkedin-dtdl91.streamlit.app/' target='_blank'><img src='https://www.fomrealestate.de/download_file/view/2/0' width='330'/></a></div>", unsafe_allow_html=True)
    
with col8:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>PJ</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://pjkeywords-n6nsrr9s7w.streamlit.app/' target='_blank'><img src='https://images.creativebase.com/_next/image?url=https%3A%2F%2Fs3.eu-central-1.amazonaws.com%2Fzone.busch.store.image%2F85b7b0cc4d4eb15bf1b505fd6cb4c3fb358c2c7829f730f7b349458d0a85f9a8.jpg&w=3840&q=100' width='330'/></a></div>", unsafe_allow_html=True)
    
with col9:
   st.markdown("<div style='text-align: center; font-weight: bold; font-size: 32px;'>Salzgitter</div>", unsafe_allow_html=True)
   st.markdown("<div style='text-align: center;'><a href='https://salzgitter-nzwlhv7i9gztyqvytknyqf.streamlit.app/' target='_blank'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Salzgitter_AG_Logo.svg/1598px-Salzgitter_AG_Logo.svg.png' width='330'/></a></div>", unsafe_allow_html=True)


