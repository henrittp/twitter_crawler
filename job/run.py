from tweepy import StreamRule

from job.extract.listener import MyListener


def run(bearer_token: str) -> None:
    stream = MyListener(bearer_token)
    stream.add_rules(StreamRule("trump"))
    stream.filter()
