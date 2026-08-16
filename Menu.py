def ohms_law(voltage, resistance):
    return voltage / resistance

def stress_mpa(force, area):
    return force / area

def power*(voltage, current):
    return voltage * current


while True:
    print()  
    print("--- forge-tools ---")
    print("1: Ohm's law")
    print("2: Stress")
    print("3: Quit")
    choice = input("Pick a tool: ")

    if choice == "1":
        v = float(input("Voltage (V): "))
        r = float(input("Resistance (ohms): "))
        print(f"Current = {ohms_law(v, r)} A")
    elif choice == "2":
        f = float(input("Force (N): "))
        a = float(input("Area (mm^2): "))
        print(f"Stress = {stress_mpa(f, a)} MPa")
    elif choice == "3":
        print("Goodbye!")
        break  
    else:
        print("Haha lalaloooser - invalid choice.")