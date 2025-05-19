# input: "apple,banana,cherry"
# output: ["apple", "banana", "cherry"]


def string_parser(csv_string):
    split = csv_string.split(",")
    for i in range(len(split)):
        # handle words with white space around it like "  apple "
        split[i] = split[i].strip()

    return split
