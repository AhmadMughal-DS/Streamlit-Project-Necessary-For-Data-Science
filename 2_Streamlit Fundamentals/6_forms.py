import streamlit as st
import numpy as np
import pandas as pd
with st.form(key="my_form",clear_on_submit= False,border=True):
    header = st.write("# what would you to like to order")
    appetizer = st.selectbox("choose a choices",options=['choice1','choice2','choice3'])
    main=st.selectbox("Main course",options=['choice1','choice2','choice3'])
    dessart = st.selectbox("Dessert",options=['choice1','choice2','choice3'])
    wine = st.checkbox("Are you bringing your own wine")
    date = st.date_input("when are coming")
    time = st.time_input("At what time are you coming:")
    allergies = st.text_area("You have any kind of allerge from any item",placeholder="leave your comment here")
    submit_btn = st.form_submit_button("Submit")
st.write(f"""Your Order Summary*\n
    Appertizer: {appetizer}
    Main Course: {main}
    Dessert: {dessart}
    Are you bring wine your own{"Yes" if wine else "no"}
    Date of visits:{date}
    Time of visits:{time}
    Allergies{allergies}         
""")