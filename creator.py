# Meet the Creator Interactive Profile Script
import random
from pyscript import display, document

def get_random_hobby(event):
    document.getElementById("creator-output").innerHTML = ""

    hobbies = [
        "Dejan is super passionate about cars, airplanes, and anything that moves!",
        "Dejan actively competes in duathlons (running + cycling).",
        "Dejan plays Valorant in his free time.",
        "Dejan plays badminton and is currently trying out basketball!"
    ]

    #Random fact choosing
    chosen_fact = random.choice(hobbies)
    display(f"🏎️ {chosen_fact}", target="creator-output")