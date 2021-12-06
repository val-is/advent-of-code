inputs = [int(i) for i in open('inputs/day06.txt', 'r').read().strip().split(",")]

def get_init_timers(inputs):
    timers = {i:0 for i in range(9)}
    for t in inputs:
        timers[t] = timers.get(t, 0) + 1
    return timers

def step_day(timers):
    new_timers = {i:0 for i in range(9)}
    for i in range(9):
        if i == 0:
            new_timers[8] += timers[i]
            new_timers[6] += timers[i]
        else:
            new_timers[i-1] += timers[i]
    return new_timers

def count_fish(timers):
    s=0
    for t in timers:
        s+=timers[t]
    return s

def run_days(days, timers):
    for _ in range(days):
        timers = step_day(timers)
    return timers

part1 = count_fish(run_days(80, get_init_timers(inputs)))
print(f"part 1: {part1}")

part2 = count_fish(run_days(256, get_init_timers(inputs)))
print(f"part 2: {part2}")
