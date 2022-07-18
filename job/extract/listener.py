import json
from datetime import datetime
from typing import Any

import tweepy

# Define a file to write tweets to
date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
output = open(f"collected_tweets_{date_now}.txt", "w")


# Implement class to listen for tweets
class MyListener(tweepy.StreamingClient):
    # Override the on_data method to write tweets to a file
    def on_data(self, data: Any) -> bool:
        # Write the data to the file
        tweet_dict = json.dumps(data.decode("utf-8"))
        output.write(tweet_dict + "\n")
        print(data)
        return True

    # Override the on_error method to print error messages
    def on_status(self, status: str) -> bool:
        print(status)
        return True
