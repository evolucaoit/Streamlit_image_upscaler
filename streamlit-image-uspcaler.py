import streamlit as st
import cv2
import numpy as np
import os
import uuid

# Função para aumentar a escala da imagem e melhorar a resolução
def upscale_image(image, scale_factor=2):
    # Usa INTER_CUBIC para melhorar a qualidade da imagem
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Função para gerar um nome de arquivo único
def generate_unique_filename():
    return f"image_{uuid.uuid4()}.png"

# Interface do Streamlit
st.title("Image Upscale App 📈")

# Upload da imagem
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Lê a imagem como um array do NumPy
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Exibe a imagem original
    st.image(image, caption='Original Image', use_column_width=True)

    # Aplica o upscale
    upscaled_image = upscale_image(image, scale_factor=2)

    # Exibe a imagem melhorada
    st.image(upscaled_image, caption='Upscaled Image', use_column_width=True)

    # Gera um nome de arquivo único
    filename = generate_unique_filename()

    # Salva a imagem melhorada na raiz
    cv2.imwrite(filename, upscaled_image)

    st.success(f"Imagem salva com sucesso como {filename} na raiz do diretório!")

    # Botão para baixar a imagem
    with open(filename, "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name=filename,
            mime="image/png"
        )
