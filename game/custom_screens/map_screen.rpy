label showMap:
    call screen MapUI

screen MapUI:
    add "map/bg map.jpg"

    ## Requires action piece to make it possible to even see hove rappear 
    imagebutton:
        xpos 618
        ypos 570
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action Jump ("house1_pressed")
    
    imagebutton:
        xpos 596
        ypos 165
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action Jump ("house2_pressed")
