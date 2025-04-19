import streamlit as st
import pandas as pd
from collections import Counter
from fpdf import FPDF
import json

# Sayfa başlığı ve yapı
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .sidebar .sidebar-content { padding-top: 1.5rem; }
    .css-1d391kg { background-color: #f0f2f6; border-radius: 8px; }
    .css-1v0mbdj p { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Antika Müşteri Öneri Paneli")
st.markdown("---")

# Sidebar menü
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Antiques_roadshow_logo.png/600px-Antiques_roadshow_logo.png", width=220)
st.sidebar.markdown("### 🚀 Menü")
menu_secimi = st.sidebar.radio("Bir işlem seçin:", ["🔍 Öneri Sistemi", "📤 Veri Yükle", "📊 Favori Analizi", "🧾 PDF & JSON Çıktısı"])

# Favori ürünler için session_state başlat
if "favoriler" not in st.session_state:
    st.session_state.favoriler = []

# PDF oluşturma fonksiyonu
def favori_listesini_pdf_yap(favoriler):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Favori Ürünler Listesi", ln=True, align="C")
    for fav in favoriler:
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"{fav['ad']} - {fav['fiyat']}", ln=True)
        pdf.cell(200, 10, txt=f"Link: {fav['link']}", ln=True)
    path = "favori_listesi.pdf"
    pdf.output(path)
    return path

# JSON çıktısı oluşturma fonksiyonu
def favorileri_json_yap(favoriler):
    path = "favori_listesi.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(favoriler, f, indent=2, ensure_ascii=False)
    return path
