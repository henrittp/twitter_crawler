# from config.config import access_token, access_token_secret, consumer_key, consumer_secret
from config.config import bearer_token
from job.run import run

if __name__ == "__main__":
    run(bearer_token[0])
