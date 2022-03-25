import json
import requests

headers = {

    'Content-Type': 'application/json'
}

json_data = {
    'api_key': '',
    'agent_id': '',
    'utterance': 'こんにちは',
    'uid': 'mebo.ai_sample_001',
}

response = requests.post('https://api-mebo.dev/api', headers=headers, data=json.dumps(json_data))

res_data = response.json()
#print(response.status_code)
print(response.text)
replay = response.text
replay = json.loads(replay)
print(replay)
print(type(replay))
print(replay['utterance'])
