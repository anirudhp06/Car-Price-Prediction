import streamlit as st
import pickle as pkl
import numpy as np
import traceback
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL,'en_IN')
def custom_alert(message):
    st.markdown(f'<div style="background-color:red;padding:10px;border-radius:5px">{message}</div><br>', unsafe_allow_html=True)

filename='car_model.sav'

load_model=pkl.load(open(filename,'br'))

st.title('Car price prediction model')

def pred(x):
    if x[0] < 2010 and x[3] == 1:
        custom_alert("Warning:Vehicle may not be allowed in delhi\ndue to Diesel vehicle ban.")
        #return -1
    x=np.array(x).reshape(1,-1)
    return load_model.predict(x)[0]

# [Year,Present_Price,KMs,Fuel_Type,Seller_Type,Transmission,Owner]
def main():
    try:
        year1=int(datetime.now().year)
        year= st.number_input('Enter year of make', min_value=1975, max_value=year1, value=1975, step=1)
        exp_price=st.number_input("Enter your expected price",min_value=100,value=100,step=1)
        kms=st.number_input("Amount of km run",min_value=500,max_value=99999,value=500,step=1)
        option=int(st.selectbox('Fuel Type of your vehicle:',('Choose Fuel -1','Petrol 0','Diesel 1','CNG 2')).split()[1])
        seller=int(st.selectbox('Seller Type:',('Choose Seller Type -1','Dealer 0','Indiviual 1')).split()[1])
        Transmission=int(st.selectbox('Transmission Type of your vehicle:',('Choose Transmission -1','Manual 0','Automatic 1')).split()[1])
        owner=int(st.selectbox('Owner Type:',('Choose Owner type -1','First 0','Second 1','Third 2','Fourth 3')).split()[1])
        if year<1975:
            custom_alert('Vehicle too old to predict')
            custom_alert('Year of make is:{}'.format(int(year)))
            return
        else:
            st.write("Year of make is:",int(year))
        st.write('Expected price of seller is:{}/-'.format(int(exp_price)))
        st.write('Kilometers run:',kms)
        st.write('Type of fuel:',option)
        st.write('Type of seller:',seller)
        st.write('Transmission type:',Transmission)
        st.write('Type of Owner:',owner)
        ls=[year,exp_price,kms,option,seller,Transmission,owner]
        print(ls)
        if st.button("Predict Price"):
            prediction=pred(ls)
        if prediction !=-1:
            prediction=locale.format_string("%.2f",prediction,grouping=True)
            st.write("Expected price of the vehicle provided is:{}/-".format(prediction))
    except:
        print('\n\n\n\nException occured but handled silently')
        traceback.print_exc()
        st.write("Enter all options correctly to show details")

if __name__=="__main__":
    main()

# delhi 15 yrs