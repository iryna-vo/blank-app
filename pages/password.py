import streamlit as st

st.title("Vérification de mot de passe")
password = "mypassWord"
saisie = st.text_input("Enter your password :")
while saisie != password:
    print("Error. Try again")
print("Well done!")