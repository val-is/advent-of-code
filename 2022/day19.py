from dataclasses import dataclass, replace
from typing import List

@dataclass(frozen=True)
class Cost:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def can_build(self, resources):
        if (resources.ore >= self.ore and
            resources.clay >= self.clay and
            resources.obsidian >= self.obsidian and
            resources.geode >= self.geode):
            return True
        return False

    def subtract_recipe(self, recipe):
        return Cost(
            self.ore - recipe.ore,
            self.clay - recipe.clay,
            self.obsidian - recipe.obsidian,
            self.geode - recipe.geode)

@dataclass(frozen=True)
class Blueprint:
    ore_robot: Cost
    clay_robot: Cost
    obsidian_robot: Cost
    geode_robot: Cost

    def get_recipes(self) -> List[Cost]:
        return [self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot]

blueprints = []
for line in open('inputs/day19.txt', 'r').readlines():
    line = line.strip().split(" ")
    blueprints.append(Blueprint(
        Cost(int(line[6]), 0, 0, 0),
        Cost(int(line[12]), 0, 0, 0),
        Cost(int(line[18]), int(line[21]), 0, 0),
        Cost(int(line[27]), 0, int(line[30]), 0),
    ))

@dataclass(frozen=True)
class DPState:
    ore_bots: int
    clay_bots: int
    obsidian_bots: int
    geode_bots: int
    resources: Cost
    cur_minute: int

start_state = DPState(1, 0, 0, 0, Cost(0, 0, 0, 0), 0)

# memoized attempts?
DP = {}
def get_next_states(cur_state: DPState, blueprint: Blueprint, final_time: int):
    global DP
    # # can we remove duplicate states early?
    # if cur_state in DP:
    #     return DP[cur_state]

    # attempt build
    # step 1: increment minute
    base_state = replace(cur_state, cur_minute=cur_state.cur_minute+1)

    # step 2: attempt build more bots
    # assumption 1: it's always optimal to build a robot ASAP.
    # i.e. we will only ever build one of each type of robot in a step
    next_states = []
    for bot_state in range(16):
        progressive_state = base_state
        if bot_state & (1<<0):
            if not progressive_state.resources.can_build(blueprint.ore_robot):
                continue
            progressive_state = replace(progressive_state,
                                        resources=progressive_state.resources.subtract_recipe(blueprint.ore_robot),
                                        ore_bots=progressive_state.ore_bots+1)
        if bot_state & (1<<1):
            if not progressive_state.resources.can_build(blueprint.clay_robot):
                continue
            progressive_state = replace(progressive_state,
                                        resources=progressive_state.resources.subtract_recipe(blueprint.clay_robot),
                                        clay_bots=progressive_state.clay_bots+1)
        if bot_state & (1<<2):
            if not progressive_state.resources.can_build(blueprint.obsidian_robot):
                continue
            progressive_state = replace(progressive_state,
                                        resources=progressive_state.resources.subtract_recipe(blueprint.obsidian_robot),
                                        obsidian_bots=progressive_state.obsidian_bots+1)
        if bot_state & (1<<3):
            if not progressive_state.resources.can_build(blueprint.geode_robot):
                continue
            progressive_state = replace(progressive_state,
                                        resources=progressive_state.resources.subtract_recipe(blueprint.geode_robot),
                                        geode_bots=progressive_state.geode_bots+1)
        # step 3: increment resources
        progressive_state = replace(progressive_state,
                            resources=replace(progressive_state.resources,
                                            ore=progressive_state.resources.ore+cur_state.ore_bots,
                                            clay=progressive_state.resources.clay+cur_state.clay_bots,
                                            obsidian=progressive_state.resources.obsidian+cur_state.obsidian_bots,
                                            geode=progressive_state.resources.geode+cur_state.geode_bots))
        next_states.append(progressive_state)

    # prune if suboptimal route
    if cur_state in DP and cur_state.resources.geode < DP[cur_state]:
        return
    DP[cur_state] = cur_state.resources.geode
    
    if cur_state.cur_minute == final_time:
        return
    
    for state in next_states:
        get_next_states(state, blueprint, final_time)

import time
start = time.time()
get_next_states(start_state, blueprints[0], 24)
end = time.time()

print(end-start)

max_geodes = 0
for state in DP:
    max_geodes = max(DP[state], max_geodes)
print(max_geodes)
