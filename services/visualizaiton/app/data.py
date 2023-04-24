import pandas as pd
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)


@st.cache_data(ttl=600)
def run_query(query) -> pd.DataFrame:
    query_job = client.query(query)
    rows_raw = query_job.result()
    pre_rows = [dict(row) for row in rows_raw]
    return pd.DataFrame(pre_rows)
