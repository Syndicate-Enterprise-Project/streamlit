import streamlit as st
import base64

from streamlit_option_menu import option_menu
from view import home
st.set_page_config(layout="wide")

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("data/background.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:background/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    st.sidebar.image("data/syndicate.png", caption="")
    st.sidebar.title("Selamat Datang!")
    with st.sidebar:
        page = option_menu("Main Menu",
                           ["Home", "Clustering"],
                           icons=["house", "book"],
                           menu_icon="cast", default_index=0,
                           styles={
                               "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px",
                                            "--hover-color": "#a01239"},
                               "nav-link-selected": {"background-color": "#ed1d56"},
                           })
    if page == "Home":
        home.main()
    elif page == "Clustering":
        pass


if __name__ == '__main__':
    main()
