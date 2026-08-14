def current_sweep(voltage, resistors):
    for r in resistors:
        current = voltage/r
        print(f" R={r} Ohms, I={current} A")

my_resistors = [100, 220, 330, 470, 1000]
current_sweep(9, my_resistors)