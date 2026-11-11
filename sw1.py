# Premium Car Club Member Checker
from pyscript import display, document

def view_user(e):
    document.getElementById('result').innerHTML = ''
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value

    full_name = first_name + ' ' + last_name

    car_members = ['Larry Bird', 'Dejan Laysa', 'SirPogi Ortiz', 'Peyton List', 'Abdul Jabar', 'Jimmmy Butler', 'Piolo Pascual']

    student_checker = full_name in car_members

    display_messege = (f'Sorry {full_name}, your name is not on the Premium Car Club list.', f'Congratulations {full_name}, you are part of the Premium Car Club!')

    display(display_messege[student_checker], target='result')