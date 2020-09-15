# coding = utf-8
import re
from html import unescape

# html格式转纯文字，返回str
def htmlToPlainText(html):
    text = re.sub('<head.*?>.*?</head>', '', html, flags=re.M | re.S | re.I)
    text = re.sub('<a\s.*?>', ' HYPERLINK ', text, flags=re.M | re.S | re.I)
    text = re.sub('<.*?>', '', text, flags=re.M | re.S)
    text = re.sub(r'(\s*\n)+', '\n', text, flags=re.M | re.S)
    return unescape(text)
    
# 含有img标签的html格式转纯文字
def imageInHtmlToText(content):
    images = re.findall(r'<img.*?src="(.*?)".*?>',content,re.S)
    for i in range(len(images)):
        content = content.replace(images[i],"/>ImAgEiMaGe%dImAgE<img"%i)
    transformed = htmlToPlainText(content)
    transformed = transformed.split("ImAgE")
    return (transformed,images)
