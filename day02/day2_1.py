with open("day02/input1.txt") as file:
    id_ranges = [id_range.strip() for id_range in file.readline().split(",")]

invalid_id_count = 0

for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]

    if len(str(start)) == len(str(end)) and len(str(start)) % 2 != 0:
        continue

    for current_id in range(start, end + 1):
        if len(str(current_id)) % 2 != 0:
            continue

        mid_start_index = int(len(str(current_id)) / 2)

        first_half = str(current_id)[:mid_start_index]
        second_half = str(current_id)[mid_start_index:]

        if first_half == second_half:
            invalid_id_count += current_id

print(invalid_id_count)
