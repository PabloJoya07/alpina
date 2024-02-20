import streamlit as st
import pandas as pd
import plotly.express as px
import ipdb
st.set_page_config(layout="wide")

st.header('Estado de perdidas y ganacias', divider='blue')
cola, colb = st.columns(2)

df10 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='PYG1')
df10 = df10.melt(id_vars=['Valores'], var_name='Mes', value_name='Desempeño')
df10 = df10[df10['Valores'].isin([" Venta Neta", " Utilidad Bruta", " Descuentos"])]
df10.loc[(df10["Valores"] == " Descuentos"), "Desempeño"] = df10.loc[(df10["Valores"] == " Descuentos"), "Desempeño"]*-1
fig10 = px.line(df10, x="Mes", y="Desempeño", color="Valores", symbol="Valores",
                title= "Dtos, VN Y  UB en dinero")
cola.plotly_chart(fig10)


df11 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='PYG2')
df11 = df11.melt(id_vars=['Valores'], var_name='Mes', value_name='Desempeño')
fig11 = px.line(df11, x="Mes", y="Desempeño", color="Valores", symbol="Valores",
                title= "Dtos, costo VN Y  UB como proporción de las VN")
colb.plotly_chart(fig11)

st.divider()

texto = """
Según el estado de resultados de Alpina para el año 2023, se observa una clara tendencia a la disminución de la utilidad bruta hasta noviembre, lo cual está fuertemente correlacionado con la caída en las ventas. Como resultado, el porcentaje de costo de ventas y descuentos sobre los ingresos ha experimentado un aumento, aunque no de manera significativamente drástica.
"""


st.write(texto)

