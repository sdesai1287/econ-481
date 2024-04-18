# %%
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps3.py"

github()

# %%
import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    df = pd.DataFrame()
    for y in years :
        df_temp = pd.read_excel(f'https://lukashager.netlify.app/econ-481/data/ghgp_data_{y}.xlsx', sheet_name='Direct Emitters', skiprows=3)
        df_temp['year'] = y
        df = pd.concat([df, df_temp])
    return df

# %%
import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    df = pd.DataFrame()
    for y in years :
        df_temp = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb', sheet_name=str(y)).dropna(how='all')
        df_temp['year'] = y
        df = pd.concat([df, df_temp])
    return df

# %%
e = import_yearly_data([2022])
p = import_parent_companies([2022])

# %%
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Some docstrings
    """
    
    return len(df) - df[col].count()
n_null(e, 'FRS Id')

# %%
def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Some docstrings.
    """
    df = pd.merge(emissions_data, parent_data, left_on=['Facility Id', 'year'], right_on=['GHGRP FACILITY ID', 'year'])
    df = df[['Facility Id', 'year', 'State', 'Industry Type (sectors)', 'Total reported direct emissions', 'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]
    df.columns = df.columns.str.lower()
    return df
c = clean_data(e, p)
c

# %%
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    stats = ['min', 'median', 'mean', 'max']
    df = df.groupby(group_vars).agg({
        'total reported direct emissions': stats,
        'parent co. percent ownership': stats
    }).sort_values(by=('total reported direct emissions', 'mean'), ascending=False)
            
    return df
aggregate_emissions(c, ['state'])



