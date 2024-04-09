# %% [markdown]
# Exercise 0: 
# 
# Please write a function that takes no arguments and returns a link to your solutions on GitHub.

# %%
def github() -> str:
    """
    arguments: none
    returns: a link to your solutions on GitHub.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps2.py"
github()

# %% [markdown]
# Exercise 1: 
# 
# Please write a function that returns 1000 simulated observations via the following data generating process:
# 
# 
# In particular, your function should take one argument, seed, an integer that is used to set a seed (this should default to 481 if not provided), and should return a tuple of two elements, (y,X) where y is a (1000, 1) np.array and X is a (1000, 3) np.array 

# %%
import numpy as np
def simulate_data(seed: int = 481) -> tuple:
    """
    arguments: an integer seed
    returns: 1000 simulated observations in the form of a (y, X) tuple
    where where y is a (1000, 1) np.array and X is a (1000, 3) np.array 
    """
    np.random.seed(seed)
        
    X = np.random.normal(loc= 0, scale= 2, size=(1000, 3))
    e = np.random.normal(loc= 0, scale= 1, size=(1000, 1))
    y = 5 + 3 * X[:, 0] + 2 * X[:, 1] + 6 * X[:, 2] + e[:, 0]
    y = y.reshape((-1, 1))
    return (y, X)

y, X = simulate_data()
y.shape, X.shape


# %% [markdown]
# Exercise 2: 
# 
# Write a function that estimates the MLE parameters for data simulated as above
# 
# In particular, your function should take as arguments a (1000, 1) np.array y and a (1000, 3) np.array X and return a (4, 1) np.array with the coefficients.

# %%
import numpy as np
from scipy.optimize import minimize

def log_likelihood(parameters, y, X) :
    """
    arguments: parameters, y and X to do log likelihood estimation on
    returns: the log likelihood function to minimize
    """
    parameters = np.array(parameters).reshape((-1, 1))
    N = X.shape[0]
    X_with_intercept = np.hstack((np.ones((X.shape[0], 1)), X))
    
    
    # Calculate predicted values
    y_pred = np.matmul(X_with_intercept, parameters)
    residuals = y - y_pred
    ll = N * 0.5 * (np.log(2 * np.pi)) + 0.5 * np.sum(residuals**2)
    return ll

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    arguments: data y and X representing observations
    returns: MLE estimates of the parameters
    """
    parameters = [0] * (X.shape[1] + 1)
    result = minimize(log_likelihood, x0 = parameters, args=(y, X), method= 'Nelder-Mead')   
    return result.x.reshape((-1, 1))
    
estimate_mle(y, X)

# %% [markdown]
# Exercise 3: 
# 
# Write a function to estimate the OLS coefficients for the simulated data, with a catch: do not use the closed-form solution
# 
# In particular, your function should take as arguments a (1000, 1) np.array y and a (1000, 3) np.array X and return a (4, 1) np.array with the coefficients.

# %%
import numpy as np
from scipy.optimize import minimize

def sum_of_squared_residuals(parameters, y, X) :
    """
    arguments: parameters, y and X to do OLS estimation on
    returns: the sum of squared residuals to minimize 
    """
    parameters = np.array(parameters, dtype=np.float64)
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    parameters = parameters.reshape((-1, 1))
    
    # Calculate predicted values
    y_pred = np.matmul(X, parameters)

    # Calculate error term (residuals)
    residuals = y - y_pred

    # Calculate and return the sum of residuals
    ssr = np.sum(residuals ** 2)
    return ssr

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    arguments: data y and X representing observations
    returns: OLS estimates of the parameters
    """
    parameters = [0] * (X.shape[1] + 1)
    min = -99999999999999
    max = 99999999999999
    bounds = ((min, max), (min, max), (min, max), (min, max))
    result = minimize(sum_of_squared_residuals, x0 = parameters, bounds = bounds, args=(y, X))
    return result.x.reshape((-1, 1))
    
estimate_ols(y, X)


