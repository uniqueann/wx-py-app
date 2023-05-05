# navbar.py

import streamlit as st

def navbar():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'About'])
    return page
