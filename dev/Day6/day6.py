import os


def read_answers_by_group(raw_answers: str) -> list:
    # Returns list-list-set:
    #  [group i][person j] = (a, b, c)
    answers = []

    for group_idx, raw_groups in enumerate(raw_answers.split("\n\n")):
        group_answers = []

        for person_idx, person_answers in enumerate(raw_groups.split("\n")):
            group_answers.insert(person_idx, set(person_answers))

        answers.insert(group_idx, group_answers)

    return answers


def sum_common_answers_by_group(answers: list) -> int:
    sum_ret = 0
    for group_answers in answers:
        common_answers = len(set.union(*group_answers))
        sum_ret = sum_ret + common_answers
    return sum_ret


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_answers = file.read()

    answers = read_answers_by_group(raw_answers)
    print(sum_common_answers_by_group(answers))
