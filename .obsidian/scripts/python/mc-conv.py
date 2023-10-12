import markdown
import re
import webbrowser

def process_text(text):
    # Completely delete patterns like ![[Zoom_vG02SsRNBO.png]]
    text = re.sub(r'!\[\[[^\]]+\]\]', '', text)
    
    # Replace [[any words or words]] with any words or words
    text = re.sub(r'\[\[([\w\s]+)\]\]', r'\1', text)
    
    # Replace [[any words before | any words after]] with any words after
    text = re.sub(r'\[\[[^\|]+\|([^\]]+)\]\]', r'\1', text)
       
    return text

with open('conv-file.md', 'r') as f:
    text = f.read()
    ptext = process_text(text)
    html = markdown.markdown(ptext)
  
output_file = 'converted.html'
with open('converted.html', 'w') as f:
    f.write(html)

# Open the converted HTML in the default browser
webbrowser.open(output_file)
