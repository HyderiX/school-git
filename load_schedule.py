import json
def load_schedule():
    with open("schedulejson.txt", "r") as f:
        return json.loads(f.read())