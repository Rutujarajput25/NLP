from constraint import Problem  # Import the constraint-solving library

# Define list of teams
teams = ["T1", "T2", "T3", "T4"]

# Generate all possible matches — each unique pair of teams
# Example: [('T1','T2'), ('T1','T3'), ('T1','T4'), ('T2','T3'), ('T2','T4'), ('T3','T4')]
matches = [(t1, t2) for i, t1 in enumerate(teams) for t2 in teams[i + 1:]]

# Define available time slots and stadiums
time_slots = [1, 2, 3]      # 3 possible time slots
stadiums = ["A", "B"]       # 2 possible stadiums

# Create a constraint satisfaction problem instance
p = Problem()

# Each match is assigned a (time_slot, stadium) pair
# Example domain: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]
p.addVariables(matches, [(t, s) for t in time_slots for s in stadiums])

# ---------------- Constraint 1 ----------------
# No team can play more than one match at the same time slot
for team in teams:
    # Get all matches where the current team is participating
    team_matches = [m for m in matches if team in m]
    
    # For each pair of matches involving the same team
    for i in range(len(team_matches)):
        for j in range(i + 1, len(team_matches)):
            # Ensure they are not scheduled in the same time slot
            p.addConstraint(
                lambda m1, m2: m1[0] != m2[0],  # Compare only time slots
                (team_matches[i], team_matches[j])
            )

# ---------------- Constraint 2 ----------------
# No two matches can happen at the same stadium in the same time slot
for i in range(len(matches)):
    for j in range(i + 1, len(matches)):
        p.addConstraint(
            # Prevent same (time_slot, stadium) combination
            lambda m1, m2: not (m1[0] == m2[0] and m1[1] == m2[1]),
            (matches[i], matches[j])
        )

# Get all possible valid solutions that satisfy all constraints
solutions = p.getSolutions()

# Display the total number of valid schedules
print("Total valid schedules:", len(solutions))

# Print one sample valid schedule
print("Sample Schedule:")
for match, schedule in solutions[0].items():
    print(f"{match}: Time Slot {schedule[0]}, Stadium {schedule[1]}")
