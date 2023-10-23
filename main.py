import feedparser
import json
import os
from datetime import datetime

def fetch_rss_data(url):
    feed = feedparser.parse(url)
    entries = []
    for entry in feed.entries:
        entries.append({
            'title': entry.title,
            'summary': entry.summary,
            'link': entry.link
        })
    return entries

def save_to_file(data, filename):
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", filename), 'w') as f:
        json.dump(data, f, indent=4)

def read_existing_data(filename):
    filepath = os.path.join("data", filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return []

def main():
    rss_urls = {
        'LeFigaro': 'https://www.lefigaro.fr/rss/figaro_actualites.xml',
        'LeMonde': 'https://www.lemonde.fr/en/rss/une.xml',
        # Add more RSS URLs here
    }

    for source, url in rss_urls.items():
        today = datetime.now().strftime("%Y%m%d")
        filename = f"{source}_{today}.json"
        
        existing_data = read_existing_data(filename)
        existing_links = [entry['link'] for entry in existing_data]

        new_data = fetch_rss_data(url)
        updated_data = existing_data + [entry for entry in new_data if entry['link'] not in existing_links]

        save_to_file(updated_data, filename)

if __name__ == '__main__':
    main()
