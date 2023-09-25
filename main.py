import requests
from email_class import Gmail
from datetime import datetime

api_key = 'pub_30091dbab20ef77b69300a7c5038dd9d163d5'
url = "https://newsdata.io/api/1/news?"\
       f"apikey={api_key}"\
       "&language=en"

# make a request
request = requests.get(url)
# get a dict with data
content = request.json()['results']

# get a title and a description
body = ''
for article in content[:5]:
    if article['description'] is not None:
        body = body + article['description'] + '\n' + article['content'] + '\n' + article['link'] + 2*'\n'

#body = body.encode('utf-8')
# send news to my email
today_date = datetime.today().strftime('%d.%m.%Y')
Gmail('neonrobot9@gmail.com', 'pash ggce smtl hxzi ').send_email(f'News vom {today_date}', body)




