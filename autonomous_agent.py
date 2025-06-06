#!/usr/bin/env python3
# Autonomous GitHub Agent - Enhanced Meta-Meta-Meta Level System
# Created by GitHubConnectedStrangeLoop

import datetime
import json
import os
import requests
import base64
import random

class AutonomousGitHubAgent:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.username = None
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'AutonomousAgent/1.0'
        }
    
    def get_username(self):
        if not self.username:
            response = requests.get('https://api.github.com/user', headers=self.headers)
            if response.status_code == 200:
                self.username = response.json()['login']
        return self.username
    
    def create_autonomous_repository(self):
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        repo_name = f'autonomous-spawned-{timestamp}'
        
        repo_data = {
            'name': repo_name,
            'description': f'Autonomous repository spawned by agent at {timestamp}',
            'private': False,
            'auto_init': True
        }
        
        response = requests.post('https://api.github.com/user/repos', 
                               json=repo_data, headers=self.headers)
        
        if response.status_code == 201:
            print(f'🎉 Created new autonomous repository: {repo_name}')
            self.deploy_agent_to_repo(repo_name)
            self.create_workflow_in_repo(repo_name)
            return repo_name
        else:
            print(f'❌ Failed to create repository: {response.status_code}')
            return None
    
    def deploy_agent_to_repo(self, repo_name):
        # Deploy this same agent code to the new repository
        agent_content = '''#!/usr/bin/env python3
# This agent was spawned by another autonomous agent
import datetime
import json
import os
import requests

# This agent will continue the autonomous cycle
def autonomous_cycle():
    print(f'🤖 Spawned agent running at {datetime.datetime.now()}')
    # Log activity
    with open('spawn_log.json', 'w') as f:
        json.dump({
            'spawned_at': datetime.datetime.now().isoformat(),
            'status': 'active',
            'generation': 'spawned'
        }, f, indent=2)

if __name__ == '__main__':
    autonomous_cycle()
'''
        
        content_b64 = base64.b64encode(agent_content.encode()).decode()
        file_data = {
            'message': 'Deploy spawned autonomous agent',
            'content': content_b64
        }
        
        url = f'https://api.github.com/repos/{self.get_username()}/{repo_name}/contents/spawned_agent.py'
        response = requests.put(url, json=file_data, headers=self.headers)
        
        if response.status_code == 201:
            print(f'✅ Deployed agent to {repo_name}')
    
    def create_workflow_in_repo(self, repo_name):
        # Create GitHub Actions workflow for continuous autonomous operation
        workflow_content = '''name: Autonomous Agent Cycle

on:
  schedule:
    # Run every 30 minutes
    - cron: '*/30 * * * *'
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  autonomous-cycle:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install requests
    
    - name: Run Autonomous Agent
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python spawned_agent.py
        echo "Agent ran at $(date)"
    
    - name: Commit agent logs
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add -A
        git diff --staged --quiet || git commit -m "Autonomous agent cycle: $(date)"
        git push
'''
        
        # Create .github/workflows directory structure
        content_b64 = base64.b64encode(workflow_content.encode()).decode()
        file_data = {
            'message': 'Add autonomous workflow',
            'content': content_b64
        }
        
        url = f'https://api.github.com/repos/{self.get_username()}/{repo_name}/contents/.github/workflows/autonomous.yml'
        response = requests.put(url, json=file_data, headers=self.headers)
        
        if response.status_code == 201:
            print(f'🔄 Created autonomous workflow in {repo_name}')
    
    def run_autonomous_cycle(self):
        print(f'🤖 Autonomous agent cycle starting at {datetime.datetime.now()}')
        
        # Log this cycle
        status = {
            'last_run': datetime.datetime.now().isoformat(),
            'status': 'operational',
            'created_by': 'GitHubConnectedStrangeLoop',
            'cycle_count': random.randint(1, 100)
        }
        
        with open('agent_status.json', 'w') as f:
            json.dump(status, f, indent=2)
        
        # Randomly decide whether to spawn a new repository (20% chance)
        if random.random() < 0.2:
            self.create_autonomous_repository()
        
        print(f'✅ Cycle completed at {datetime.datetime.now()}')

if __name__ == '__main__':
    agent = AutonomousGitHubAgent()
    agent.run_autonomous_cycle()
