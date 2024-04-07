# MSDS-460-Assignment-1-The-Diet-Problem
NWU MSDS 460 (Individual) Assignment 1: Linear Programming Example---The Diet Problem Revisited (Spring 2024)

Part 1:

Having recently succumbed to the allure of Trader Joe's, I found myself drawn to utilizing their diverse array of food items for my initial assignment. What captivates me about Trader Joe's is their expansive selection, offering everything from humble rice dishes to indulgent Portuguese custard tarts. For this assignment, I selected five distinct food items: Japanese-Style Fried Rice, Chicken Burrito Bowl, and Blackened Salmon, along with additional grocery essentials such as Pasture-raised Large Brown Eggs and Greek Nonfat Yogurt. In the Product Shots folder you can find screenshots of the nutrional facts for each food item.

The pricing methodology employed to determine the cost per serving is also included in the product shots folder. This process involves multiplying the serving size in grams by the number of servings per item to ascertain the total weight in grams. Subsequently, dividing the serving size in grams by the total weight yields a decimal value, which is then multiplied by the price of the entire item to derive the cost per serving.

Part 2: Program Code and Output

CODE:

import pulp as lp

prob = lp.LpProblem("Minimize Total Cost", lp.LpMinimize)

x1 = lp.LpVariable("Japanese-Style Fried Rice", lowBound=0, cat='Continuous')
x2 = lp.LpVariable("Pasture Raised Large Brown Eggs", lowBound=0, cat='Continuous')
x3 = lp.LpVariable("Blackened Salmon", lowBound=0, cat='Continuous')
x4 = lp.LpVariable("Chicken Burrito Bowl", lowBound=0, cat='Continuous')
x5 = lp.LpVariable("Greek Nonfat Yogurt Plain", lowBound=0, cat='Continuous')

C1 = 1.52  # Adjusted price per serving of Japanese-Style Fried Rice
C2 = 0.42  # Adjusted price per serving of Pasture Raised Large Brown Eggs
C3 = 5.50  # Adjusted price per serving of Blackened Salmon
C4 = 3.49  # Adjusted price per serving of Chicken Burrito Bowl
C5 = 1.20  # Adjusted price per serving of Greek Nonfat Yogurt Plain
prob += C1 * x1 + C2 * x2 + C3 * x3 + C4 * x4 + C5 * x5

# Sodium
prob += 7 * (680 * x1 + 70 * x2 + 240 * x3 + 630 * x4 + 75 * x5) <= 35000  

# Energy
prob += 7 * (340 * x1 + 70 * x2 + 230 * x3 + 370 * x4 + 110 * x5) >= 14000  

# Protein
prob += 7 * (9 * x1 + 6 * x2 + 23 * x3 + 22 * x4 + 17 * x5) >= 350  

# Vitamin D
prob += 7 * (0 * x1 + 1.2 * x2 + 12.1 * x3 + 0 * x4 + 0 * x5) >= 140 

# Calcium
prob += 7 * (70 * x1 + 26 * x2 + 20 * x3 + 130 * x4 + 190 * x5) >= 9100  

# Iron
prob += 7 * (1.4 * x1 + 1 * x2 + 0.6 * x3 + 2.6 * x4 + 0 * x5) >= 126  

# Potassium
prob += 7 * (260 * x1 + 0 * x2 + 390 * x3 + 690 * x4 + 240 * x5) >= 32900  

prob.solve()

print("Optimal Solution:")
for var in prob.variables():
    print(f"{var.name}: {var.varValue}")

print(f"Total Cost: {lp.value(prob.objective)}")

OUTPUT:

Optimal Solution:
Blackened_Salmon: 1.2762197
Chicken_Burrito_Bowl: 5.1677501
Greek_Nonfat_Yogurt_Plain: 2.6521949
Japanese_Style_Fried_Rice: 0.0
Pasture_Raised_Large_Brown_Eggs: 3.798118
Total Cost: 29.832499639

Part 3.

To meet the nutritional requirements while minimizing the total cost, I should consume approximately (Rounded two decimal points):	

Japanese-Style Fried Rice: 0 servings or 0 grams
Pasture Raised Large Brown Eggs: 3.80 servings or 190 grams
Blackened Salmon: 1.28 servings or 145 grams
Chicken Burrito Bowl: 5.17 servings or 1706 grams
Greek Nonfat Yogurt Plain: 2.65 servings or 451 grams

At a total, minimized cost of $29.83
This means I would need to spend, at a minimum, $29.83 on food a week.

It is important to note that the Japanese-Style Fried Rice is not included in the optimal solution, meaning it does not contribute to meeting the nutritional requirements most cost-effectively.

Part 4.

The revised linear programming problem with the constraint of at least one serving of each food item per week resulted in a slightly different solution compared to the original one. 
Here's a comparison of the two solutions:

Before Constraint:

Blackened Salmon: 1.28 servings
Chicken Burrito Bowl: 5.17 servings
Greek Nonfat Yogurt Plain: 2.65 servings
Japanese Style Fried Rice: 0.00 servings
Pasture Raised Large Brown Eggs: 3.80 servings
Total Cost: $29.83

After Constraint:

Blackened Salmon: 1.32 servings
Chicken Burrito Bowl: 4.78 servings
Greek Nonfat Yogurt Plain: 2.60 servings
Japanese Style Fried Rice: 1.00 serving
Pasture Raised Large Brown Eggs: 3.37 servings
Total Cost: $30.01

I would need to spend $0.18 more a week with the new constraint.


To enhance the diversity of my diet, I could make further adjustments to the model. For instance, new food items could be incorporated, each with its unique nutritional profile and cost. 
Moreover, constraints could be implemented to restrict the maximum servings per food item, promoting a more balanced and varied diet. Additionally, integrating preferences or constraints 
pertaining to taste, texture, or dietary limitations could contribute to enriching the variety of my diet solution.

Part 5.

