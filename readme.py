import feedparser, datetime

git_blog_rss_uri="https://otch80.github.io/feed.xml"
rss_feed = feedparser.parse(git_blog_rss_uri)

MAX_POST_NUM = 10

latest_blog_post_list = ""


for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = "##🔥🔥Latest Blog Post\n"

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
