import streamlit as st
import pandas as pd
import pickle
from PIL import Image
image1 = Image.open('air_india.jpg')
image2 = Image.open('air_asia.jpg')
image3 = Image.open('go_first.jpg')
image4 = Image.open('indigo.jpg')
image5 = Image.open('spice_jet.jpg')
image6 = Image.open('vistara.jpg')

st.title("Prediksi Harga Tiket Pesawat")


# import model
model = pickle.load(open("price_pred.pkl", "rb"))


# user input
air = st.sidebar.selectbox(label='Airline', options=['AirAsia', 'Air_India','GO_FIRST','Indigo','SpiceJet','Vistara'])
if air == 'Air_India':
    st.image(image1, caption='Air India')
elif air == 'AirAsia':
    st.image(image2, caption='Air Asia')
elif air == 'GO_FIRST':
    st.image(image3, caption='Go First')
elif air == 'Indigo':
    st.image(image4, caption='Indigo')
elif air == 'SpiceJet':
    st.image(image5, caption='Spice Jet')
else:
    st.image(image6, caption='Vistara')

sou = st.sidebar.selectbox(label='Source City', options=['Bangalore', 'Chennai','Delhi','Hyderabad','Kolkata','Mumbai'])
dep = st.sidebar.selectbox(label='Departure Time', options=['Early_Morning','Morning','Afternoon','Evening','Night','Late_Night'])
sto = st.sidebar.selectbox(label='Stops', options=['zero','one','two_or_more'])
arr = st.sidebar.selectbox(label='Arrival Time', options=['Early_Morning','Morning','Afternoon','Evening','Night','Late_Night'])
des = st.sidebar.selectbox(label='Destination City', options=['Bangalore', 'Chennai','Delhi','Hyderabad','Kolkata','Mumbai'])
cls = st.sidebar.selectbox(label='Class', options=['Economy','Business'])

dur = st.slider(label='Duration', min_value=0.83, max_value=49.83, value=5.0, step=0.01)

dl = st.number_input(label='Days Left', min_value=1, max_value=49, value=14, step=1)


# convert into dataframe
data = pd.DataFrame({'airline': [air],
                'source_city': [sou],
                'departure_time': [dep],
                'stops':[sto],
                'arrival_time': [arr],
                'destination_city': [des],
                'class': [cls],
                'duration': [dur],
                'days_left': [dl]})

# model predict
clas = model.predict(data).tolist()[0]

# interpretation
if st.button('Predict'):
    st.write('Harga Tiket Pesawat: ',clas,'₹')
