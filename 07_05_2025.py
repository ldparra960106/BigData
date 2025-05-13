# cd C:\Users\luisp\OneDrive - UPV\ESTP\2do\BIG_DATA
# Pour l'activer: streamlit run 07_05_2025.py
import streamlit as st
import pandas as pd

st.write('hello LUIS PARRA GONZALEZ , world this is  a streamlit app-')
st.title('My stramlit app')
st.subheader('Try out the app!')
st.text('This is a simple text element')

graph_type=st.sidebar.selectbox('choisissez un type de graphique:',['Ligne','Barres','aucun'])
st.write(f'Vous avez choisi le type de graphique: {graph_type}')

uploaded_file = st.file_uploader('Telecharger un fichier CSV', type=['csv'])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())

    #4 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique sélectionné.")

st.write("Merci d'avoir utilisé notre application")

#4 SLider
age = st.slider("Quel age avez-vous ?", 0, 100, 25)
st.write(f"Vous avez {age} ans.")

import numpy as np
# Checkbox
if st.checkbox("Afficher un tableau aléatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']))
