import streamlit as st

st.title("Hello Techeie !!!")
name = st.text_input("Enter your Name : ")
# name = st.text_input("Enter Your name:" , "Type Here ...")
fname = st.text_input("Enter Your surname: ")
adr = st.text_area("Address: ")
status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
classdata = st.selectbox("Skills : ",["Software", "Hardware", "HTML", "CSS", "JavaScript", "Java", "Mobile"])

button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {name}
                Surname : {fname}
                Gender : {status}
                address : {adr}
                class : {classdata}""")
