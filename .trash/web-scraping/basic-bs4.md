---
aliases: 
tags: 
date created: Saturday, August 12th 2023, 8:37:32 pm
date modified: Saturday, August 12th 2023, 8:39:11 pm
---
```python
import requests
import contextlib
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
with open("output.html", "a") as f:
  print(r.content, file=f)
```

[Implementing Web Scraping in Python with BeautifulSoup - GeeksforGeeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
