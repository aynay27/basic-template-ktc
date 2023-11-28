import streamlit as st

st.set_page_config(
    page_title="Organizational Experience|Inayah",
    page_icon="😼",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Beberapa Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Team Readaksi Plural")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("img/plural.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai Anggota Team Redaksi Plural*")
   
st.container()
col1, = st.columns(1)
with col1:
    st.subheader("ISIM Al-Bukhori")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("img/isim.png", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai Anggota ISIM Al-Bukhori*")
   