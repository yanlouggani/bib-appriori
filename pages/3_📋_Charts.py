import streamlit as st
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

st.set_page_config(page_title="Charts",page_icon="📋")
st.sidebar.success("séléctionnez une page audessus")

rules1 = st.session_state["rules1"]
rules2 = st.session_state["rules2"]
frequent_items1 = st.session_state["frequent_items1"]
frequent_items2 = st.session_state["frequent_items2"]
df1 = st.session_state["df1"]
df2 = st.session_state["df2"]

chart_selector = st.selectbox("choisissez quel graphique vous voulez afficher", ["fréquence d'emprunts par livre S1 et S2","Emprunts de livre par temps" ])

if chart_selector == "fréquence d'emprunts par livre S1 et S2":
    st.write("fréquence d'emprunts de livre S1 et S2")
    semestre1_counts = df1.groupby('notice_id').size()
    semestre2_counts = df2.groupby('notice_id').size()
    df_counts = pd.DataFrame({'Semestre 1': semestre1_counts, 'Semestre 2': semestre2_counts})
    counts_chart = st.bar_chart(df_counts)

elif chart_selector == "Emprunts de livre par temps":
    st.write("Emprunts de livre par temps")
    monthly_counts_1 = df1.groupby(df1['borrowed_at'].dt.to_period('W')).size().reset_index(name='count')
    monthly_counts_2 = df2.groupby(df2['borrowed_at'].dt.to_period('W')).size().reset_index(name='count')
    monthly_counts = pd.concat([monthly_counts_1, monthly_counts_2], ignore_index=True)
    monthly_counts['borrowed_at'] = monthly_counts['borrowed_at'].dt.to_timestamp()

    time_chart = st.line_chart(monthly_counts, x='borrowed_at', y='count')

