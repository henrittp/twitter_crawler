from pathlib import Path

filepath = Path(__file__).parent / "bearer_token.txt"

with open(filepath, "r") as file:
    bearer_token = file.readlines()
