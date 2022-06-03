import itertools
import streamlit as st
import requests
import json


BASE_URI = "http://127.0.0.1:8000"

def viroids():
    all_sequence = itertools.permutations("CGTA", 4)
    one_sequence = st.text_input("Enter a sequence")
    if one_sequence is not None and len(one_sequence) > 3:
        all_4grams = [one_sequence[i:i+4] for i in range(len(one_sequence)-3)]
        st.write(all_4grams[0:10])

        params = {"sequence": one_sequence}
        response = requests.get(f"{BASE_URI}/viroid", params = params)

        if response.status_code == 200:
             result = response.json()
             if result["prob"] > 0.5:
                  st.markdown(f"# Loup said this sequence is a viroid <{result['prob']}>")
             else:
                  st.markdown(f"# you are safe no viroid around") 
        else:
            st.write("Boom !")

        
