import pulp as lp

# Define the problem as a minimization problem
prob = lp.LpProblem("Minimize Total Cost", lp.LpMinimize)

# Define decision variables
x1 = lp.LpVariable("Japanese-Style Fried Rice", lowBound=0, cat='Continuous')
x2 = lp.LpVariable("Pasture Raised Large Brown Eggs", lowBound=0, cat='Continuous')
x3 = lp.LpVariable("Blackened Salmon", lowBound=0, cat='Continuous')
x4 = lp.LpVariable("Chicken Burrito Bowl", lowBound=0, cat='Continuous')
x5 = lp.LpVariable("Greek Nonfat Yogurt Plain", lowBound=0, cat='Continuous')

# Define objective function
C1 = 1.52  # Adjusted price per serving of Japanese-Style Fried Rice
C2 = 0.42  # Adjusted price per serving of Pasture Raised Large Brown Eggs
C3 = 5.50  # Adjusted price per serving of Blackened Salmon
C4 = 3.49  # Adjusted price per serving of Chicken Burrito Bowl
C5 = 1.20  # Adjusted price per serving of Greek Nonfat Yogurt Plain
prob += C1 * x1 + C2 * x2 + C3 * x3 + C4 * x4 + C5 * x5

# Define nutritional constraints
# Replace the placeholders (s1, e1, etc.) with actual coefficients
# Sodium
prob += 7 * (680 * x1 + 70 * x2 + 240 * x3 + 630 * x4 + 75 * x5) <= 35000  

# Energy
prob += 7 * (340 * x1 + 70 * x2 + 230 * x3 + 370 * x4 + 110 * x5) >= 14000  

# Protein
prob += 7 * (9 * x1 + 6 * x2 + 23 * x3 + 22 * x4 + 17 * x5) >= 350  

# Vitamin D
prob += 7 * (0 * x1 + 1.2 * x2 + 12.1 * x3 + 0 * x4 + 0 * x5) <= 140 

# Calcium
prob += 7 * (70 * x1 + 26 * x2 + 20 * x3 + 130 * x4 + 190 * x5) >= 9100  

# Iron
prob += 7 * (1.4 * x1 + 1 * x2 + 0.6 * x3 + 2.6 * x4 + 0 * x5) >= 126  

# Potassium
prob += 7 * (260 * x1 + 0 * x2 + 390 * x3 + 690 * x4 + 240 * x5) >= 32900  

# Solve the problem
prob.solve()

# Print the optimal solution
print("Optimal Solution:")
for var in prob.variables():
    print(f"{var.name}: {var.varValue}")

# Print the optimized total cost
print(f"Total Cost: {lp.value(prob.objective)}")


