if __name__ == "__main__":
    print("Advent of Code 2022 - Day 1")

    with open("input.txt") as f:
        acc = 0
        top = []

        for n in f.readlines():
            try:
                acc += int(n)
            except Exception:
                top.append(acc)
                acc = 0

        top.sort(reverse=True)

        print("Part 1: {}".format(top[0]))
        print("Part 2: {}".format(sum(top[0:3])))

