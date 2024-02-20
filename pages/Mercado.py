import streamlit as st
import pandas as pd
import plotly.express as px
import ipdb
st.set_page_config(layout="wide")

st.header('Mercado', divider='blue')
st.subheader('Caracterización')
df1 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla1')
df1 = df1[df1["FABRICANTES"] != "TOTAL"]
for i in df1.columns[1: 5]:
    df1[i] = df1[i]*100
    df1[i] = df1[i].apply(lambda x: round(x, 2))
st.markdown('**Ventas por mes tercer trimestre 2023 por marca en dinero y posición relativa del mercado**')
st.dataframe(df1.style.highlight_max(axis=0), use_container_width=True)

col1, col2= st.columns(2)
df2 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla2')
df2["Mercado"] = df2["Mercado"].apply(lambda x: x[:x.find(" T")])
fig = px.pie(df2, values='TOTAL %', names='Mercado', title='Cobertura de mercado por región', hole=.3)
col1.plotly_chart(fig, use_container_width=True)

df2a = df2.drop(columns="TOTAL %")
cols = ["ANTIOQUIA_CHOCO", "CUNDI_BOY", "ATLANTICO"]
df2a = df2a[df2a["Mercado"].isin(cols)]
df2a = df2a.melt(id_vars=['Mercado'], var_name='Fecha', 
                 value_name='Ventas %')
fig2 = px.line(df2a, x="Fecha", y="Ventas %", color='Mercado', 
               symbol="Mercado", title='Evolución ventas top 3 regiones')
col2.plotly_chart(fig2)

df3 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla3')
fig3a = px.pie(df3, values='VENTAS $', names='SEGMENTO', 
               title='% Ventas $ por segmento', hole=.3)
st.plotly_chart(fig3a, use_container_width=True)

df4 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla4')
fig4 = px.icicle(df4, path=[px.Constant("all"), 'PRESENTACIÓN', 'GRAMAJE'], 
                 values='VENTAS UNI %', title='Ventas unitarias por tipo de presentación y gramaje')
fig4.update_traces(root_color="darkblue")
st.plotly_chart(fig4, use_container_width=True)

texto = """- Alpina tiene un dominio absoluto del mercado de bebidas lacteas en Colombia con una cobertura de mercado del 67 % en el tercer trimestre del 2023. Este predominio se ve reforzado con los datos de sus ocho mejores competidores (Fabricantes) quienes tienen una cobertura del mercado entre el 1% y el 9%.  
- A pesar de que el mercado se expandio mes tras mes alpina decayó en su participación del mercado mas de un 1.5 % desde julio hasta septiembre.
- Atlantico, la región cundiboyacense y Antioquía con Choco cubren más del 70 % de las ventas (en dinero) del mercado de bebidas lacteas en el país.
- Antioquía y la región Cundiboyacense tienen tendencia de crecimiento en ventas (en dinero).
- El 90 % de las ventas (en dinero) se realizan en los segmentos YOG CTE + REF LACTEO, Adiciones y avena.
- El mercado colombiano demanda principalmente productos en vaso entre 150 - 199 cc  (36 % de undiades vendidas) y productos en bolsa entre 200 - 250 cc (19 % de undiades vendidas)""" 

st.write(texto)
st.divider()
st.subheader('Yogo Yogo Oportunidades y estrategia')



col6, col7= st.columns(2)
df7 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla7')
df7["SIZE"] = 4
fig7 = px.scatter(df7, x="COBERTURA $ ", y="GRAMAJE", color="MARCA", size="SIZE",
                 title="Cobertura Yogo Yogo vs mejor marca (no alpina) por gramaje"
                )
col6.plotly_chart(fig7)

df6 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla6')
fig6 = px.bar(df6, x='RANGOS UNIF', y='VENTAS $', 
              title='Ventas por gramaje productos mismas caracteríticas Yogo Yogo')
col7.plotly_chart(fig6)


col8, col9= st.columns(2)

df8 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla8')
df8["SIZE"] = 4
df8["REGIÓN"] = df8["REGIÓN"].apply(lambda x: x[:x.find(" T")])
fig8 = px.scatter(df8, x="COBERTURA $ ", y="REGIÓN", color="MARCA", size="SIZE",
                 title="Cobertura Yogo Yogo vs mejor marca (no alpina) por gramaje"
                )
col8.plotly_chart(fig8)

df5 = pd.read_excel("AlpinaCaso.xlsx", sheet_name='Tabla5')
df5["REGION"] = df5["REGION"].apply(lambda x: x[:x.find(" T")])
fig5 = px.bar(df5, x='REGION', y='VENTAS $', 
              title='Ventas por región productos mismas caracteríticas Yogo Yogo')
col9.plotly_chart(fig5)


texto2 = """
Según los datos recopilados, considerando la predominancia de Alpina en el mercado, las oportunidades de la marca Yogo Yogo se centran en el gramaje de sus presentaciones y en las regiones de distribución. Teniendo en cuenta que la marca Yogo Yogo participa principalmente en el segmento de productos de presentación regular, como envases de botella, vaso, bolsa y caja aséptica, y en los segmentos de Yogures Cuchareables, Adiciones y YOG CTE + REF LACTEO, se puede concluir lo siguiente:

- Yogo Yogo no lidera las ventas (en términos de ingresos) en gramajes menores a 100 cc, entre 130 cc - 149 cc y superiores a 200 cc e inferiores a 999 cc.
- Los productos con mayor volumen de ventas en el mismo segmento y presentación son aquellos de menor gramaje, que oscilan entre 100 cc y 200 cc. Esto destaca su popularidad entre un público notablemente joven, debido a su practicidad para el transporte y su consumo en momentos distintos a las comidas principales del día.
- Yogo Yogo no es una marca predominante en las regiones de Santanderes y Antioquia-Chocó.
- Antioquia-Chocó y Santanderes, respectivamente, ocupan el tercer y quinto lugar en importancia en el mercado para los productos similares a Yogo Yogo.

En consecuencia, como parte del plan de acción, se sugiere que Yogo Yogo se enfoque en la fabricación y revitalización, según sea necesario, de presentaciones de sus productos en los gramajes específicos de 131 a 150 cc y de 200 a 250 cc, especialmente dirigido a las regiones de Antioquia-Chocó y Santanderes. Dado su no liderazgo, es en estas presentaciones y áreas geográficas donde la marca tiene una mayor oportunidad de expansión y crecimiento.
""" 

st.write(texto2)
