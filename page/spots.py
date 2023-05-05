import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("主菜单", ["景区列表", '关于'], 
        icons=['list', 'about'], menu_icon="cast", default_index=1)
    selected
