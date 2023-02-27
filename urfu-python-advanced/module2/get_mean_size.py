import sys


def get_mean_size(data):
    size_sum = 0
    for line in data:
        columns = line.split()
        print(columns)
        size_sum += int(columns[4])

    return size_sum / len(data)


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()[1:]
    result = get_mean_size(data)
    print(f'Средний размер файла: {result} B')
