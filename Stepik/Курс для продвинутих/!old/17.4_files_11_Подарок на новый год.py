with open('17.4_files_11_Подарок на новый год.txt', 'r', encoding='utf-8') as input_file, open('new_scores.txt', 'w', encoding='utf-8') as output_file:
    scores_list = [[int(item) if item.isdigit() else item for item in line.split()] for line in input_file.readlines()]
    # new_score_list = []
    for score in scores_list:
        if score[-1] >= 95:
            score[-1] = 100
        else:
            score[-1] = score[-1] + 5

        output_file.write(' '.join(str(item) for item in score) + '\n')


# print(new_score_list)