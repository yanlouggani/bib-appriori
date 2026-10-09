import streamlit as st
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

st.set_page_config(page_title="Algorithme d'appriori",page_icon="⚙️")
st.sidebar.success("séléctionnez une page audessus")

st.title("Application d el'algorithme d'appriori sur la simulation de données d'emprunt d'une bibliothèque")
st.write("télécharger le fichier excel contenant les données d'emprunt de la bibliothèque")
fichier = st.file_uploader("Upload a file", type=["xlsx"])
if fichier is not None:
    sheet = st.selectbox("choisi ta feuille", pd.ExcelFile(fichier).sheet_names)
    data = pd.read_excel(fichier, sheet_name=sheet)
    col1,col2,col3= st.columns(3)
    with col1:
        borrowed_at = st.selectbox("choisi la colonne de date d'emprunt :", data.columns,index=None, placeholder="choisi la colonne de date d'emprunt")
    with col2:
        student_id = st.selectbox("choisi la colonne de l'identifiant de l'étudiant", data.columns,index=None, placeholder="choisi la colonne de l'identifiant de l'étudiant")
    with col3:
        notice_id = st.selectbox("choisi la colonne de l'identifiant de la notice", data.columns,index=None, placeholder="choisi la colonne de l'identifiant de la notice")
    if borrowed_at not in data.columns or student_id not in data.columns or notice_id not in data.columns:
        st.write("en attente du choix des colonnes")
    else:
        df1_1= data[(9<=data[borrowed_at].dt.month)&(data[borrowed_at].dt.month<=12) ]
        df1_2= data[(1==data[borrowed_at].dt.month) ]
        df1= pd.concat([df1_1,df1_2])
        df1_session= df1
        df2= data[(9>data[borrowed_at].dt.month) & (data[borrowed_at].dt.month>1)]
        df2_session= df2
        if not df1.empty:
            st.title("donner du premier semestre : ")
            min_sup = st.slider("choisi ton min sup",min_value=0.0,max_value=1.0,value=0.05,step=0.01,key="min_sup_1")
            min_conf = st.slider("choisi ton min conf",min_value=0.0,max_value=1.0,value=0.05,step=0.01,key="min_conf_1")
            df1=df1.groupby([student_id])[notice_id].agg(",".join).reset_index()
            df1=df1.drop([student_id],axis=1)
            new= df1[notice_id].str.split(",", n=0, expand=False)
            array_1= new.to_numpy()
            te= TransactionEncoder().set_output(transform="pandas")
            te_arr= te.fit(array_1).transform(array_1)
            frequent_items = apriori(te_arr,min_support = min_sup,use_colnames=True)
            rules = association_rules(frequent_items, metric='confidence',min_threshold=min_conf)
            st.write("les regles d'association du premier semestre : ")
            st.write(rules)
        if not df2.empty:
            st.title("donner du second semestre : ")
            min_sup = st.slider("choisi ton min sup",min_value=0.0,max_value=1.0,value=0.05,step=0.01,key="min_sup_2")
            min_conf = st.slider("choisi ton min conf",min_value=0.0,max_value=1.0,value=0.05,step=0.01,key="min_conf_2")
            df2=df2.groupby([student_id])[notice_id].agg(",".join).reset_index()
            df2=df2.drop([student_id],axis=1)
            new= df2[notice_id].str.split(",", n=0, expand=False)
            array_2= new.to_numpy()
            te= TransactionEncoder().set_output(transform="pandas")
            te_arr_2= te.fit(array_2).transform(array_2)
            frequent_items_2 = apriori(te_arr_2,min_support = min_sup,use_colnames=True)
            rules_2 = association_rules(frequent_items_2, metric='confidence',min_threshold=min_conf)
            st.write("les regles d'association du second semestre : ")
            st.write(rules_2)


        if "df1" not in st.session_state:
            st.session_state["df1"]=df1_session
        if "df2" not in st.session_state:
            st.session_state["df2"]=df2_session
        if "frequent_items1" not in st.session_state:
            st.session_state["frequent_items1"]=frequent_items
        if "frequent_items2" not in st.session_state:
            st.session_state["frequent_items2"]=frequent_items_2
        if "rules1" not in st.session_state:
            st.session_state["rules1"]=rules
        if "rules2" not in st.session_state:
            st.session_state["rules2"]=rules_2
        if "min_sup1" not in st.session_state:
            st.session_state["min_sup1"]=min_sup
        if "min_sup2" not in st.session_state:
            st.session_state["min_sup2"]=min_sup
        if "min_conf1" not in st.session_state:
            st.session_state["min_conf1"]=min_conf
        if "min_conf2" not in st.session_state:
            st.session_state["min_conf2"]=min_conf

    st.write("vous pouvez maintenant aller sur la page de recommandation pour tester l'algorithme d'appriori sur les données d'emprunt de livres de la bibliothèque"
        )
    st.write(st.session_state["df1"])




