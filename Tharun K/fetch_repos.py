import urllib.request
import json

url = "https://api.github.com/users/tharun-1605/repos?per_page=100&sort=updated"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    repos = []
    for repo in data:
        if not repo['fork']:
            repos.append({
                'name': repo['name'],
                'description': repo['description'] or 'No description provided.',
                'url': repo['html_url'],
                'language': repo['language'] or 'Unknown'
            })
    
    with open('repos.json', 'w') as f:
        json.dump(repos, f, indent=2)
    print(f"Fetched {len(repos)} repositories.")
except Exception as e:
    print(f"Error: {e}")
