import streamlit as st
import random
import time

st.set_page_config(page_title="LAB 3A - NIGHT SHIFT", page_icon="🧪")

# STATE INIT
if "scene" not in st.session_state:
    st.session_state.scene = "intro"
if "sanity" not in st.session_state:
    st.session_state.sanity = 100
if "key" not in st.session_state:
    st.session_state.key = False

def sanity_loss(x):
    st.session_state.sanity -= x
    if st.session_state.sanity < 0:
        st.session_state.sanity = 0

st.title("LAB 3A — NIGHT SHIFT")
st.caption("jam 02:13 | gedung kosong | lampu berkedip")

st.write(f"Sanity: {st.session_state.sanity}%")

# GAME OVER
if st.session_state.sanity <= 0:
    st.error("Kamu kehilangan kendali. Sesuatu berdiri di belakangmu.")
    st.stop()

# SCENES
if st.session_state.scene == "intro":
    st.write("""
    Kamu sendirian di laboratorium analisis.
    Tiba-tiba alat UV-Vis menyala sendiri.
    """)
    if st.button("Mendekati alat"):
        sanity_loss(10)
        st.session_state.scene = "uvvis"
    if st.button("Keluar ruangan"):
        st.session_state.scene = "hallway"

elif st.session_state.scene == "uvvis":
    st.write("""
    Layar UV-Vis menampilkan absorbansi:
    0.666
    Padahal tidak ada sampel.
    """)
    if st.button("Matikan alat"):
        st.session_state.scene = "hallway"
    if st.button("Cek ruang sampel"):
        sanity_loss(15)
        st.session_state.key = True
        st.session_state.scene = "sample_room"

elif st.session_state.scene == "hallway":
    st.write("""
    Lorong gelap.
    Bau formalin.
    Ada suara langkah di belakangmu.
    """)
    if st.button("Lari ke gudang"):
        sanity_loss(20)
        st.session_state.scene = "storage"
    if st.button("Masuk ruang QC"):
        st.session_state.scene = "qc_room"

elif st.session_state.scene == "sample_room":
    st.write("""
    Kamu menemukan botol tanpa label.
    Di bawahnya tertulis:
    'Presisi itu bohong.'
    """)
    if st.button("Ambil botol"):
        sanity_loss(25)
    if st.button("Pergi"):
        st.session_state.scene = "hallway"

elif st.session_state.scene == "storage":
    st.write("""
    Gudang gelap.
    Lemari bergerak sendiri.
    """)
    if st.button("Buka lemari"):
        if st.session_state.key:
            st.success("Kamu menemukan jalan keluar.")
            st.balloons()
            st.stop()
        else:
            sanity_loss(30)
    if st.button("Kembali"):
        st.session_state.scene = "hallway"

elif st.session_state.scene == "qc_room":
    st.write("""
    Ruang QC.
    Whiteboard bertuliskan:
    '%RSD < 2/3 CV Horwitz'
    Tapi angkanya berubah-ubah.
    """)
    if st.button("Hitung ulang"):
        if random.random() > 0.5:
            st.success("Perhitungan benar. Pintu terbuka.")
            st.balloons()
            st.stop()
        else:
            sanity_loss(20)
    if st.button("Kabur"):
        st.session_state.scene = "hallway"
