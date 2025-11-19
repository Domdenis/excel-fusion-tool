import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Fusion de fichiers Excel", layout="wide")

st.title("🧬 Outil de fusion Excel agnostique")

# === Étape 1 : Upload des fichiers ===
file_base = st.file_uploader("📄 Fichier source (base à enrichir)", type=["xlsx"], key="base")
file_enrich = st.file_uploader("➕ Fichier d'enrichissement", type=["xlsx"], key="enrich")

if file_base and file_enrich:
    df_base = pd.read_excel(file_base)
    df_enrich = pd.read_excel(file_enrich)

    # Nettoyage des noms de colonnes
    df_base.columns = df_base.columns.str.strip().str.replace(r'[\r\n]+', '', regex=True).str.lower()
    df_enrich.columns = df_enrich.columns.str.strip().str.replace(r'[\r\n]+', '', regex=True).str.lower()

    st.success("✅ Fichiers chargés avec succès.")
    
    # === Étape 2 : Choix des colonnes de clé ===
    st.subheader("🔑 Clé de fusion")
    st.write("Sélectionnez les colonnes qui constitueront la clé de fusion dans **chaque fichier**.")
    col1, col2 = st.columns(2)

    with col1:
        base_keys = st.multiselect("Clés dans le fichier source", df_base.columns.tolist(), key="key_base")
    with col2:
        enrich_keys = st.multiselect("Clés dans le fichier d'enrichissement", df_enrich.columns.tolist(), key="key_enrich")

    if len(base_keys) == len(enrich_keys) and len(base_keys) > 0:
        # Création de la clé de fusion
        df_base["fusion_id"] = df_base[base_keys].astype(str).apply(lambda row: ''.join(row).strip().lower(), axis=1)
        df_enrich["fusion_id"] = df_enrich[enrich_keys].astype(str).apply(lambda row: ''.join(row).strip().lower(), axis=1)

        # === Étape 3 : Sélection des colonnes à importer ===
        st.subheader("🧲 Colonnes à importer depuis le fichier d’enrichissement")
        enrich_columns = [col for col in df_enrich.columns if col not in enrich_keys and col != "fusion_id"]
        selected_columns = st.multiselect("Colonnes à importer", enrich_columns)

        if selected_columns:
            df_enrich_filtered = df_enrich[["fusion_id"] + selected_columns].drop_duplicates(subset="fusion_id")

            # === Étape 4 : Nom du fichier de sortie ===
            base_filename = file_base.name.replace(".xlsx", "")
            default_filename = f"{base_filename}_enrichi.xlsx"
            output_filename = st.text_input("📝 Nom du fichier de sortie", value=default_filename)

            # === Étape 5 : Fusion ===
            if st.button("🚀 Lancer la fusion"):
                df_merged = pd.merge(df_base, df_enrich_filtered, on="fusion_id", how="left")
                df_merged.drop(columns=["fusion_id"], inplace=True)

                output = BytesIO()
                df_merged.to_excel(output, index=False)
                output.seek(0)

                st.success("✅ Fusion terminée avec succès.")
                st.download_button(
                    label="📥 Télécharger le fichier fusionné",
                    data=output,
                    file_name=output_filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.info("Veuillez sélectionner au moins une colonne à importer.")
    elif len(base_keys) != len(enrich_keys):
        st.warning("Veuillez sélectionner le **même nombre de colonnes** de chaque côté pour la clé de fusion.")
