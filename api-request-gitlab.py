import requests

response=requests.get("https://gitlab.com/api/v4/users/techworld-with-nana/projects")
my_project=response.json()

for project in my_project:
    print(f"Project Name: {project['name']} | Project URL: {project['web_url']}\n")