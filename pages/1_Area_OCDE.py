import streamlit as st
from pages.utils.ui_theme import setup_page

setup_page("Proyecto de Investigación")

st.title("Área OCDE y Objetivos de Desarrollo Sostenible")
left, right = st.columns([1.1, 1], gap="large", vertical_alignment="center")

with left:
    st.markdown(
    """
La idea central de esta investigación se enmarca exclusivamente en el dominio de las Ciencias Sociales, específicamente en el área de la Geografía. 
El problema fundamental a resolver es la comprensión y delimitación espacial de las dinámicas territoriales del conflicto en Ucrania, analizando cómo la violencia 
transforma el territorio a lo largo del tiempo.

Además, el proyecto se alinea directamente con dos Objetivos de Desarrollo Sostenible (ODS) de la ONU. Primero, con el ODS 16 ("Paz, justicia e instituciones sólidas"), 
al aportar inteligencia geoespacial empírica para mapear objetivamente la violencia. Segundo, con el ODS 11 ("Ciudades y comunidades sostenibles"), ya que al separar 
matemáticamente el combate de infantería de los bombardeos remotos sobre áreas urbanas, el modelo facilita la identificación de zonas de riesgo y corredores de evacuación 
más seguros para la protección civil.

A nivel metodológico, se trata de una investigación cuantitativa, exploratoria y descriptiva. Para procesar el masivo volumen de coordenadas, el proyecto utiliza algoritmos 
de clustering espacial a modo de herramienta de cálculo avanzado. Al delegar la segmentación territorial a modelos de aprendizaje no supervisado, se elimina el sesgo visual humano y se descubren patrones espaciales objetivos basados estrictamente en los datos.
"""
)

with right:
    st.image("pages/photos/OECD.png", width=560)

    