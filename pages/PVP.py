import streamlit as st
import pandas as pd
import plotly.express as px
import ipdb
st.set_page_config(layout="wide")

st.header('Precio de venta al público', divider='blue')
st.subheader("Arquitectura de rpecio por volumen")

colc, cold = st.columns(2)
df9 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='PVP')
df9 = df9.drop(columns=["sku", "sku_string_correct"])
df9.drop_duplicates(subset=["Generico_1"], keep='first', inplace=True)
df9["Cantidad"] = df9["Cantidad"].astype(int)
df9 = df9.sort_values(by=["Generico_2", "Cantidad"])
fig9 = px.line(df9, x="Cantidad", y="g/ml", color="Generico_2", symbol="Generico_2")
colc.plotly_chart(fig9)
cold.image('arqprecios.png')


st.divider()

texto = """
Tras realizar un análisis detallado de la estructura de precios de la marca Yogo Yogo, se observa una consistencia en términos de tipo de envase, contenido unitario y cantidades en todas sus líneas, excepto en un producto específico. Esta coherencia implica que los productos de una misma línea (envase y contenido unitario) disminuyen en su valor por gramo o mililitro a medida que las presentaciones del producto contienen más unidades. En otras palabras, a medida que aumenta la cantidad unitaria en la presentación, el precio por gramo/mililitro disminuye. Sin embargo, el único producto que no sigue esta estructura de precios es el Yogo Bolsa familiar de un litro por 12 unidades, que presenta un precio por mililitro superior al Yogo Bolsa familiar de una unidad y de 1.1 litros.
 """

st.write(texto)