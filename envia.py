import requests
import json

header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic ZTI5YjZhMWYtZTJkYS00OWJiLTkyZTAtMDRjMjIzOWNiOTBi"}

payload = {"app_id": "ff177554-db1d-4280-bf67-5f5a7602ba5c",
           "include_player_ids": ["071993f2-958a-46b2-8369-4318324e41a7"],
           "contents": {"en": "Ya pe papi"}}
 
req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
 
print(req.status_code, req.reason)