import requests
import json

response = requests.get("https://api.yelp.com/v3/businesses/search?location=Chicago&term=Starbucks&limit=50&offset=0",
    headers={
        "Authorization": ""
    }
)
respJSON = response.json()
businesses = respJSON['businesses']

for i in range(1, 10):
    response = requests.get("https://api.yelp.com/v3/businesses/search?location=Chicago&term=Starbucks&limit=50&offset=" + str(50 * i),
        headers={
            "Authorization": ""
        }
    )
    respJSON = response.json()
    businesses.extend(respJSON['businesses'])

businessData = []
for business in businesses:
    if "Starbucks" in business['name']:
        businessData.append({'id': business['id'], 'alias': business['alias'], 'coordinates': business['coordinates'], 'reviewCount': business['review_count']})

print("Length of businessData: " + str(len(businessData)))

businessReviewData = []
for businessDatum in businessData:
    response = requests.get("https://api.yelp.com/v3/businesses/" + businessDatum['id'] + "/reviews",
        headers={
            "Authorization": "Bearer S_sMSY7Lg9iyt54QL4CFA9fauAeLiiOF_7QYAP3Ti3cPbpM8pG8K-reYLULM3tiCDTL7hjyoDoUoz3YXTGtExiJRBdfHHp7zsIOo4ifg6laQDuz690lvnDKhdUZIXnYx"
        }
    )
    respJSON = response.json()
    try: 
        reviews = respJSON['reviews']
        for review in reviews:
            businessReviewDatum = {
                'id': businessDatum['id'],
                'alias': businessDatum['alias'],
                'coordinates': businessDatum['coordinates'],
                'reviewCount': businessDatum['reviewCount'],
                'text': review['text'],
                'rating': review['rating']
            }
            businessReviewData.append(businessReviewDatum)
    except Exception as e:
        print(e)
        print("Exception occurred. Moving onto the next review...")

print(businessReviewData)
print("Review Data length: " + str(len(businessReviewData)))

with open('review-data.json', 'w', encoding='utf-8') as f:
    json.dump(businessReviewData, f, ensure_ascii=False, indent=4)

# with open("review-data.json") as fo:
#     data1 = json.load(fo)

# with open("dunkin-review-data.json") as fo:
#     data2 = json.load(fo)

# data1.extend(data2)

# with open("combined-review-data.json", "w") as fo:
#     json.dump(data1, fo)