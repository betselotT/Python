import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.concat([df1, df2], ignore_index=False, sort=False)
    return df_merged