import streamlit as st
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

img_1 = Image.open("img/images1.jpg")
img_2 = Image.open("img/images2.jpg")
img_3 = Image.open("img/images3.jpg")
img_4 = Image.open("img/images4.jpg")

st.title("🫶 Hobbies")
st.write("Hobi menurut saya adalah ekspresi diri dan pelepas stress. Berikut beberapa hobi yang saya gemari")

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.image(img_1)
   
with col2:
   st.image(img_2)

with col3:
   st.image(img_3)

with col4:
   st.image(img_4)