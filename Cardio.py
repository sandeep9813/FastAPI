import streamlit as st
import requests

API_URL =  'https://fastapi-1-raqk.onrender.com/cardio-predict' 

st.header('Cardiovascular Disease Prediction system')
st.subheader('using Logistic regression')

# age = st.text_input(
#     'age',
#     placeholder = 'enter age of patient'
# )
#    age: int
#     height: int
#     weight: float
#     ap_hi: int
#     ap_lo: int
#     cholesterol: int
#     gluc: int
#     smoke: int
#     alco: int
#     active: int
age = st.sidebar.slider(
    'age',
    max_value = 90,
    min_value = 20,
    step = 1,
    value =30
)

gender = st.sidebar.radio(
    'Gender[1-female,2-male]',
    (1,2)
)

weight = st.sidebar.slider(
     'weight',
    max_value = 200,
    min_value = 20,
    step = 1,
    value =30
)

height = st.sidebar.slider(
    "height",
    max_value = 200,
    min_value = 100,
    step = 1,
    value = 40
)

ap_hi = st.sidebar.slider(
    'systolic pressure',
    max_value = 210,
    min_value = 120,
    step  = 1,
    value = 30
)
ap_lo = st.sidebar.slider(
    'Di_systolic pressure',
    max_value = 180,
    min_value = 50,
    step  = 1,
    value = 70
)

cholesterol_options = {1:'healthy',2:'mild',3:'unhealthy'}
cholesterol = st.sidebar.radio(
    'Cholesterol[1-healthy,2-mid,3-high]',
     options = list(cholesterol_options.keys()),
     format_func = lambda x:cholesterol_options.get(x)
)


gluc_options = {1 : 'healthy',2:'mid',3:'high glucose'}
gluc= st.sidebar.radio(
    'Glucose[1-healthy,2-mid,3-healthy]',
    options  = list(gluc_options.keys()),
    format_func = lambda x: gluc_options.get(x)
)
smoke_options = {0:'doesnot smoke',1:'smoke'}
smoke = st.sidebar.radio(
    'smoke[0-no smoke,1-smoke]',
    options = list(smoke_options.keys()),
    format_func = lambda x: smoke_options.get(x)
)

alco_options = {0:'doesnot drink', 1:'drink'}
alco = st.sidebar.radio(
    'alco[0-doesnot drink ,1-drink]',
    options = list(alco_options.keys()),
    format_func = lambda x:alco_options.get(x)
)
active_options = {0:'does PA',1:'doesnt do PA'}
active = st.sidebar.radio(
    'active[0-PA,1-NPA]',
    options = list(active_options.keys()),
    format_func = lambda x:active_options.get(x)
)


if st.button("Predict Cardio Disease"):
    payload = {
        "age": age,
        "height": height,
        "weight": weight,
        "ap_hi": ap_hi,
        "ap_lo": ap_lo,
        "cholesterol": cholesterol,   # Make sure this matches your API field name
        "gluc": gluc,
        "smoke": smoke,
        "alco": alco,
        "active": active
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            if result["prediction_status"] == 0:
                st.write("No cardiovascular disease found.")
                st.success("Patient is likely to be healthy.")
            else:
                st.write("Cardiovascular disease found.")
                st.error("Patient is likely to be unhealthy.")
        else:
            st.error(f"API Error: {response.status_code}")

    except requests.exceptions.RequestException:
        st.error("API URL not found or server is not running.")