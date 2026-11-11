# Working with sets and set operators
from pyscript import display, document

# 4 Predefined sets of club members by grade level (Instruction #4)
grade_7 = {"John Doe", "Jane Smith"}
grade_8 = {"Alice Brown", "Bob White"}
grade_9 = {"Charlie Green", "Diana Prince"}
grade_10 = {"Eve Davis", "Frank Miller"}

def add_member(event):
    document.getElementById("output").innerHTML = ""

    # Get values from text boxes
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value
    
    # Create a set for the new member
    new_member = {f"{first_name} {last_name}"}
    
    # Combine sets using the union operator (|)
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member
    
    # Display the full list of members and total count (Instruction #5)
    display(f"Full List of All Members: {master_set}", target='output')
    display(f"Total Number of Members: {len(master_set)}", target='output')