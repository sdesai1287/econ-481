# %%
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/sdesai1287/econ-481/blob/main/ps5.py"

github()

# %%
import requests
from bs4 import BeautifulSoup

def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            code_snippets = soup.find_all('code')
            python_code = []
            for code_snippet in code_snippets:
                if 'class' in code_snippet.attrs and 'python' in code_snippet['class']:
                    code_lines = code_snippet.get_text().split('\n')
                    filtered_code = [line for line in code_lines if not line.strip().startswith('%')]
                    for item in filtered_code :
                        python_code.append(''.join(item))
            formatted_code = '\n'.join(python_code)
            return formatted_code
        else:
            return "Failed to fetch webpage (Status code: {})".format(response.status_code)
    except Exception as e:
        return "Error: {}".format(str(e))

# Test the function
url = "https://lukashager.netlify.app/econ-481/01_intro_to_python"
print(scrape_code(url))


