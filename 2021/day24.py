"""
so, i did this one mainly on paper. i used build_exp to get a lisp-ish expression of the MONAD code,
and then did on-paper analysis of it. very cool problem, i liked it!
"""

inputs = [i for i in open('inputs/day24.txt', 'r').readlines()]

class Interpreter:
    w, x, y, z = 0, 0, 0, 0
    pc = 0
    
    instrs = []

    def __init__(self, instrs):
        self.instrs = instrs
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.pc = 0

    def get_reg(self, reg):
        if type(reg) == int:
            return reg
        return {
                "w": self.w,
                "x": self.x,
                "y": self.y,
                "z": self.z,
                }[reg]
    
    def set_reg(self, reg, val):
        if reg == "w":
            self.w = val
        elif reg == "x":
            self.x = val
        elif reg == "y":
            self.y = val
        elif reg == "z":
            self.z = val
        else:
            assert False

    def step(self, input_stack):
        # returns true if halted
        instr = self.instrs[self.pc]
        op, a, b = instr

        if op == "inp":
            self.set_reg(a, input_stack.pop(0))
        elif op == "add":
            self.set_reg(a, self.get_reg(a) + self.get_reg(b))
        elif op == "mul":
            self.set_reg(a, self.get_reg(a) * self.get_reg(b))
        elif op == "div":
            self.set_reg(a, int(self.get_reg(a) // self.get_reg(b)))
        elif op == "mod":
            self.set_reg(a, self.get_reg(a) % self.get_reg(b))
        elif op == "eql":
            self.set_reg(a, 1 if self.get_reg(a) == self.get_reg(b) else 0)
        else:
            assert False

        self.pc += 1
        if self.pc >= len(self.instrs):
            return True
        return False

    def build_exp(self):
        instr = self.instrs[self.pc]
        x = "(x)"
        y = "(y)"
        z = "(z)"
        w = "(w)"

        input_idx = 0
        simplifications = {}
        def update_reg(op, a, b):
            nonlocal x, y, z, w, input_idx, simplifications
            v = ""
            target_val = {"w":w, "x":x, "y":y, "z":z}[a]
            if b == "":
                b_val = ""
            elif type(b) == int:
                b_val = f"({b})"
            else:
                b_val = {"w":w, "x":x, "y":y, "z":z}[b]
            if op == "inp":
                v = f"([ld {input_idx}])"
                input_idx += 1
            elif op == "add":
                v = f"(+ {target_val} {b_val})"
                if b_val == 0:
                    v = target_val
            elif op == "mul":
                v = f"(* {target_val} {b_val})"
                if b_val == 0:
                    v = "(0)"
            elif op == "div":
                v = f"(/ {target_val} {b_val})"
                if target_val == "(0)":
                    v = "(0)"
            elif op == "mod":
                v = f"(% {target_val} {b_val})"
                if target_val == "(0)":
                    v = "(0)"
            elif op == "eql":
                v = f"(= {target_val} {b_val})"
                if target_val == b_val:
                    v = "(1)"
            
            if a == "w":
                w = v
            elif a == "x":
                x = v
            elif a == "y":
                y = v
            elif a == "z":
                z = v

        self.pc = 0
        while self.pc < len(self.instrs):
            op, a, b = self.instrs[self.pc]
            update_reg(op, a, b)

            self.pc += 1
        print(x)
        print(y)
        print(z)
        print(w)

def parse_instrs(inputs):
    instrs = []
    for i in inputs:
        op, vs = i.strip().split(" ", 1)
        if op == "inp":
            instrs.append((op, vs, ""))
        else:
            a, b = vs.split(" ")
            if b not in "wxyz":
                b = int(b)
            instrs.append((op, a, b))
    return instrs

def run_program(instrs, prog_input):
    stack = [int(i) for i in prog_input.strip()]
    interp = Interpreter(instrs)
    halted = False
    while not halted:
        halted = interp.step(stack)
    return interp.w, interp.x, interp.y, interp.z

monad_prog = parse_instrs(inputs)

def test_model(model_num, instrs=monad_prog):
    model_num = str(model_num)
    w, x, y, z = run_program(instrs, model_num)
    return z == 0

# max_n = 99999999999999 
# for n in range(max_n, 0, -1):
#     print(n)
#     if "0" in str(n):
#         continue
#     if test_model(n):
#         print(n)
print(test_model(11815671117121))

part1 = 0
print(f"part 1: {part1}")

part2 = 0
print(f"part 2: {part2}")
