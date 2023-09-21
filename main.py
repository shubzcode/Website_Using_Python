import streamlit as st 

name = st.text_input("Enter your Name : ")
fname = st.text_input("Enter Your surname: ")
adr = st.text_area("Enter your text: ")
classdata = st.selectbox("Enter your class : ",(1,2,3,4,5,6,7))

button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {name}
                Surname : {fname}
                adress : {adr}
                class : {classdata}""")