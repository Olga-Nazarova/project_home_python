def main():
    with open("input.txt") as file:
        rle = file.read()
    encoded = encode(rle)
    decoded = decode(encoded)
    print("Входные данные: " + rle)
    with open('output.txt', 'a') as file:
        file.write(formatOutput(encoded))
    print("Исходящие данные: " + formatOutput(encoded))

def encode(sequence):
    count = 1
    result = []
    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1
    result.append((sequence[len(sequence) - 1], count))
    return result

def decode(sequence):
    result = []
    for item in sequence:
        result.append(item[0] * item[1])
    return "".join(result)

def formatOutput(sequence):
    result = []
    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])
    return "".join(result)

if __name__ == "__main__":
    main()