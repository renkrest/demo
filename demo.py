# Mebgimpor library
import streamlit as st

# Membuat judul
st.title('JUDUL FRESH')

from PIL import Image

# Menambah subheader
st.subheader('Selamat datang di Data Science Deployment')

image = Image.open('D:\Megabagusid\Python Masterclass\ML Deployment\Streamlit\data science.jpg')
st.image(image, use_column_width=True)

# Menulis text (ukuran kecil)
st.write('blablabla')

st.write('tulisan bawahnya')

# Membuat markdown
st.markdown('Ini adalah markdown cell seperti di jupyter notebook')

# Membuat keterangan sukses
st.success('Selamat Anda berhasil')

# Memunculkan error
st.error('Ini keterangan error')