import requests
import json



data=requests.get("https://student.ecoachinglms.com/courses/57")

print(data.content)