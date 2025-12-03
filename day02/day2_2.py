def split_equal(string: str, part_size: int) -> list[str]:
    part_list: list[str] = []

    start = 0
    end = part_size

    while end <= len(string):
        part_list.append(string[start:end])

        start += part_size
        end += part_size

    return part_list


with open("day02/input1.txt") as file:
    id_ranges = [id_range.strip() for id_range in file.readline().split(",")]

invalid_id_count = 0

for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]

    for current_id in range(start, end + 1):
        max_part_len = int(len(str(current_id)) / 2)

        for part_len in range(1, max_part_len + 1):
            if len(str(current_id)) % part_len != 0:
                continue

            parts = split_equal(str(current_id), part_len)

            if (len(set(parts))) == 1:
                invalid_id_count += current_id
                break


print(invalid_id_count)
