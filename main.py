import feedparser
import json
import os

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
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    rss_urls = {
        'LeFigaro': 'https://www.lefigaro.fr/rss/figaro_actualites.xml',
        # Add more RSS URLs here
    }

    for source, url in rss_urls.items():
        data = fetch_rss_data(url)
        save_to_file({source: data}, f"{source}.json")

if __name__ == '__main__':
    main()
