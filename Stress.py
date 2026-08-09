def stress_mpa(force_n, area_mm2):
    return force_n / area_mm2

def factor_of_safety(yield_mpa, working_mpa):
    return yield_mpa / working_mpa


s = stress_mpa (2000, 25)
print(f"Stress: {s} MPa")
print(f"Factor of Safety: {factor_of_safety(250, s)}")
