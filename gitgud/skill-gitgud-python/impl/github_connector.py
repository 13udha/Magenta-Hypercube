import requests

GITHUB_API_URL = "https://api.github.com/repos/"
GITHUB_PROJECT_URI = "13udha/Magenta-Hypercube"


def get_github_stats():
    url = GITHUB_API_URL
    url += GITHUB_PROJECT_URI if not GITHUB_PROJECT_URI.startswith('/') else GITHUB_PROJECT_URI.split('/',1)[-1]
    try:
        raw = requests.get(url)
        raw.raise_for_status()
        stats = raw.json()['description']
        print(stats)
    except Exception as err:
        print(err)
        return False, err
    return True, stats