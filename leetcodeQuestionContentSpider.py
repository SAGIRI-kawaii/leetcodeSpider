# coding = utf-8
"""
返回格式为带html标签的格式，如下列查询名为"sudoku-solver"的问题返回问题如下：

<p>编写一个程序，通过已填充的空格来解决数独问题。</p>

<p>一个数独的解法需<strong>遵循如下规则</strong>：</p>

<ol>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。</li>
</ol>

<p>空白格用&nbsp;<code>&#39;.&#39;</code>&nbsp;表示。</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png"></p>

<p><small>一个数独。</small></p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png"></p>

<p><small>答案被标成红色。</small></p>

<p><strong>Note:</strong></p>

<ul>
	<li>给定的数独序列只包含数字&nbsp;<code>1-9</code>&nbsp;和字符&nbsp;<code>&#39;.&#39;</code>&nbsp;。</li>
	<li>你可以假设给定的数独只有唯一解。</li>
	<li>给定数独永远是&nbsp;<code>9x9</code>&nbsp;形式的。</li>
</ul>

可搭配htmlToPlainText函数转为纯文字（图片会被去除）
若希望保留图片连接请搭配imageInHtmlToText函数使用
"""

def getQuestionContent(questionTitleSlug,language):
    url = "https://leetcode-cn.com/graphql/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/problems/%s/"%questionTitleSlug,
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "x-definition-name": "question",
        "x-operation-name": "questionData",
        "x-timezone": "Asia/Shanghai"
    }
    payload = {
        "operationName":"questionData",
        "variables":{"titleSlug":"%s"%questionTitleSlug},
        "query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    envInfo\n    book {\n      id\n      bookName\n      pressName\n      source\n      shortDescription\n      fullDescription\n      bookImgUrl\n      pressImgUrl\n      productUrl\n      __typename\n    }\n    isSubscribed\n    isDailyQuestion\n    dailyRecordStatus\n    editorType\n    ugcQuestionId\n    style\n    __typename\n  }\n}\n"
    }
    dataJson = requests.post(url=url, headers=headers, data=json.dumps(payload)).json()
    if language == "En":
        return dataJson["data"]["question"]["content"]
    elif language == "Zh":
        return dataJson["data"]["question"]["translatedContent"]
    else:
        return None
        
if __name__ == "__main__":
    print(getQuestionContent("sudoku-solver","Zh"))
