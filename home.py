import time
import webbrowser
import streamlit as st
import streamlit.components.v1 as components
from streamlit_image_select import image_select



st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    st.image("https://www.storymachine.de/assets2/img/storymachine.png", width=200)

with col2:
    st.header("Data Team Dashboard")


st.title("WELCOME to LinkedIn Monitoring Dashboard")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

st.header("Choose your Project to Start Monitoring")

image_list = [
    "images/white-rwe.jpeg",
    "https://media.licdn.com/dms/image/C560BAQFBl5k-bIrCvg/company-logo_200_200/0/1550337518830?e=1686787200&v=beta&t=W3QSd4a6MzBgPPOctix7KZREWjtdP99rAKCsoaeJZvc",
    "images/white-mutares.png",
    "images/white-palantir.jpeg",
    "images/white-db.png",
    "images/white-goldbeck.jpeg",
    "images/fom.jpeg",
    "https://images.creativebase.com/_next/image?url=https%3A%2F%2Fs3.eu-central-1.amazonaws.com%2Fzone.busch.store.image%2F85b7b0cc4d4eb15bf1b505fd6cb4c3fb358c2c7829f730f7b349458d0a85f9a8.jpg&w=3840&q=100",
    "images/white-Salzgitter_AG_Logo.svg.png",
]
#

captions_list = [
    "RWE",
    "DOBNER",
    "MUTARES",
    "PALANTIR",
    "NIKO WARBANOFF",
    "GOLDBECK",
    "FOM REAL ESTATE",
    "PJ",
    "SALZGITTER",
]

app_dict = {
    0: "https://storymachinedata-linkedinmonitor-rwe-andereceos-mb4bf4.streamlit.app/",
    1: "https://storymachinedata-linkedinmonito-linkedin-keyword-monitor-8iidyr.streamlit.app/",
    2: "https://storymachinedata-mutares-linkedin-mutares-linkedin-posts-gangz0.streamlit.app/",
    3: "https://storymachinedata-palantir-dash-main-i14y5q.streamlit.app/",
    4: "https://storymachinedata-nikowarbanoff-linkedin-keyword-monitor-zzeog9.streamlit.app/",
    5: "https://storymachinedata-goldbeck-linkedin-keyword-monitor-8xqh3w.streamlit.app/",
    6: "https://storymachinedata-fom-rea-fom-keyword-monitoring-linkedin-dtdl91.streamlit.app/",
    7: "https://pjkeywords-n6nsrr9s7w.streamlit.app/",
    8: "https://salzgitter-nzwlhv7i9gztyqvytknyqf.streamlit.app/",
}

with st.columns(3)[1]:
    col_1_key = image_select(
        "",
        images=image_list[:3],
        captions=captions_list[:3],
        return_value="index",
        index=-1, 
    )

    if col_1_key != -1:
        webbrowser.open_new_tab(app_dict[col_1_key])

    col_2_key = image_select(
        "",
        images=image_list[3:6],
        captions=captions_list[3:6],
        return_value="index",
        index=-1
        
    )

    if col_2_key != -1:
        webbrowser.open_new_tab(app_dict[col_2_key])

    col_3_key = image_select(
        "",
        images=image_list[6:9],
        captions=captions_list[6:9],
        return_value="index",
        index=-1
    )

    if col_3_key != -1:
        webbrowser.open_new_tab(app_dict[col_3_key])
