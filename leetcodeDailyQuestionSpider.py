# coding = utf-8
"""
需配合leetcodeQuestionContentSpider使用
使用示例：
dailyQuestionData = getDailyQuestionJson()
questionTitleSlug = dailyQuestionData["data"]["todayRecord"][0]["question"]["questionTitleSlug"]
content = getQuestionContent(questionTitleSlug,"Zh")
print(content)
"""

def getDailyQuestionJson():
    url = "https://leetcode-cn.com/graphql/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "302",
        "content-type": "application/json",
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/problemset/all/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    payload = {
        "operationName":"questionOfToday",
        "variables":{},
        "query":"query questionOfToday {\n  todayRecord {\n    question {\n      questionFrontendId,\n      questionTitleSlug,\n      __typename\n    }\n    lastSubmission {\n      id,\n      __typename,\n    }\n    date,\n    userStatus,\n    __typename\n  }\n}\n"
    }
    dataJson = requests.post(url=url, headers=headers, data=json.dumps(payload)).json()
    return dataJson
