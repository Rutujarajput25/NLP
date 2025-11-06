# -----------------------------
# Knowledge Base: Rules
# -----------------------------
# Each rule connects a set of problems (premises) to a possible solution (conclusion).
rules = [
    ([("problem", "power_light_off")],
     ("solution", "check_power_supply")),

    ([("problem", "computer_not_starting"),
      ("solution", "power_supply_ok")],
     ("solution", "check_RAM")),

    ([("problem", "blank_display"),
      ("solution", "power_supply_ok")],
     ("solution", "check_monitor_cable")),

    ([("problem", "computer_not_starting"),
      ("problem", "blank_display")],
     ("solution", "check_graphics_card")),

    ([("problem", "strange_beep")],
     ("solution", "check_motherboard")),

    ([("problem", "computer_not_starting"),
      ("problem", "strange_beep")],
     ("solution", "check_hard_disk")),

    ([("problem", "computer_not_starting"),
      ("solution", "RAM_ok")],
     ("solution", "check_operating_system")),
]


# -----------------------------
# Function: Forward Chaining
# -----------------------------
# This function applies forward chaining inference on the given facts using the rules.
# It keeps adding new conclusions until no new facts can be derived.
def forward_chaining(facts, rules):
    inferred = set(facts)  # Start with known facts
    changed = True         # Track if any new inference occurs

    while changed:
        changed = False
        # Check each rule in the knowledge base
        for premises, conclusion in rules:
            # If all premises are true, infer the conclusion
            if all(p in inferred for p in premises):
                if conclusion not in inferred:
                    inferred.add(conclusion)
                    changed = True
    return inferred


# -----------------------------
# Main Program: User Interaction
# -----------------------------
# Allows the user to enter symptoms and applies the expert system to suggest solutions.
if __name__ == "__main__":
    print("Troubleshooting Expert System")
    print("Enter observed problems (symptoms).")
    print("Available: computer_not_starting, power_light_off, blank_display, strange_beep")
    print("Type 'done' when finished.\n")

    facts = []  # Store user-entered symptoms

    # Take user input until they type 'done'
    while True:
        symptom = input("Enter a problem (or 'done'): ").strip()

        if symptom.lower() == "done":
            break

        # Accept only known problems
        if symptom in ["computer_not_starting", "power_light_off", "blank_display", "strange_beep"]:
            facts.append(("problem", symptom))
        else:
            print("Unknown problem. Choose from the list.")

    # Perform forward chaining inference
    inferred_facts = forward_chaining(facts, rules)

    # Display the results
    print("\nSuggested Actions / Solutions:")
    solutions_found = False

    for f in inferred_facts:
        if f[0] == "solution":
            print("-", f[1])
            solutions_found = True

    if not solutions_found:
        print("No solution found. Please provide more symptoms.")
