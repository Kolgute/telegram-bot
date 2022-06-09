from open_file import *
from parse import *

# Get product reviews
def take_reviews():
    imtId_list = take_list_from_file()
    feedbacks = []
    for id in imtId_list:
        review = []
        root_id = search_rootId(id)
        answer = get_feedback(root_id)
        for item in answer:
            review.append(item)
        feedbacks.append(review)
    return feedbacks


# Converting the response from the server to a user-friendly form
def convertor_list_str(feedbacks):
    reviews = []
    for items in feedbacks:
        for answer in items:
            text = "negative feedback\n"
            text = (
                text
                + answer["productName"]
                + "\nID product - "
                + str(answer["imtId"])
                + "\nProduct evaluation - "
                + str(answer["productValuation"])
                + "\n"
                + answer["text"]
            )
            reviews.append(text)
    return reviews
