import streamlit as st
import numpy as np

st.title("Programme de choix aléatoire")

if st.button("Poser une question et obtenir une réponse"):
    choix = np.random.randint(1, 5)
    answer = "Oui" if choix == 1 else "Non" if choix == 2 else "Peut-être" if choix == 3 else "Peut-être pas"
    st.success(f"**{answer}**")