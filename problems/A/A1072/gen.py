from random import *
from cyaron import *

CASES = 10

for _t in range(1, CASES + 1):
    io = IO(f"{_t}.in")
    # ==============================
    if _t <= 5:
        io.input_writeln(f"{randint(1, 100)} {randint(1, 100)}")
    else:
        io.input_writeln(f"{randint(1000, 100000)} {randint(1000, 100000)}")
    # ==============================
    io.close()
