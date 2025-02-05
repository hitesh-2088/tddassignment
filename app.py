
def add(numbers):
    if not numbers:
        return 0

    delimiters = [",", "\n"]
    if numbers.startswith("//"):
        custom_delimiter = numbers[2]
        numbers = numbers[4:]
        delimiters.append(custom_delimiter)

    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.split(",")

    result = 0
    for number in numbers:
        if number:
            num = int(number)
            if num < 0:
                raise ValueError("Negatives not allowed")
            if num <= 1000:
                result += num
    return result