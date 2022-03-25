import json
import requests

headers = {

    'Content-Type': 'application/json'
}

json_data = {
    'api_key': '2f187337-6c08-4430-b013-0aa31533e94e17fba0db70d13c',
    'agent_id': '1a881bd1-4321-4bc0-9266-25e52450506817fb583a205358',
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