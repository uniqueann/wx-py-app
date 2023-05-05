# app.py

import streamlit as st
from pages import home, about
from components import navbar, footer

# 定义应用程序路由逻辑
def main():
    page = navbar.navbar()
    if page == 'Home':
        home.app()
    elif page == 'About':
        about.app()


    # 显示页脚
    footer.footer()

if __name__ == '__main__':
    main()
