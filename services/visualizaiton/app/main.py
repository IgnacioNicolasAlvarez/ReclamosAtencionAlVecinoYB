import plotly.express as px
import streamlit as st
from data import run_query

st.write("# Yerba Buena, Tucuman: Datasets")

tab1, tab2 = st.tabs(["Perdida de Agua", "-"])


with tab1:
    df = run_query("SELECT * FROM `project-reclamos-yb.dataset_yb.vw_perdida_agua`")

    unique_AnioMes = df["AnioMes"].unique().tolist()

    st.write("## Perdida de Agua")

    options = st.multiselect(
        "Selecciona Periodo/s",
        unique_AnioMes,
        unique_AnioMes[0],
    )

    filtered_df = df[df["AnioMes"].isin(options)]

    st.divider()
    st.dataframe(filtered_df)

    fig = px.bar(
        filtered_df,
        x="Barrio",
        y="Cantidad",
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
