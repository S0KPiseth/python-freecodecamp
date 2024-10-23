def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]

        if operator == "+":
            answer = str(int(first_number) + int(second_number))
        else:
            answer = str(int(first_number) - int(second_number))

        width = max(len(first_number), len(second_number)) + 2
        first_line.append(first_number.rjust(width))
        second_line.append(operator + second_number.rjust(width - 1))
        dashes.append("-" * width)
        answers.append(answer.rjust(width))

    if show_answers:
        arranged_problems = (
            "    ".join(first_line) + "\n" +
            "    ".join(second_line) + "\n" +
            "    ".join(dashes) + "\n" +
            "    ".join(answers)
        )
    else:
        arranged_problems = (
            "    ".join(first_line) + "\n" +
            "    ".join(second_line) + "\n" +
            "    ".join(dashes)
        )

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')