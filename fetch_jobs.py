import httpx

url = "https://boards-api.greenhouse.io/v1/boards/duolingo/jobs"

response = httpx.get(url)
data = response.json()

print("Total jobs: ", data["meta"]["total"])

for job in data["jobs"]:
    print(job["title"], " - ", job["location"]["name"])
    