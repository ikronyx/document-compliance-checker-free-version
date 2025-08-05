# Handles export of results
import pandas as pd
from io import BytesIO, StringIO

def to_csv(df):
    return df.to_csv(index=False)

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()
