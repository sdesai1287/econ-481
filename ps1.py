# %% [markdown]
# Exercise 0
# Please write a function that takes no arguments and returns a link to your solutions on GitHub.
# 

# %%
def github() -> str:
    """
    arguments: none
    returns: a link to your solutions on GitHub.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps1.py"

github()

# %% [markdown]
# Exercise 1
# Please ensure that you can run python1, can use Git, and install the following packages2 (we’ll install more as we go):
# 
# numpy
# pandas
# scipy
# matplotlib
# seaborn

# %%
# %pip install numpy
# %pip install pandas
# %pip install scipy
# %pip install matplotlib
# %pip install seaborn

# %% [markdown]
# Exercise 2
# Please write a function called evens_and_odds that takes as argument a natural number n and returns a dictionary with two keys, “evens” and “odds”. “evens” should be the sum of all the even natural numbers less than n, and “odds” the sum of all natural numbers less than n.
# 
# For example, evens_and_odds(4) should return
# 
# {'evens': 2, 'odds': 4}

# %%
def evens_and_odds(n: int) -> dict:
    """
    arguments: a natural number n
    returns: a dictionary with two keys, “evens” and “odds”. “evens” should be the sum of all the even natural numbers less than n, and “odds” the sum of all odd natural numbers less than n.
    For example, evens_and_odds(4) should return
    {'evens': 2, 'odds': 4}.
    """
    evenSum = 0
    oddSum = 0
    output = {'evens' : evenSum, 'odds' : oddSum}
    for i in range(n) :
        if (i % 2 == 0) :
            evenSum += i
        else :
            oddSum += i
    output['evens'] = evenSum
    output['odds'] = oddSum
    return output

evens_and_odds(4)

# %% [markdown]
# Exercise 3
# Please write a function called time_diff that takes as arguments two strings in the format ‘YYYY-MM-DD’ and a keyword out dictating the output. If the keyword is “float”, return the time between the two dates (in absolute value) in days. If the keyword is “string”, return “There are XX days between the two dates”. If not specified, the out keyword should be assumed to be “float”. You should use the datetime package, and no others.
# 
# For example, time_diff('2020-01-01', '2020-01-02', 'float') should return
# 
# 1
# For example, time_diff('2020-01-03', '2020-01-01', 'string') should return
# 
# "There are 2 days between the two dates"

# %%
from datetime import datetime
from typing import Union

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    arguments: two strings in the format ‘YYYY-MM-DD’ and a keyword out dictating the output
    returns: If the keyword is “float”, return the time between the two dates (in absolute value) in days. If the keyword is “string”, return “There are XX days between the two dates”. If not specified, the out keyword should be assumed to be “float”
    """
    date_format = "%Y-%m-%d"
    try :
        d1 = datetime.strptime(date_1, date_format)
        d2 = datetime.strptime(date_2, date_format)
    except ValueError :
        return "Date inputs are not in the correct format, please try again!"

    days = abs(d2 - d1).days
    if (out == 'string') :
        return 'There are ' + str(days) + ' days between the two dates'
    else :
        return days
    
print(time_diff('2020-01-01', '2020-01-02', 'float'))
print(time_diff('2020-01-03', '2020-01-01', 'string'))


# %% [markdown]
# Exercise 4
# Please write a function called reverse that takes as its argument a list and returns a list of the arguments in reverse order (do not use any built-in sorting methods).
# 
# For example, reverse(['a', 'b', 'c']) should return
# 
# ['c', 'b', 'a']

# %%
def reverse(in_list: list) -> list:
    """
    arguments: a list
    returns: a list of the arguments in reverse order
    Note: could do this with 'return in_list[::-1]'
    """
    output = []
    n = len(in_list)
    for i in range(n - 1, -1, -1) :
        output.append(in_list[i])
    return output

reverse(['a', 'b', 'c'])

# %% [markdown]
# Exercise 5
# Write a function called prob_k_heads that takes as its arguments natural numbers n and k with n>k and returns the probability of getting k heads from n flips.
# 
# For example, prob_k_heads(1,1) should return 0.5

# %%
import numpy as np
def prob_k_heads(n: int, k: int) -> float:
    """
    arguments: natural numbers n and k representing total flips and heads desired
    return: probability of getting exactly k heads from n flips
    Notes: could apply math.comb(n, k) for nCk
    """
    
    nCk = int(np.prod(np.arange(k + 1, n + 1)) / np.prod(np.arange(1, n - k + 1)))
    p = (0.5 ** n) * nCk
    return p

prob_k_heads(1,1)


