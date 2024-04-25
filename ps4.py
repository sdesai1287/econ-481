# %%
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps4.py"

github()

# %%
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Some docstrings.
    """
    df = pd.read_csv('https://lukashager.netlify.app/econ-481/data/TSLA.csv')
    return df
df = load_data()
df

# %%
import matplotlib.pyplot as plt
def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """
    filtered_data = df[df['Date'] >= start]
    filtered_data = filtered_data[filtered_data['Date'] <= end]
    plt.figure(figsize=(10, 7))
    plt.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-')
    plt.title(f"Closing Price ({start} to {end})")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
plot_close(df)

# %%
import statsmodels.api as sm
from datetime import timedelta
def autoregress(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    new_df = df.set_index('Date')
    new_df.index = pd.to_datetime(new_df.index)
    new_df = new_df.sort_values(by='Date')
    new_df['Close_diff'] = new_df['Close'].diff()
    new_df['Close_diff_shifted'] = new_df['Close_diff'].shift(1, freq=timedelta(1))
    new_df = new_df.dropna()

    x = new_df['Close_diff']
    y = new_df['Close_diff_shifted']

    model = sm.OLS(y, x).fit(cov_type='HC1')
    t_statistic = model.tvalues[0]

    return t_statistic
autoregress(df)

# %%
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    new_df = df.set_index('Date')
    new_df.index = pd.to_datetime(new_df.index)
    new_df = new_df.sort_values(by='Date')
    new_df['Close_diff'] = new_df['Close'].diff()
    new_df['Close_diff_shifted'] = new_df['Close_diff'].shift(1, freq=timedelta(1))
    new_df = new_df.dropna()
    x = new_df['Close_diff']
    y = (new_df['Close_diff_shifted'] > 0).astype(int)

    model = sm.Logit(y, x).fit(disp=0)

    t_statistic = model.tvalues[0]

    return t_statistic

autoregress_logit(df)

# %%
def plot_delta(df: pd.DataFrame) -> None:
    """
    Some docstrings.
    """
    df = df.sort_values(by='Date')
    df['Delta_Close'] = df['Close'].diff()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Delta_Close'], marker='o', linestyle='-')
    plt.title("Change in Close over time")
    plt.xlabel("Date")
    plt.ylabel("Delta Close")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
plot_delta(df)


