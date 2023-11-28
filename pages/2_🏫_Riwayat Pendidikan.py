import streamlit as st

st.set_page_config(
    page_title="Riwayat Sekolah | Inayah",
    page_icon="🙀",
    layout="wide"
)
st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA ENYAM")

st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("SDN SENGON 03")
   
with col2:
    st.subheader("MTs Plus AL Bukhori")
    
with col3:
    st.subheader("MA Plus AL Bukhori")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("img/sd.png", width= 190)
with col2:
   
    st.image("img/mts.png", width= 190)
with col3:
    
    st.image("img/ma.png", width= 190)
with col4:
    
    st.image("img/unuu.png", width= 190)
