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
    owner=st.selectbox('Owner Type:',('Choose Owner type','First','Second','Third','Fourth'))
    if year<1975:
        st.write("Invalid:",int(year))
    else:
        st.write("Year of make is:",int(year))
    st.write('Expected price of seller is:{}/-'.format(int(exp_price)))
    st.write('Kilometers run:',kms)
    st.write('Type of fuel:',option)
    st.write('Type of seller:',seller)
    st.write('Transmission type:',Transmission)
    st.write('Type of Owner:',owner)
    ls=[option,seller,Transmission,owner]

if __name__=="__main__":
    main()

# delhi 15 yrs