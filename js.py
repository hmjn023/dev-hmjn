import json

no = 0
groups = 0

data = {
        "no": no,
        "groups": groups,
        "reserve": []
}

with open("data.json", "w") as f:
    json.dump(data, f)

opend = open("./data.json","r")
loaded = json.load(opend)

print(loaded)
print("no: ", loaded["no"], "groups: ", loaded["groups"])

