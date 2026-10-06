print("====================================")
print("   INSULATION RESISTANCE CALCULATOR")
print("====================================")

voltage = float(input("Enter test voltage (V): "))
leakage_current = float(input("Enter leakage current (A): "))

if voltage <= 0 or leakage_current <= 0:
    print("\nPlease enter positive values.")
else:
    resistance = voltage / leakage_current

    print("\n------------- RESULTS -------------")
    print(f"Test Voltage       : {voltage:.2f} V")
    print(f"Leakage Current    : {leakage_current:.6f} A")
    print(f"Insulation Resistance: {resistance:.2f} Ω")

    # Convert to megaohms
    resistance_mohm = resistance / 1_000_000
    print(f"Insulation Resistance: {resistance_mohm:.4f} MΩ")
    print("-----------------------------------")
