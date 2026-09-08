label house1_pressed:
    scene bg classroom
    "House 1 was pressed!"
    jump after_house_choice

label house2_pressed:
    scene bg classroom
    "House 2 was pressed!"
    jump after_house_choice


label after_house_choice:
    "Tada!"
    return