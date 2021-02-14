import json
def load_schedule():
    with open("schedulejson.json", "r") as f:
        return json.loads(f.read())