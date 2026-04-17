import streamlit as st
import pandas as pd
import tempfile
import os
from motor import generar_proyecto

st.set_page_config(page_title="BI Generator", page_icon="📊", layout="centered")
st.title("📊 BI Generator")
st.caption("Sube tu Excel y genera un proyecto Power BI listo para abrir.")

necesidad = st.text_input("¿Qué necesitas analizar?", placeholder="Ej: ventas por mes y por vendedor")
archivo   = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if archivo:
    # Mostrar preview de hojas y columnas detectadas
    xl = pd.ExcelFile(archivo)
    st.success(f"✅ {len(xl.sheet_names)} hoja(s) detectada(s): {', '.join(xl.sheet_names)}")

    with st.expander("Ver columnas detectadas"):
        for sheet in xl.sheet_names:
            df = xl.parse(sheet, nrows=3)
            st.markdown(f"**{sheet}** — {len(df.columns)} columnas")
            st.dataframe(df, use_container_width=True)

    st.markdown("**Visuales que se generarán automáticamente:**")
    for sheet in xl.sheet_names:
        df_full = xl.parse(sheet, nrows=0)
        numerics  = [c for c in df_full.columns if pd.api.types.is_numeric_dtype(df_full[c].dtype) or str(df_full[c].dtype) in ("int64","float64")]
        dates     = [c for c in df_full.columns if "datetime" in str(df_full[c].dtype)]
        cats      = [c for c in df_full.columns if df_full[c].dtype == object]
        items = [f"📋 Tabla con todas las columnas de **{sheet}**"]
        if cats and numerics:
            items.append(f"📊 Barras: {cats[0]} × {numerics[0]}")
        if dates and numerics:
            items.append(f"📈 Líneas: {dates[0]} × {numerics[0]}")
        for item in items:
            st.write(f"- {item}")

if st.button("⚡ Generar proyecto Power BI", type="primary", disabled=archivo is None):
    with st.spinner("Generando..."):
        # Guardar Excel en un archivo temporal con nombre original
        suffix = os.path.splitext(archivo.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(archivo.getbuffer())
            tmp_path = tmp.name

        zip_path = generar_proyecto(necesidad, tmp_path)
        os.unlink(tmp_path)

    st.success("🎉 ¡Proyecto generado!")
    st.info("💡 **Instrucciones:** Descarga el ZIP → descomprímelo → abre `proyecto.pbip` con Power BI Desktop → clic en **Actualizar** para cargar los datos.")

    with open(zip_path, "rb") as f:
        st.download_button(
            label="⬇️ Descargar proyecto_pbip.zip",
            data=f,
            file_name="proyecto_pbip.zip",
            mime="application/zip",
            type="primary"
        )
