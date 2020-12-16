input_raw = open("inputs/day16.txt", 'r').read().strip()
parts = [i.strip() for i in input_raw.split("\n\n")]
rules, ticket, nearby = parts

ticket = ticket.split("\n")[1]
nearby = nearby.split("\n")[1:]

fields = {}
for rule in rules.split("\n"):
    key, value = rule.split(": ")
    range1, range2 = value.split(" or ")
    range1 = [int(i) for i in range1.split("-")]
    range2 = [int(i) for i in range2.split("-")]
    fields[key] = (range1, range2)

def validate_ticket(ticket):
    fields_in = {int(i): [] for i in ticket.split(",")}
    inv_fields = []
    for i in fields_in:
        v = False
        for field_validating in fields:
            r1, r2 = fields[field_validating]
            if (r1[0] <= i <= r1[1] or
                    r2[0] <= i <= r2[1]):
                    v = True
        if not v:
            inv_fields += [i]
    return inv_fields

part1 = 0

valid_tickets = []
for n in nearby:
    error = validate_ticket(n)
    if error == []:
        valid_tickets.append(n)
    part1 += sum(error)

print(f"part 1: {part1}")

def build_field_set(ticket):
    indexes = [int(i) for i in ticket.split(",")]
    fields_in = {}
    for index, i in enumerate(indexes):
        possible = []
        for field_validating in fields:
            r1, r2 = fields[field_validating]
            if (r1[0] <= i <= r1[1] or
                    r2[0] <= i <= r2[1]):
                    possible += [field_validating]
        fields_in[index] = possible
    return fields_in

# include as index: [keys]
possible_keys = []
for field in fields:
    possible_keys.append(field)
include_list = {i: possible_keys.copy() for i in range(len(ticket.split(",")))}

def iter_thing():
    for t in valid_tickets:
        possible_fields = build_field_set(t)
        # possible fields: {index: [possible_fields]}
        for index in possible_fields:
            deleting_fields = []
            for field in include_list[index]:
                if field not in possible_fields[index]:
                    deleting_fields.append(field)
            for field in deleting_fields:
                include_list[index].remove(field)

known_fields = {field: -1 for field in fields}
def done():
    for i in known_fields:
        if known_fields[i] == -1:
            return False
    return True

while not done():
    iter_thing()
    done_fields = []
    for index in include_list:
        if len(include_list[index]) == 1:
            done_fields.append(include_list[index][0])
            known_fields[include_list[index][0]] = index
    for field in done_fields:
        for index in include_list:
            if len(include_list[index]) != 1 and field in include_list[index]:
                include_list[index].remove(field)

ticket = [int(i) for i in ticket.split(",")]
part2 = 1
for index in include_list:
    if include_list[index][0].startswith("departure"):
        part2 *= ticket[index]

print(f"part 2: {part2}")