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

LLM Implementation: ChatGPT

I have chosen to use ChatGPT for Part 5 to see if this LLM is capable of being a useful tool to assist with this assignment.

ChatGPT URL: https://chat.openai.com/

Step-by-step review of implementation:

1. Opened up ChatGPT via the URL provided and started to prompt. 
2. The first prompt I provided was "You are a data science master's student in a decision analytics class. You are tasked with the problem below. Please specify a model for The Diet Problem 
and create a linear programming model that finds the optimal solution, that is to find the optimal servings of five food items at the minimal cost. Where there is a variable I must fill in, 
please indicate it so I can update it with the correct information."
3. After the prompt, I provided the assignment details.
4. Next, ChatGPT was able to construct a response for Part 1 but did not continue with Parts 2, 3, and 4 so I asked to continue with those parts.
5. ChatGPT then provided me with the code for my linear programming model and was also able to add the additional constraint from Part 4.

ChatGPT was able to develop the Python code needed to solve this problem. It was successful in understanding my problem and was able to provide not only the code but the write-ups, for 
example in Part 2 explaining the problem and creating a sort of template that I would need to just go into and fill in my appropriate information. Some successes was that ChatGPT caught that 
we were supposed to satisfy a weekly diet so it knew to multiply the daily required values by 7. The only failure which was not really a failure was that I had to continue to prompt ChatGPT
to finish answering all the parts of the assignment. Overall, the conversation was seamless and did not require too much tailoring. I was impressed that ChatGPT was able to understand information
very quickly and efficiently to produce a backbone or jumping-off point for this assignment. I also used PuLP for my problem so it was easy for me to understand the code it produced. 
I believe I could have continued to prompt ChatGPT to complete the full assignment if I provided the information about my five food items. ChatGPT is very capable of doing this assignment and 
assignments like this as it can effectively understand the situation and understand more information to construct the solution. 

COMPLETE CONVERSATION:

Diet LP Model: Python.
User
You are a data science master's student in a decision analytics class. You are tasked with the problem below. Please specify a model for The Diet Problem and create a linear programming model that finds the optimal solution, that is to find the optimal servings of five food items at the minimal cost. Where there is a variable I must fill in, please indicate it so I can update it with the correct information.  Problem: The Diet Problem Revisited (version 11)

Developed by Thomas W. Miller. Revised March 20, 2024.

Introduced by Stigler (1945) and discussed by Dantzig (1990), the diet problem is a classic problem in constrained optimization often used to introduce linear programming concepts. The diet problem has been studied extensively through the years (van Dooren 2018).

For this assignment, you need to construct a personalized diet using current recommended dietary allowances from the U.S. Food and Drug Administration, updated to account for recent research on sodium intake and health (Mente, O'Donnell, and Yusuf 2021). Interested in learning more about nutrition and healthy living? Check out Nutrients, an open-access journal, at its home page https://www.mdpi.com/journal/nutrientsLinks to an external site. .

The constraints for this linear programming problem, should consider seven components of nutrition and their daily values, as shown in the following table:

Component

Max/Min

Daily Amount and measure

Sodium

Maximum

5,000 milligrams (mg)

Energy

Minimum

2,000 Calories (kilocalories, kcal)

Protein

Minimum

50 grams (g)

Vitamin D

Minimum

20 micrograms (mcg)

Calcium

Minimum

1,300 milligrams (mg)

Iron

Minimum

18 milligrams (mg)

Potassium

Minimum

4,700 milligrams (mg)

Set this up as a standard linear programming problem with decision variables taking any non-negative values. In other words, partial servings are permitted.  

For nutritional constraints, consider setting these to satisfy a weekly diet. That is, multiply each daily requirement by seven (7).

Nutrition labels on packaged foods should contain information about these eight components of nutrition along with other components. Each of the components represents a constraint in the linear programming problem you are developing.

To adapt the problem to your personal diet, collect nutrition facts from five packaged food items in your household. Use packaged foods that are part of your normal diet and for which you have prices. Also, ensure that the across the set of food items there are positive values for each of the eight components of nutrition. Adjust the price for each food item so that it represents one serving size, as defined on the nutrition facts label. Each food item represents a decision variable in the linear programming problem.

The goal or objective of this problem is to find the minimum-cost diet (servings of food items) that satisfies the eight nutritional requirements. Use Python PuLP or AMPL (perhaps with its Python API). 

Deliverables (150 points total, 30 points for each part)

Paper (pdf file in GitHub repository). The paper/write-up should be submitted as a pdf file (two pages max for text, appendices for tables, figures, and images do not count in the two-page max). Think of the paper as comprising the methods and results sections of a written research report. If you like, provide a paragraph on methods and a paragraph about results for each of the five parts of this assignment. As this is an individual assignment about your personal eating habits, it is fine to use the first person in writing this paper. 

Program code (text link/URL to GitHub repository). Key information from the paper should also be included in the README.md markdown file of a public GitHub repository established by the student for this assignment. The GitHub repository should include text files for the program code, and program output, Image files (.jpg or .png extension) should be included for the scanned food labels may also be included in the repository. Include the web address text (URL) for the GitHub repository in the comments form of the assignment posting.  You should be providing a link to a separate repository that can be cloned. It should end with the .git extension.

This assignment has five graded components, with each component worth 30 points:

Part 1. Provide documentation for the five packaged food items you have selected for the assignment. Photographs of the Nutrition Facts labels are sufficient. Show your price calculations for serving sizes. [If you cook meals for yourself and prefer not to use packaged food items in this assignment, see the Assignment Addendum below.]
Part 2. Specify the linear programming problem in standard form, showing decision variables, objective function with cost coefficients, and weekly nutritional constraints. Describe the problem in plain English. Implement the linear programming problem using Python PuLP or AMPL. Provide the program code and output/listing as plain text files, posting within a GitHub repository dedicated to this assignment. 
Part 3. Solve the linear programming problem using your Python PuLP or AMPL code. Describe the solution, showing units (serving sizes) for each of the five food items. What is the minimum cost solution? How much would you need to spend on food each week? Include the text file (listing) of your solution in the GitHub repository.
Part 4. Solutions to the diet problem are notorious for their lack of variety. Suppose you require at least one serving of each food item or meal during the week, setting constraints in the diet problem accordingly. Solve the revised linear programming problem. How do these additional constraints change the solution? How much more would you have to spend on food each week? Include the text file (listing) of your solution of this revised problem in the GitHub repository. Suppose this diet solution continues to lack variety. Describe how could you add further variety to your diet by making additional revisions to the model specification.
ChatGPT
To tackle this problem, we need to define a linear programming model that minimizes the cost of the diet while satisfying the given nutritional constraints. Let's denote the decision variables as \( x_1, x_2, x_3, x_4, x_5 \), representing the servings of the five food items respectively. The objective function will be to minimize the total cost, which will be the sum of the cost of each food item multiplied by its servings. The constraints will ensure that the total nutritional intake from the diet meets or exceeds the recommended daily allowances for each nutrient.

Let's define the problem more formally:

**Decision Variables:**
- \( x_1, x_2, x_3, x_4, x_5 \): Servings of food items 1, 2, 3, 4, and 5 respectively.

**Objective Function:**
Minimize the total cost:
\[ \text{Minimize} \quad  c_1x_1 + c_2x_2 + c_3x_3 + c_4x_4 + c_5x_5 \]
Where \( c_1, c_2, c_3, c_4, c_5 \) are the costs per serving of food items 1, 2, 3, 4, and 5 respectively.

**Nutritional Constraints:**
1. Sodium: \( 0.005x_1 + 0.005x_2 + 0.005x_3 + 0.005x_4 + 0.005x_5 \geq 35,000 \)
2. Energy: \( E_1x_1 + E_2x_2 + E_3x_3 + E_4x_4 + E_5x_5 \geq 14,000 \)
3. Protein: \( P_1x_1 + P_2x_2 + P_3x_3 + P_4x_4 + P_5x_5 \geq 350 \)
4. Vitamin D: \( VD_1x_1 + VD_2x_2 + VD_3x_3 + VD_4x_4 + VD_5x_5 \geq 140 \)
5. Calcium: \( Ca_1x_1 + Ca_2x_2 + Ca_3x_3 + Ca_4x_4 + Ca_5x_5 \geq 9,100 \)
6. Iron: \( Fe_1x_1 + Fe_2x_2 + Fe_3x_3 + Fe_4x_4 + Fe_5x_5 \geq 126 \)
7. Potassium: \( K_1x_1 + K_2x_2 + K_3x_3 + K_4x_4 + K_5x_5 \geq 32,900 \)

Where \( E_i, P_i, VD_i, Ca_i, Fe_i, K_i \) are the energy, protein, vitamin D, calcium, iron, and potassium content per serving of food item \( i \) respectively.

We would set up this linear programming problem in Python using the PuLP library. Then we'd solve it to find the optimal servings of each food item and the minimum cost of the diet.

For Part 2 and Part 3 of the assignment, we'll implement the Python code using PuLP to set up and solve the linear programming problem, and then describe the solution and minimum cost. For Part 4, we'll modify the constraints to include the requirement of at least one serving of each food item during the week and observe how it affects the solution.
User
Please continue with doing parts 2,3, and 4
ChatGPT
Sure, let's continue with Parts 2, 3, and 4.

**Part 2: Specifying the Linear Programming Problem and Implementing the Code**

We'll use the PuLP library in Python to set up and solve the linear programming problem. Below is the Python code to accomplish this:

```python
import pulp

# Create a LP Minimization problem
prob = pulp.LpProblem("Diet_Problem", pulp.LpMinimize)

# Define decision variables
x1 = pulp.LpVariable("Food_Item_1", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Food_Item_2", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("Food_Item_3", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("Food_Item_4", lowBound=0, cat='Continuous')
x5 = pulp.LpVariable("Food_Item_5", lowBound=0, cat='Continuous')

# Define cost coefficients
costs = [1.25, 0.75, 2.00, 1.50, 1.00]  # Example cost per serving for each food item

# Define nutritional content per serving for each food item
nutritional_content = {
    "Food_Item_1": [100, 10, 5, 2, 3, 200],  # [Energy, Protein, Vitamin D, Calcium, Iron, Potassium]
    "Food_Item_2": [150, 8, 3, 1, 2, 250],
    "Food_Item_3": [120, 15, 6, 4, 5, 300],
    "Food_Item_4": [90, 20, 4, 3, 4, 180],
    "Food_Item_5": [80, 12, 7, 3, 2, 150]
}

# Add objective function to minimize cost
prob += sum(costs[i]*[x1, x2, x3, x4, x5][i] for i in range(5)), "Total Cost"

# Add nutritional constraints
daily_requirements = [14000, 350, 140, 9100, 126, 32900]  # Energy, Protein, Vitamin D, Calcium, Iron, Potassium
for j in range(6):
    prob += sum(nutritional_content[item][j] * [x1, x2, x3, x4, x5][i] for i, item in enumerate([x1, x2, x3, x4, x5])) >= daily_requirements[j]

# Solve the problem
prob.solve()

# Print the results
print("Optimal servings of food items:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("\nMinimum cost of the diet: $", pulp.value(prob.objective))
```

**Part 3: Solving the Linear Programming Problem**

After running the above code, we get the optimal servings of each food item and the minimum cost of the diet.

**Part 4: Adding Constraints for Variety**

To ensure variety in the diet, we'll add constraints that require at least one serving of each food item per week. We'll modify the constraints accordingly and solve the revised problem.

```python
# Add additional constraints for variety
for item in [x1, x2, x3, x4, x5]:
    prob += item >= 1  # At least one serving of each food item per week

# Solve the revised problem
prob.solve()

# Print the results
print("Revised optimal servings of food items:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("\nRevised minimum cost of the diet: $", pulp.value(prob.objective))
```

By adding these constraints, we ensure that the solution includes at least one serving of each food item per week, thus adding variety to the diet. We then print the revised optimal servings of each food item and the corresponding minimum cost of the diet.

This completes Parts 2, 3, and 4 of the assignment. The Python code provided can be run to obtain the optimal solution to the diet problem, both with and without constraints for variety.
