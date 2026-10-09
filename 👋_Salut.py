import io
import streamlit as st
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

st.set_page_config(page_title="Application de l'algorithme d'appriori sur une simulation de données d'emprunts de livres d'une bibliothèque", 
                   page_icon="👋" )
st.sidebar.success("séléctionnez une page audessus")

st.title("Bienvenue dans notre demonstration de l'algorithme d'appriori dans le contexte d'une bibliothèque 👋")
st.markdown("---")
st.markdown("L'algorithme d'appriori est un algorithme d'exploration de données utilisé pour découvrir des motifs fréquents dans des ensembles de transactions. Il est souvent utilisé dans le domaine du commerce électronique pour identifier les produits qui sont souvent achetés ensemble, mais il peut également être appliqué à d'autres domaines tels que la santé, la finance et la sécurité.")
st.markdown("Dans cette démonstration, nous allons appliquer l'algorithme d'appriori sur un ensemble de données simulant les emprunts de livres dans une bibliothèque. Nous allons découvrir les motifs fréquents d'emprunts de livres et générer des règles d'association à partir de ces motifs.")
st.markdown("vous trouverez ci-dessous un exemple de fichier excel contenant les données d'emprunts de livres dans une bibliothèque. Vous pouvez télécharger ce fichier et l'utiliser pour tester l'algorithme d'appriori.")
all_sheets = pd.read_excel(
    "dataset_apriori_bibliotheque_2025_2026.xlsx", sheet_name=None
)

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    for sheet_name, df in all_sheets.items():
        df.to_excel(
            writer, sheet_name=sheet_name, index=False
          ) 

excel_bytes = buffer.getvalue()

st.download_button(
    label="Télécharger l'exemple de fichier Excel",
    data=excel_bytes,
    file_name="data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    icon=":material/download:",
)