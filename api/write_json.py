import json
import random


def new_seq_id(old_seq_id):
    sid = int(old_seq_id) + 1
    new_sid = str(sid)
    return new_sid


# with open("client.json", "r") as rf:
#     contents = json.load(rf)
# # new_seqId = contents['SequenceID']
#     contents['SequenceID'] = new_seq_id(contents['SequenceID'])
#
#     with open("client.json", "w") as f:
#         print(type(contents))
#         f.write(json.dump(contents, rf))

# with open("client.json", "r") as f:
#     content = json.load(f)
#     content['SequenceID'] = "1234577"
#
#
# with open("client.json", "w") as f:
#     print(type(content))
#     f.write(json.dump(content, indent=2))

with open("client.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    # tmp = data["location"]
    print(data['SequenceID'])
    data['SequenceID'] = new_seq_id(data['SequenceID'])
    print(data['SequenceID'])

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile, indent=2)
    print(data['SequenceID'])
    jsonFile.truncate()








