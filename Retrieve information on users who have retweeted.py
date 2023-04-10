import requests
import json
import pandas as pd

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = 'your_bearer_token'

def create_url(next_token=None):
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    user_fields = "user.fields=created_at,description"
    # You can replace the ID given with the Tweet ID you wish to lookup Retweeting users for
    # You can find an ID by using the Tweet lookup endpoint
    id = "hogehoge"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = f"https://api.twitter.com/2/tweets/{id}/retweeted_by"
    if next_token:
        url = f"{url}?pagination_token={next_token}"
    return url, user_fields

def encode(s):
    return s.replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RetweetedByPython"
    return r

def connect_to_endpoint(url, user_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=user_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json(), response.headers.get("link")

def main():
    url, user_fields = create_url()
    data = []
    while True:
        json_response, pagination_token = connect_to_endpoint(url, user_fields)
        for user in json_response["data"]:
            data.append({
                "id": user["id"],
                "Name": encode(user["name"]),
                "created_at": user["created_at"]
            })
        if pagination_token and "next" in pagination_token:
            next_token = pagination_token.split("next")[0].split("page")[1].split("=")[1][:-2]
            url, _ = create_url(next_token)
        else:
            break
    df = pd.DataFrame(data, columns=["id", "Name", "created_at"])
    id = "hogehoge"
    df.to_csv(f"{id}.csv", index=False)
    print(df.head())

if __name__ == "__main__":
    main()
