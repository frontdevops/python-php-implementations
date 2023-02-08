from lxml import html

def strip_tags(html):
    return html.text_content()
 
