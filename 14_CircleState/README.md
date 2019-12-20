# Python script to check the state of the circles

### Features:
Checks if the circles are concentric, are tangents to each other or intersect each other at more than one point.

### User input:
#### Takes input for:
                        1)x, y coordinates of centres of circle A, B.
                        2)Length of the radii of circles A, B.
                        
### Algorithm / Thinking process:    
##### 1)First calculate the distance between the centres of the circles:
                      1)C1C2 = math.sqrt((x_1 - x_2)^2 + (y_1 - y_)^2)
##### 2)Now there are three cases:
                                if C1C2 == r_1 + r_2:
                                    print("Circle A and circle B are tangents to each other.")
                                elif C1C2 == 0:
                                    print("Circles A, B are concentric.")
                                elif C1C2 < r_1 + r_2:
                                    print("Circles A, B intersect each other")
                                elif C1C2 > r_1 + r_2:
                                    print("The circles don't intersect.")

### Extras:
##### I used turtle to just draw an image of what happens in the computers brain 