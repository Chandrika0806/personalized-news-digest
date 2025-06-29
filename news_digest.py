import requests
import json
from email.mime.text import MIMEText
import smtplib
from datetime import date

# ✅ Replace with your real NewsAPI key
API_KEY = 'a85520c611194e80a7e989fad1db00b3'  # 🔐 Replace this with your real NewsAPI key
NEWS_URL = 'https://newsapi.org/v2/top-headlines'

# ✅ Function to get news for a category
def get_news(category):
    params = {
        'apiKey': API_KEY,
        'category': category,
        'country': 'us',    # Use 'us' for more reliable results
        'pageSize': 5
    }
    response = requests.get(NEWS_URL, params=params)
    articles = response.json().get('articles', [])
    return [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]

# ✅ Function to send email using Gmail + App Password
def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'chandrikanarne45@gmail.com'       # ← Your Gmail
    msg['To'] = to

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('chandrikanarne45@gmail.com', 'slifjsxtvfmvmtid')  # ← Your Gmail App Password
        server.send_message(msg)

# ✅ Load users from JSON
with open('users.json') as f:
    users = json.load(f)

today = date.today().strftime('%B %d, %Y')  # Example: June 29, 2025

# ✅ Loop through users and send them their digest
for user in users:
    category = user.get('category', 'general')
    headlines = get_news(category)

    if not headlines:
        print(f"⚠️ No headlines found for '{category}'")
        continue

    body = (
        f"Hi {user['name']},\n\n"
        f"As someone who follows **{category.title()}**, here are your top news headlines for {today}:\n\n"
        + "\n".join(headlines)
        + f"\n\nStay informed and have a great day!\n\n— Your News Digest Bot"
    )

    subject = f"Your {category.title()} News Digest – {today}"
    send_email(user['email'], subject, body)
    print(f"✅ Sent news to {user['email']}")
