import pandas as pd

def load_covid_data(path, country="Germany"):
    """
    Load dan preprocessing dataset COVID-19 Kaggle.
    """
    df = pd.read_csv(path)

    # Standarisasi nama kolom
    df.rename(columns={
        "Country/Region": "Country",
        "Province/State": "Province"
    }, inplace=True)

    df = df[df["Country"] == country]

    # Agregasi jika ada provinsi
    df = df.groupby("Date")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()

    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    # Kasus aktif
    df["Active"] = df["Confirmed"] - df["Recovered"] - df["Deaths"]

    return df
