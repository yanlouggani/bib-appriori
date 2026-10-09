import streamlit as st
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

st.set_page_config(page_title="démonstration de recommandation de livres",page_icon="📊")
st.sidebar.success("séléctionne la page audessus")


rules1 = st.session_state["rules1"]
rules2 = st.session_state["rules2"]
frequent_items1 = st.session_state["frequent_items1"]
frequent_items2 = st.session_state["frequent_items2"]


with st.form("recommandation"):
    st.write("vous pouvez choisir le semestre pour lequel vous voulez faire la recommandation de livres")
    semestre =st.selectbox("choisi le semestre", ["premier semestre", "second semestre"], key="semestre")
    st.write("vous pouvez choisir le livre pour lequel vous voulez tester la recommandation de livres")
    notice = st.text_input("choisi le livre", key="livre")
    submitted = st.form_submit_button("valider")
    if submitted:
        st.write("vous avez choisi le semestre : ", semestre)
        if semestre == "premier semestre" and rules1 is not None:
                notice_frozenset = frozenset([notice])
                resultats = list(rules1[rules1["antecedents"] == notice_frozenset]["consequents"])
                str_resultat = lambda x: list(x) if len(x) > 0 else None
                resultats = [str_resultat(x) for x in resultats]
                if resultats is not None:
                    for i, livres in enumerate(resultats, start=1):
                        st.markdown(f" - recommandations {i} : " + ", ".join(livres))
                else:
                    st.write("aucune règle d'association n'a été trouvée pour le livre choisi dans le premier semestre")
        if semestre == "second semestre" and rules2 is not None :
                notice_frozenset = frozenset([notice])
                resultats = list(rules2[rules2["antecedents"] == notice_frozenset]["consequents"])
                str_resultat = lambda x: list(x) if len(x) > 0 else None
                resultats = [str_resultat(x) for x in resultats]
                if resultats is not None:
                    for i, livres in enumerate(resultats, start=1):
                        st.markdown(f" - recommandations {i} : " + ", ".join(livres))
                else:
                    st.write("aucune règle d'association n'a été trouvée pour le livre choisi dans le premier semestre")
            
                #str_rules_antecedents = rules2["antecedents"]
                #str_rules_consequents = rules2["consequents"]
                #str_rules_antecedents = str_rules_antecedents.apply(lambda x: list(x)[0]).astype("unicode")
                #str_rules_antecedents = str_rules_antecedents.tolist()
                #str_rules_consequents = str_rules_consequents.apply(lambda x: list(x)[0]).astype("unicode")
                #str_rules_consequents = str_rules_consequents.tolist()
                #if notice in str_rules_antecedents:
                    #st.write("les livres recommandés pour le livre choisi sont : ")
                    #indexes = np.where(np.array(str_rules_antecedents) == notice)[0]
                    #consequences = [str_rules_consequents[i] for i in indexes]
                    #st.markdown(
                        #"#### Livres recommandés\n" +
                        #"\n".join(f"- {livre}" for livre in consequences)
                    #)