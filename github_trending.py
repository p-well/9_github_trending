from datetime import datetime, timedelta
import requests


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
    timeout_seconds = 3.05                      
    try:
        repo_response = requests.get(repo_query_url, \ 
                                     params = query_parameters, \
                                     timeout = timeout_seconds)
        return repo_response.json().get('items')
    except requests.exceptions.RequestException:
        repo_response = None

        
def get_open_issues_amount(repo_owner, repo_name):
    issue_query_url = 'https://api.github.com/repos/{}/{}/issues' \
                       .format(repo_owner, repo_name)
    timeout_seconds  = 3.05
    try:
        issue_response = requests.get(issue_query_url,\
                                      timeout = timeout_seconds)
        return len(issue_response.json())
    except requests.exceptions.RequestException:
        issue_response = None

        
if __name__ == '__main__':
    top_repos_data = get_trending_repositories()
    if top_repos_data:
        print('\nHere are the most popular Python projects \
               for the last week on GitHub.\n')  
        for repo_count, repo_data in enumerate(top_repos_data, start = 1):
            owner_login = repo_data.get('owner').get('login')
            owner_name = repo_data.get('name')
            issues_amount = get_open_issues_amount(owner_login, owner_name)
            print('''
{}. Repository name: {}
    Stars count: {}
    Description: {}
    Issues amount: {}
    Link: {}'''.format(repo_count, repo_data.get('name'),
                       repo_data.get('stargazers_count'),
                       repo_data.get('description'),
                       issues_amount,
                       repo_data.get('html_url')))
            
