# TP2: CREER UNE APPLICATION STREAMLIT

# Étape 3 - Chargement des librairies
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Étape 4 - Demander le nom de l'utilisateur et le saluer
name = st.text_input("Quel est votre prénom ?")
if name:
    st.write(f"Bonjour, {name}")

# Étape 5 - Chargement des données
st.title("Step 3 - Importation de la base E+C-")
uploaded_file = st.file_uploader("Importez le fichier Excel E+C- (feuille 'batiments')", type=["xlsx"])
if uploaded_file:
    df_raw = pd.read_excel(uploaded_file, sheet_name='batiments', header=[0,1])
    df_raw.columns = df_raw.columns.droplevel(0)
    st.dataframe(df_raw.head(3))

    st.subheader("Statistiques descriptives")
    st.write(df_raw.describe())

    # Étape 6 - Afficher un premier graphique
    st.title("Step 4 - Nuage de points")
    st.write("Tous les bâtiments sont représentés dans le diagramme ci-dessous.")
    fig = px.scatter(df_raw, x=df_raw['id_batiment'], y=df_raw['eges'], title="ÉGES par bâtiment")
    st.plotly_chart(fig, use_container_width=True)

    # Étape 7 - Corrélations
    st.title("Step 5 - Matrice de corrélation")
    corr_df = df_raw.select_dtypes(include='number')  # seulement les colonnes numériques
    corr_matrix = corr_df.corr()
    fig_corr, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig_corr)

    # Étape 8 - BONUS : graphique interactif + filtre
    st.title("Step 6 - Analyse interactive")

    numeric_cols = corr_df.columns.tolist()
    x_var = st.selectbox("Variable X", numeric_cols, index=0)
    y_var = st.selectbox("Variable Y", numeric_cols, index=1)

    if 'eges' in df_raw.columns:
        min_eges = float(df_raw['eges'].min())
        max_eges = float(df_raw['eges'].max())
        range_eges = st.slider("Filtrer les bâtiments par ÉGES", min_eges, max_eges, (min_eges, max_eges))

        df_filtered = df_raw[(df_raw['eges'] >= range_eges[0]) & (df_raw['eges'] <= range_eges[1])]

        fig2 = px.scatter(df_filtered, x=x_var, y=y_var, color='eges', title="Graphique interactif filtré")
        st.plotly_chart(fig2)
