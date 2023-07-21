import streamlit as st
import pickle as pkl
import numpy as np

filename='car_model.sav'

load_model=pkl.load(open(filename,'br'))

st.title('Car price prediction model')

def pred(x):
    x=np.array(x).reshape(1,-1)
    return model.predict(x)[0]

# [Year,Present_Price,KMs,Fuel_Type,Seller_Type,Transmission,Owner]
def main():
    year=st.number_input("Enter year of make of your vehicle")
    exp_price=st.number_input("Enter your expected price")
    kms=st.number_input("Amount of km run")
    option=st.selectbox('Fuel Type of your vehicle:',('Choose Fuel','Petrol','Diesel','CNG'))
    seller=st.selectbox('Seller Type:',('Choose Seller Type','Dealer','Indiviual'))
    Transmission=st.selectbox('Transmission Type of your vehicle:',('Choose Transmission','Manual','Automatic'))
    if year<1950:
        st.write("Invalid:",int(year))
    else:
        st.write("Year of make is:",int(year))
    st.write('You selected:',option)

if __name__=="__main__":
    main()