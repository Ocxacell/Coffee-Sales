import polars as pl 

def clean_data(df):
    for col in df.columns:
        if df[col].dtype == pl.string:
            df = df.with_columns(pl.col(col).str.strip())
        if df[col].dtype == pl.Float64 or df[col].dtype == pl.Int64:
            df = df.with_columns(pl.col(col).fill_null(0))
    return df