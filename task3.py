machine_a = {
    ("q0", "1"): ("1", "R", "q0"),
    ("q0", "0"): ("0", "R", "q0"),
    ("q0", "_"): ("_", "R", "stop"),
}
                                        # Машина A: іде вправо і зупиняється на порожній клітинці "_"

machine_b = {
    ("q0", "1"): ("1", "R", "q0"),
    ("q0", "0"): ("0", "R", "loop"),
    ("q0", "_"): ("_", "R", "stop"),
    ("loop", "1"): ("1", "R", "loop"),
    ("loop", "0"): ("0", "R", "loop"),
    ("loop", "_"): ("_", "R", "loop"),
}
                                                            # Машина B: якщо бачить 0, то іде вправо вічно


def run(rules, text, max_steps=1000):
    tape = {}
    for i in range(len(text)):
        tape[i] = text[i]
    position = 0
    state = "q0"
    steps = 0
    while state != "stop":
        if steps == max_steps:
            return "не зупинилась за %d кроків" % max_steps
        symbol = tape.get(position, "_")
        write, move, state = rules[(state, symbol)]
        tape[position] = write
        if move == "R":
            position += 1
        else:
            position -= 1
        steps += 1
    return "зупинилась за %d кроків" % steps


for name, rules in (("A", machine_a), ("B", machine_b)):
    print("Машина", name)
    for text in ["", "1", "111", "11111", "1101", "0"]:
        print("  вхід '%s': %s" % (text, run(rules, text)))