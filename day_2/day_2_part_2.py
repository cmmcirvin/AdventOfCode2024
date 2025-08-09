from day_2_part_1 import is_safe

def dampened_is_safe(line):
    if is_safe(" ".join(line.split(" ")[1:])):
        return True
    elif is_safe(" ".join([line.split(" ")[0]] + line.split(" ")[2:])):
        return True

    levels = [int(level) for level in line.split(" ")]

    direction = None
    prev_level = levels[0]
    removed_level = False

    for level in levels[1:]:
        if abs(prev_level - level) < 1 or abs(prev_level - level) > 3:
            if not removed_level:
                # Don't update prev_level
                removed_level = True
                continue
            return False

        if direction is None:
            if level > prev_level:
                direction = "ascending"
            elif level < prev_level:
                direction = "descending"
        else:
            if direction == "ascending" and level < prev_level:
                if not removed_level:
                    removed_level = True
                    continue
                return False
            elif direction == "descending" and level > prev_level:
                if not removed_level:
                    removed_level = True
                    continue
                return False

        prev_level = level

    return True


if __name__ == "__main__":
    with open("day_2/input.txt") as f:
        lines = f.readlines()
        safe_count = sum(1 for line in lines if dampened_is_safe(line))
        print(f"{safe_count=}")

        # Test cases
        assert dampened_is_safe("0 4 5 6 7")
        assert dampened_is_safe("8 9 8 7 6")
        assert dampened_is_safe("8 12 9 7 6")
        assert dampened_is_safe("10 12 11 12 13")
