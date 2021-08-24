import pandas as pd
import base64
import streamlit as st
import numpy as np

def create_df(method, coordinate, threshold, state_input, lower = np.array([-1]), upper = np.array([-1])):
    df = pd.DataFrame()
    st.write(method)
    df['method'] = [method]
    df['coordinate'] = [coordinate]
    df['threshold'] = [threshold]
    
    df['state'] = [state_input]
    df['lower'] = [lower.tolist()]
    df['upper'] = [upper.tolist()]
    
    
    
#     'Download Parameter'
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings
    linko= f'<a href="data:file/csv;base64,{b64}" download="Parameter.csv">Download Parameter File</a>'
    st.markdown(linko, unsafe_allow_html=True)