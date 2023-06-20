def sort_by_ext(files: list):
    files_without_name = []
    files_with_name = []
    for i in files:
        if i.startswith('.') and i.count('.') == 1:
            files_without_name.append(i)
        else:
            files_with_name.append(i)
    files_without_name.sort()
    files_with_name.sort(key=lambda x: (x.split('.')[-1], x))
    return files_without_name + files_with_name
