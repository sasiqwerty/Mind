---
aliases: 
tags: 
date created: Thursday, August 31st 2023, 12:57:36 pm
date modified: Thursday, August 31st 2023, 1:00:05 pm
---
```python
import markdown

with open('Picnic.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('Picnic.html', 'w') as f:
    f.write(html)
```
