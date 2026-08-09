def ohms_law(voltage, resistance):
    return voltage / resistance

def current_status(current):
    if current > 1:
        return "WARNING: high current!"
    else:
        return "Current is within a safe, working range."


    v = float(input("Voltage (V): "))
    r = float(input("Resistance (Ω): "))
    i = ohms_law(v, r)
    print(f"Current: {i} A")
    print(current_status(i))
    