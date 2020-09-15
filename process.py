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

# 文字转图片
def textToImg(texts=[], images=[], size=12, color='black', bg='white'):
    # 可自行更换字体文件
    fnt = ImageFont.truetype('/Users/user/Library/Group Containers/UBF8T346G9.Office/FontCache/4/CloudFonts/STKaiti/34202148807.ttf', size)
    
    mlength = []
    mheight = []
    text = []
    for i in texts:
        if "iMaGe" not in i:
            text += i.split("\n")
            print(text)
        else:
            text.append(i)
            
    length = -1
    for j in text:
        if len(j) > length:
            length = len(j)

    while "" in text:
        text.remove("")

    print(text)
    for i in range(len(text)):
        filename = "./temp/%s.png"%i
        print(filename)
        if "iMaGe" in text[i]:
            img_content=requests.get(images[int(text[i][5])]).content
            image=Image.open(BytesIO(img_content))
            mlength.append(image.width)
            mheight.append(image.height)
            image.save(filename)
            continue

        mlength.append(int(size)*len(text[i]))
        mheight.append(size*2)

        image = Image.new(mode = "RGB", size = (int(size)*len(text[i]),size*2), color = bg)
        draw = ImageDraw.Draw(image)
        draw.text((10,10), text[i], font=fnt, fill='black')
        image.save(filename)
        
    output = Image.new(mode="RGB", size=(max(mlength)+10, sum(mheight)+20), color="white")
    index = 0
    h = 0
    path = os.listdir("./temp")
    path.sort(key=lambda x:int(x[:-4]))
    for i in path:
        output.paste(Image.open("./temp/%s"%i), (10,h))
        h += mheight[index]
        index += 1
        os.remove("./temp/%s"%i)
        
    # output.show()
    output.save("output.png")
