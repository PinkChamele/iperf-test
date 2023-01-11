import json

def parse(output):
  decoded_json = output.read().decode("utf-8")

  return json.loads(decoded_json)
