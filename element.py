# Periodic Table Non-Metals Finder
from pyscript import display, document

# List of tuples storing non-metal elements: (Symbol, (Element Name, Atomic Number, Atomic Mass))
elements_list = [
    ("H", ("Hydrogen", 1, 1.008)),
    ("He", ("Helium", 2, 4.0026)),
    ("C", ("Carbon", 6, 12.011)),
    ("N", ("Nitrogen", 7, 14.007)),
    ("O", ("Oxygen", 8, 15.999)),
    ("F", ("Fluorine", 9, 18.998)),
    ("Ne", ("Neon", 10, 20.180)),
    ("P", ("Phosphorus", 15, 30.974)),
    ("S", ("Sulfur", 16, 32.060)),
    ("Cl", ("Chlorine", 17, 35.450)),
    ("Ar", ("Argon", 18, 39.948)),
    ("Se", ("Selenium", 34, 78.971)),
    ("Br", ("Bromine", 35, 79.904)),
    ("Kr", ("Krypton", 36, 83.798)),
    ("I", ("Iodine", 53, 126.90)),
    ("Xe", ("Xenon", 54, 131.29)),
    ("Rn", ("Radon", 86, 222.00))
]

# Dictionary created using dict() from list of tuples
non_metals = dict(elements_list)

# Dictionary mapper for default message when an element is not found
out_mapper = {
    "Not Found": "Element does not exist in the non-metals list."
}


def search_element(event):
    document.getElementById("output").innerHTML = ""

    # Get user input symbol
    symbol = document.getElementById("symbol-input").value.strip().capitalize()

    # Retrieve details tuple using .get()
    details = non_metals.get(symbol, ("Not Found", "N/A", "N/A"))

    # Format result output text using index positions
    result_text = f"Element Symbol: {symbol}<br>Element Name: {details[0]}<br>Atomic Number: {details[1]}<br>Atomic Mass: {details[2]}"

    # Select final text using out_mapper.get() (No if-else statement needed)
    final_output = out_mapper.get(details[0], result_text)

    # Display output using unified PyScript display target
    display(final_output, target="output")