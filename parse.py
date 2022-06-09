from datetime import datetime
import requests

# Get product reviews by rootID
def get_feedback(rootId):
    list_answer = []
    raw_data = {"imtId": rootId, "skip": 0, "take": 5, "order": "dateDesc"}
    url = "https://public-feedbacks.wildberries.ru/api/v1/feedbacks/site"
    response = requests.post(
        url=url, headers={"Content-Type": "application/json"}, json=raw_data
    )
    response_message = response.json()
    for items in response_message["feedbacks"]:
        # Convert date to desired form
        time = items["createdDate"].replace("-", "/").replace("T", " ").replace("Z", "")
        time = datetime.strptime(time, "%Y/%m/%d %H:%M:%S")
        now_day = datetime.today().strftime("%Y/%m/%d")
        review_day = time.strftime("%Y/%m/%d")
        # Revocation Date Check
        if (
            datetime.strptime(now_day, "%Y/%m/%d")
            - datetime.strptime(review_day, "%Y/%m/%d")
        ) != 0: # if you need change date check, change this value ( ==0 - today| !=0 not todaty| <0 yesterday)
            # Embedding a dictionary with the required data in a list
            if items["productValuation"] != 5:
                dict_answer = {}
                dict_answer["text"] = items["text"]
                dict_answer["productValuation"] = items["productValuation"]
                dict_answer["productName"] = items["productDetails"]["productName"]
                dict_answer["imtId"] = items["productDetails"]["nmId"]
                list_answer.append(dict_answer)
    return list_answer


# Getting root Id by product id from the site
def search_rootId(imtId):
    url = (
        "https://card.wb.ru/cards/detail?spp=0&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,48,1,40,71&stores=117673,122258,122259,125238,125239,125240,6159,507,3158,117501,120602,120762,6158,121709,124731,159402,2737,130744,117986,1733,686,132043&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&dest=-1029256,-102269,-1278703,-1255563&nm="
        + str(imtId)
        + ";64245978;64245979%27"
    )
    response = requests.get(url=url)
    response_message = response.json()
    for item in response_message["data"]["products"]:
        if item["id"] == imtId:
            rootId = int(item["root"])

    return rootId
