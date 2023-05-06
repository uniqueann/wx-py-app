import streamlit as st
from streamlit_option_menu import option_menu

# 设置页面标题和横幅
st.set_page_config(page_title='沽酒渔歌-首页', page_icon=':canoe:', layout='wide', initial_sidebar_state='expanded')

selected = '主页'

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("", ['主页','景区列表', '关于'], 
        icons=['house','list', 'info-square'], menu_icon="cast", default_index=0)

# 在页面上显示横幅
# st.markdown("""
# <style>
# .banner {
#     display: flex;
#     align-items: center;
#     background-color: #f0f0f0;
#     color: white;
#     padding: 0.5rem;
# }
# .banner img {
#     margin-right: 1rem;
# }
# .banner h1 {
#     margin: 0;
#     font-size: 2rem;
# }
# </style>
# <div class="banner">
# <img src="/assets/images/logo.png" alt="Logo" width="100">
# <h1>尽情沽酒渔歌！</h1>
# </div>
# """, unsafe_allow_html=True)

# 在页面上显示其他内容
# st.write('这是一个示例 Streamlit 应用程序。')

if selected == '主页':
    st.write('主页')
elif selected == '景区列表':
    # 创建一个包含图片、文字和小标题的列表
    with st.beta_container():
        with st.beta_columns([1, 4]):
            with st.beta_container():
                st.image("https://picsum.photos/100", width=100)
            with st.beta_container():
                st.subheader("这是一个小标题")
                st.write("这是一些文字。")

        with st.beta_columns([1, 4]):
            with st.beta_container():
                st.image("https://picsum.photos/100", width=100)
            with st.beta_container():
                st.subheader("这是另一个小标题")
                st.write("这是一些其他的文字。")

elif selected =='关于':
    st.write('关于')



