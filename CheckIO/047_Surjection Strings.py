def isometric_strings(a: str, b: str) -> bool:
    temp_dict = {}
    for i in range(len(a)):
        if temp_dict.get(a[i]) == None or temp_dict.get(a[i]) == b[i]:
            temp_dict[a[i]] = b[i]
        else:
            return False
    return True
