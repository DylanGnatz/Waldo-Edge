def list_dicts_contains(searchList, searchKey, searchVal):
    for i in searchList:
        if i[searchKey] == searchVal:
            return True
    return False