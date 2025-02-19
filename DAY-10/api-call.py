import requests
 
response = requests.get("https://api.github.com/repos/aws-samples/amazon-bedrock-workshop/pulls")

compelte_detail = response.json()

for i in range(len(compelte_detail)):
 print(compelte_detail[i]["user"]["login"])
