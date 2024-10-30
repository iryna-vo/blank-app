import streamlit as st

st.title("Vérification de mot de passe")
#password = "mypassWord"
#saisie = st.text_input("Enter your password :")
#while saisie != password:
#    print("Error. Try again")
#print("Well done!")
password = st.text_input("Enter your password :", type = "password")
if password:
    if password == "mypassWord":
        st.success("C'est bon !")
    else: st.error("Mot de passe incorrect. Essayez à nouveau !")
