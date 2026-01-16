import streamlit as st
import random
import time

st.set_page_config(
    page_title="THE LAST ANALYST",
    page_icon="☠️",
    layout="centered"
)

# =====================
# INIT STATE
# =====================
if "scene" not in st.session_state:
    st.session_state.scene = "intro"
if "fear" not in st.session_state:
    st.session_state.fear = 0
if "door" not in st.session_state:
    st.session_state.door = False
if "shadow" not in st.session_state:
    st.session_state.shadow = False

def add_fear(x):
    st.session_state.fear += x
    if st.session_state.fear > 100:
        st.session_state.fear = 100

st.title("☠️ THE LAST ANALYST")
st.caption("02:47 WIB | Laboratorium Kimia Analisis | Lampu Mati")

st.progress(st.session_state.fear)
st.write("TINGKAT TEROR")

# =====================
# GAME OVER
# =====================
if st.session_state.fear >= 100:
    st.error("NAPASMU TERHENTI.")
    st.write("""
    Kamu merasa ada tangan dingin menyentuh lehermu.
    Suara berbisik tepat di telingamu:

    *“Data ini tidak pernah lulus validasi…”*
    """)
    st.stop()

# =====================
# SCENE LOGIC
# =====================
if st.session_state.scene == "intro":
    st.write("""
    Kamu sendirian di laboratorium.
    Semua orang sudah pulang.
    Timbangan analitik menyala sendiri.
    Ada **bayangan berdiri di belakangmu**.
    """)
    if st.button("Menoleh perlahan"):
        add_fear(20)
        st.session_state.shadow = True
        st.session_state.scene = "shadow_seen"
    if st.button("Lari ke lorong"):
        add_fear(10)
        st.session_state.scene = "hallway"

elif st.session_state.scene == "shadow_seen":
    st.write("""
    Bayangan itu tidak punya wajah.
    Tapi **ia sedang menatapmu**.
    """)
    if st.button("Menyebut namanya"):
        add_fear(30)
    if st.button("Menutup mata"):
        st.session_state.scene = "hallway"

elif st.session_state.scene == "hallway":
    st.write("""
    Lorong laboratorium.
    Lampu berkedip.
    Ada suara **langkah mengikuti langkahmu**.
    """)
    if st.button("Masuk ruang preparasi"):
        add_fear(15)
        st.session_state.scene = "prep_room"
    if st.button("Sembunyi di ruang QC"):
        st.session_state.scene = "qc_room"

elif st.session_state.scene == "prep_room":
    st.write("""
    Ruang preparasi gelap.
    Bau asam kuat.
    Di meja ada **jas lab bernoda hitam**.
    """)
    if st.button("Sentuh jas lab"):
        add_fear(25)
        st.write("*Jas itu MASIH HANGAT.*")
    if st.button("Ambil kunci di meja"):
        st.session_state.door = True
        add_fear(10)
    if st.button("Keluar"):
        st.session_state.scene = "hallway"

elif st.session_state.scene == "qc_room":
    st.write("""
    Ruang QC.
    Whiteboard penuh coretan:
    **%RSD… GAGAL… ULANG…**
    Tiba-tiba papan itu BERGERAK SENDIRI.
    """)
    if st.button("Mendekat"):
        add_fear(30)
        st.session_state.scene = "board"
    if st.button("Kabur"):
        add_fear(10)
        st.session_state.scene = "hallway"

elif st.session_state.scene == "board":
    st.write("""
    Tulisan di papan berubah:
    **“KAMU TIDAK SENDIRIAN.”**
    Napas panas tepat di belakang lehermu.
    """)
    if st.button("Menoleh"):
        add_fear(40)
    if st.button("Lari ke pintu keluar"):
        if st.session_state.door:
            st.success("PINTU TERBUKA.")
            st.write("Kamu berlari keluar. Bayangan itu BERHENTI DI AMBANG PINTU.")
            st.balloons()
            st.stop()
        else:
            add_fear(20)
