import requests
from datetime import datetime, timedelta

def get_week_ago_date():
    raw_week_ago_date = datetime.now() - timedelta(weeks = 1)
    formated_week_ago_date = raw_week_ago_date.strftime('%Y-%m-%d')
    return formated_week_ago_date

def get_trending_repositories(top_size=20):
    repo_query_url = 'https://api.github.com/search/repositories'
    query_parameters = {'q':'created:>{}'.format(get_week_ago_date()),
                        'language': 'python',
                        'sort':'stars',
                        'order':'desc',
                        'per_page': top_size}
    try:
        repo_responce = requests.get(repos_query_url, params = query_parameters)
    except requests.exceptions.RequestException:
        repo_responce = None
    if repo_responce is not None:
        return repo_responce.json().get('items')
        
def get_open_issues_amount(repo_owner, repo_name):
    issue_query_url = 'https://api.github.com/repos/{}/{}/issues'
                                                    .format(repo_owner, repo_name)
    try:
        issue_responce = request.get(issue_query_url)
    except requests.exceptions.RequestException:
        issue_responce = None
    if issue_responce is not None:
        return len(issue_responce.json())

if __name__ == '__main__':
    top_repos_data = get_trending_repositories()
    if top_repos_data:
        print('Hey! Here are the most popular Python projects for the last week on GitHub.'/n)  
        for repo_count, repo_data in enumerate(top_repos_data, start = 1):
            print('''
{}. Repository name: {}
    Stars count: {}
    Description: {}
    Issues count: {}
    Link: {}'''.format(repo_count, repo_data.get('name'),
                       repo_data.get('stargazers_count'),
                       repo_data.get('description'),
                       get_open_issues_amount(repo_data.get('owner').get('login'), repo_data.get('name')),
                       repo_data.get('html_url')))
