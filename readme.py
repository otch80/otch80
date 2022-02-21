import feedparser, datetime

git_blog_rss_uri="https://otch80.github.io/feed.xml"
rss_feed = feedparser.parse(git_blog_rss_uri)

MAX_POST_NUM = 5

front_markdown_text = """


<div align="center">


# Hi, I'm MinGyu👋

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fotch80&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


## Blog

<a href="https://otch80.github.io/" target="_blank"><img src="https://img.shields.io/badge/otch's Blog-<COLOR CODE>?style=flat-square&logo=<ICON>&logoColor=white"/></a>

### 🔥Latest Blog Post🔥
"""

back_markdown_text = """

## Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=Node.js&logoColor=white"/> <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=flat-square&logo=Spring Boot&logoColor=white"/> <img src="https://img.shields.io/badge/java-007396?style=flat-square&logo=Spring Boot&logoColor=white"/> 

<br>
<br>
  
![trophy](https://github-profile-trophy.vercel.app/?username=otch80)

<br>
<br>

[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=otch80&theme=gruvbox)](https://github.com/anuraghazra/github-readme-stats) [![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=otch80&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

</div>



"""


j=0
for i, feed in enumerate(rss_feed['entries']):
    if i > 5:
        break
    else:
        dt = feed['published']
        # markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
        front_markdown_text += f"[{feed['title']}]({feed['link']}) <br>\n"

front_markdown_text += back_markdown_text
print(front_markdown_text)
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()  
