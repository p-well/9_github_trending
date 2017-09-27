import requests
from datetime import datetime, timedelta

def get_week_ago_date():
    raw_week_ago_date = datetime.now() - timedelta(weeks = 1)
    formated_week_ago_date = raw_week_ago_date.strftime('Y%-%m-%d')
    return formated_week_ago_date

def get_trending_repositories(top_size=20):
    query_url = https://api.github.com/search/repositories
    query_parameters = {'q':'created:>{}'.format(get_week_ago_date()),
                        'language': 'python',
                        'sort':'stars',
                        'order':'desc',
                        'per_page': top_size}
    try:
        github_responce = requests.get(query_url, params = query_parameters)
    except requests.exceptions.ConnectionError:
        github_responce = None
    if github_responce is not None:
    


def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
pass

https://api.github.com/search/repositories?q=created:%3E2017-09-20+language:python&sort=stars&order=desc&per_page=20

