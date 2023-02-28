import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_summary_rss(path):
    OUTPUT_FILE = os.path.join(BASE_DIR, path)
    with open(OUTPUT_FILE) as file:
        lines = file.readlines()[1:]
        rss_sum = 0

        for line in lines:
            columns = line.split()
            rss_sum += int(columns[5])

    return rss_sum


if __name__ == "__main__":
    result = get_summary_rss("output_file.txt")
    print(
        f'Памяти использовано:\n{result} B\n{result / 1024} KB\n{result / 1024 / 1024} MB\n{result / 1024 / 1024 / 1024} GB')
