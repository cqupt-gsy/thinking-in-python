import json


def loadJsonDataForKey(key='missingPage', backup='item_link.json'):
    json_file = open(backup, mode='r')
    json_data = json.load(json_file)
    results = []
    for data in json_data:
        if data.get(key) is not None:
            results.append(data.get(key))
    return results


def appendItemLinkInMissingPageForKey(key='itemLink'):
    back_up_file = open('item_link_backup.json', mode='r')
    original_file = open('item_link.json', mode='r')

    back_up_data = json.load(back_up_file)
    original_data = json.load(original_file)
    back_up_file.close()
    original_file.close()
    for data in back_up_data:
        if data.get(key) is not None:
            original_data.append({'itemLink': data.get(key)})
    original_file = open('item_link.json', mode='w')
    json.dump(original_data, original_file, indent=0)
    original_file.close()


def removeItemLinkForKey(key='missingPage'):
    original_file = open('item_link.json', mode='r')

    original_data = json.load(original_file)
    original_file.close()
    for data in original_data:
        if data.get(key) is not None:
            original_data.remove(data)
    original_file = open('item_link.json', mode='w')
    json.dump(original_data, original_file, indent=0)
    original_file.close()

# appendItemLinkInMissingPageForKey()
# removeItemLinkForKey()

