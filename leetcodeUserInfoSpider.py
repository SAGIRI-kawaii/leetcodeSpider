# coding = utf-8
import requests
import json

def getUserInfo(userSlug):
    url = "https://leetcode-cn.com/graphql/"
    headers = {
        "origin": "https://leetcode-cn.com",
        "referer": "https://leetcode-cn.com/u/%s/"%userSlug,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN",
        "x-definition-name": "userProfilePublicProfile",
        "x-operation-name": "userPublicProfile",
        "content-type": "application/json"
    }
    payload = {
        'operationName': "userPublicProfile",
        "query":"query userPublicProfile($userSlug: String!) {\n  userProfilePublicProfile(userSlug: $userSlug) {\n    username,\n    haveFollowed,\n    siteRanking,\n    profile {\n      userSlug,\n      realName,\n      aboutMe,\n      userAvatar,\n      location,\n      gender,\n      websites,\n      skillTags,\n      contestCount,\n      asciiCode,\n      medals {\n        name,\n        year,\n        month,\n        category,\n        __typename,\n      }\n      ranking {\n        rating,\n        ranking,\n        currentLocalRanking,\n        currentGlobalRanking,\n        currentRating,\n        ratingProgress,\n        totalLocalUsers,\n        totalGlobalUsers,\n        __typename,\n      }\n      skillSet {\n        langLevels {\n          langName,\n          langVerboseName,\n          level,\n          __typename,\n        }\n        topics {\n          slug,\n          name,\n          translatedName,\n          __typename,\n        }\n        topicAreaScores {\n          score,\n          topicArea {\n            name,\n            slug,\n            __typename,\n          }\n          __typename,\n        }\n        __typename,\n      }\n      socialAccounts {\n        provider,\n        profileUrl,\n        __typename,\n      }\n      __typename,\n    }\n    educationRecordList {\n      unverifiedOrganizationName,\n      __typename,\n    }\n    occupationRecordList {\n      unverifiedOrganizationName,\n      jobTitle,\n      __typename,\n    }\n    submissionProgress {\n      totalSubmissions,\n      waSubmissions,\n      acSubmissions,\n      reSubmissions,\n      otherSubmissions,\n      acTotal,\n      questionTotal,\n      __typename\n    }\n    __typename\n  }\n}",
        'variables': '{"userSlug": "%s"}'%userSlug
    }
    dataJson = requests.post(url=url, headers=headers, data=json.dumps(payload)).json()
    return dataJson
    
if __name__ == "__main__":
    userData = getUserInfo("test")
    print(userData)
