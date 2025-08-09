def is_safe(line):
    levels = [int(level) for level in line.split(" ")]

    direction = None
    prev_level = levels[0]

    for level in levels[1:]:
        if abs(prev_level - level) < 1 or abs(prev_level - level) > 3:
            return False
        if direction is None:
            if level > prev_level:
                direction = "ascending"
            elif level < prev_level:
                direction = "descending"
        else:
            if direction == "ascending" and level < prev_level:
                return False
            elif direction == "descending" and level > prev_level:
                return False

        prev_level = level

    return True


if __name__ == "__main__":
    with open("day_2/input.txt") as f:
        lines = f.readlines()
        safe_count = sum(1 for line in lines if is_safe(line))
        print(f"{safe_count=}")
