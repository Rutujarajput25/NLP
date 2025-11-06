# -----------------------------
# Class: GoalStackPlanner
# -----------------------------
# Implements the Goal Stack Planning algorithm for AI planning problems.
# The planner works by maintaining a stack of goals and actions.
# It tries to satisfy goals one by one by pushing actions and their preconditions
# onto the stack until the goal state is achieved.
class GoalStackPlanner:
    def __init__(self, initial, goal, actions):
        self.state = set(initial)   # Current world state
        self.goal = goal            # Goal facts to achieve
        self.actions = actions      # All possible actions
        self.stack = list(goal)     # Initialize stack with goal conditions
        self.plan = []              # Stores the final sequence of actions

    # Check if a fact is already satisfied in the current state
    def is_satisfied(self, fact):
        return fact in self.state

    # Apply an action: update the current state
    def apply_action(self, action):
        for d in action["delete"]:
            self.state.discard(d)
        for a in action["add"]:
            self.state.add(a)

    # Core planning loop
    def plan_steps(self):
        while self.stack:
            top = self.stack.pop()  # Look at the top of the stack

            if isinstance(top, str):   # If top is a goal condition (fact)
                if not self.is_satisfied(top):  # If not yet achieved
                    # Find an action that can achieve this goal
                    for action in self.actions:
                        if top in action["add"]:
                            # Push action and its preconditions onto the stack
                            self.stack.append(action)
                            self.stack.extend(action["preconditions"])
                            break
            else:   # If top is an action
                # Check if all preconditions are satisfied
                if all(pre in self.state for pre in top["preconditions"]):
                    self.apply_action(top)
                    self.plan.append(top["name"])  # Record the executed action

        return self.plan


# -----------------------------
# Action Definitions
# -----------------------------
# These functions define possible actions with their preconditions, add, and delete lists.

def pickup(x):
    return {
        "name": f"PickUp({x})",
        "preconditions": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})"],
        "delete": [f"OnTable({x})", "ArmEmpty"]
    }


def putdown(x):
    return {
        "name": f"PutDown({x})",
        "preconditions": [f"Holding({x})"],
        "add": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})"]
    }


def stack(x, y):
    return {
        "name": f"Stack({x},{y})",
        "preconditions": [f"Holding({x})", f"Clear({y})"],
        "add": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})", f"Clear({y})"]
    }


def unstack(x, y):
    return {
        "name": f"UnStack({x},{y})",
        "preconditions": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})", f"Clear({y})"],
        "delete": [f"On({x},{y})", "ArmEmpty"]
    }


# -----------------------------
# Problem Definition
# -----------------------------
# Initial world state
initial = [
    "OnTable(A)", "OnTable(B)", "OnTable(C)",
    "Clear(A)", "Clear(B)", "Clear(C)", "ArmEmpty"
]

# Goal state to achieve
goal = ["On(C,B)", "On(B,A)"]

# Define all possible actions in the Blocks World
actions = [
    pickup("A"), pickup("B"), pickup("C"),
    putdown("A"), putdown("B"), putdown("C"),
    stack("A", "B"), stack("A", "C"),
    stack("B", "A"), stack("B", "C"),
    stack("C", "A"), stack("C", "B"),
    unstack("A", "B"), unstack("B", "A"),
    unstack("C", "A"), unstack("C", "B")
]

# -----------------------------
# Execute the Planner
# -----------------------------
planner = GoalStackPlanner(initial, goal, actions)
solution = planner.plan_steps()
print("Plan:", solution)
