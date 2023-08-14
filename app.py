import streamlit as st 
import streamlit.components.v1 as stc
import pandas as pd
import pygwalker as pyg
# .\pyvenv\Scripts\activate

def init():
    st.set_page_config(
        page_title="StWalker App",
        layout="wide"
    )

def load_data(data):
    return pd.read_csv(data)

def main():
    with st.sidebar.form("upload_form"):
        data_file = st.file_uploader("Upload a CSV file:", type=['csv', 'txt'])
        submitted = st.form_submit_button("Submit")
    if submitted:
        df = load_data(data_file)
        # st.dataframe(df)
        pyg_html = pyg.walk(df, return_html=True)
        stc.html(pyg_html, scrolling=True, height=1000)

if __name__ == "__main__":
    main()