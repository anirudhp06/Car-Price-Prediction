import streamlit as st
import pickle as pkl
import numpy as np
import traceback
import locale
from datetime import datetime
from streamlit.components.v1 import html
import streamlit.components.v1 as components

locale.setlocale(locale.LC_ALL,'en_IN')

def custom_alert(message):
    st.markdown(f'<div style="background-color:red;padding:10px;border-radius:5px">{message}</div><br>', unsafe_allow_html=True)

filename='car_model.sav'
load_model=pkl.load(open(filename,'br'))

# Set title of page
st.set_page_config(page_title="Car Price Predictor",page_icon='favicon.png')
st.title('Car price prediction model')

def pred(x):
    x=np.array(x).reshape(1,-1)
    return load_model.predict(x)[0]

# Mapping of data
fuel_type_mapping={'Petrol':0,'Diesel':1,'CNG':2}
seller_type_mapping={'Dealer':0,'Individual':1}
transmission_type_mapping={'Manual':0,'Automatic':1}
owner_type_mapping={'First':0,'Second':1,'Third':2,"Fourth":3}

# [Year,Present_Price,KMs,Fuel_Type,Seller_Type,Transmission,Owner]
def main():
    try:
        present_year=int(datetime.now().year)

        year=st.number_input('Enter year of make', min_value=1975, max_value=present_year, value=1975, step=1)
        exp_price=st.number_input("Enter your expected price",min_value=50000,value=50000,step=1)
        kms=st.number_input("Amount of km run",min_value=1500,max_value=99999,value=1500,step=1)
        
        # Mapping Values
        fuel_str=st.selectbox('Fuel type of Vehicle',('Petrol','Diesel','CNG'))
        fuel=fuel_type_mapping[fuel_str]

        seller_str=st.selectbox('Seller Type:',('Dealer','Individual'))
        seller=seller_type_mapping[seller_str]

        transmission_str=st.selectbox('Transmission Type of your vehicle:',('Manual','Automatic'))
        transmission=transmission_type_mapping[transmission_str]

        owner_str=st.selectbox('Owner Type:',('First','Second','Third','Fourth'))
        owner=owner_type_mapping[owner_str]

        if present_year - year > 10:
            custom_alert("Vehicle may not be allowed in Delhi ({} make), Due to emission norms".format(year))
        else:
            st.write("Year of make is:",int(year))
        st.write('Expected price of seller is:{}/-'.format(int(exp_price)))
        st.write('Kilometers run:',locale.format_string("%.0f",kms,grouping=True),"kms")
        st.write('Type of fuel:',fuel_str)
        st.write('Type of seller:',seller_str)
        st.write('Transmission type:',transmission_str)
        st.write('Type of Owner:',owner_str)
        ls=[year,exp_price,kms,fuel,seller,transmission,owner]
        print(ls)
        if st.button("Predict Price"):
            prediction=pred(ls)
            prediction=locale.format_string("%.2f",prediction,grouping=True)
            st.write("Expected price of the vehicle provided is:{}/-".format(prediction))
    except:
        print('\n\n\n\nException occured but handled silently')
        traceback.print_exc()
        st.write("Enter all options correctly to show details")

def alert(message):
    # Used to make alert boxes in streamlit app
    # Still haven't used this in any program.

    # Define your javascript
    my_js = "alert('{}');".format(message)
    # Wrap the javascript as html code
    my_html = f"<script>{my_js}</script>"
    html(my_html)

if __name__=="__main__":
    main()


