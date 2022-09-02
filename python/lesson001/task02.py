# Напишите программу для проверки истинности утверждения:
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = [0, 1]
y = [0, 1]
z = [0, 1]

# form output header
header_str = f"{'X'}\t{'Y'}\t{'Z'}\t"
header_str += f"{'XvY'}\t{'XvYvZ'}\t{'¬(XvYvZ)'}  "
header_str += f"{'¬X'}\t{'¬Y'}\t{'¬Z'}\t"
header_str += f"{'¬Xv¬Y'}\t"
header_str += f"{'¬X⋀¬Y⋀¬Z'}\t"
header_str += f"¬(XvYvZ) = ¬X⋀¬Y⋀¬Z"

print(header_str)

for item_x in x:
    for item_y in y:
        for item_z in z:      
            
            # Left expression
            x_or_y = item_x or item_y # X ⋁ Y
            x_or_y_or_z = x_or_y or item_z # X ⋁ Y ⋁ Z
            left_expression = not x_or_y_or_z # ¬(X ⋁ Y ⋁ Z)
            
            # Right expression
            not_x = not item_x # ¬X
            not_y = not item_y # ¬Y
            not_z = not item_z # ¬Z
            not_x_or_not_y = not_x or not_y # ¬X ⋀ ¬Y
            right_expression = not_x_or_not_y or not_z # ¬X ⋀ ¬Y ⋀ ¬Z

            # Form output str
            output_str = f"{item_x}\t{item_y}\t{item_z}\t "
            output_str += f"{int(x_or_y)}\t  "
            output_str += f"{int(x_or_y_or_z)}\t    "
            output_str += f"{int(left_expression)}\t   "

            output_str += f"{int(not_x)}\t "
            output_str += f"{int(not_y)}\t "
            output_str += f"{int(not_z)}\t  "
            output_str += f"{int(not_x_or_not_y)}\t    "
            output_str += f"{int(right_expression)}\t\t\t "
            output_str += f"{int(left_expression == right_expression)}"
            
            print(output_str)
