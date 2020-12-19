inputs = [i.strip() for i in open('inputs/day18.txt', 'r').readlines()]

def eval_intstring(expression, precedence):
    break_it_down = expression.split(" ")
    for operators in precedence:
        i = 0
        while i < len(break_it_down) - 2:
            left, op, right = break_it_down[i:i+3]
            if op in operators:
                v = str(eval(left + op + right))
                break_it_down = break_it_down[:i] + [v] + break_it_down[i+3:]
            else:
                i += 1
    return break_it_down[0]

def parse_line(start, line, precedence):
    depth = 0
    s = ""
    for k, char in enumerate(line[start:]):
        if char == "(":
            if depth == 0:
                s += parse_line(k+start+1, line, precedence)
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                break
        elif depth >= 1:
            continue
        else:
            s += char
    v = eval_intstring(s, precedence)
    return str(v)

part1 = sum([int(parse_line(0, line, ["*+"])) for line in inputs])
print(f"part 1: {part1}")

part2 = sum([int(parse_line(0, line, ["+", "*"])) for line in inputs])
print(f"part 2: {part2}")