# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("El")
define a = Character("Alice")

label start:


    scene city

    image el scaled = im.Scale("el default.png", 700, 950)
    show el scaled

    a "You come here often?"
    e "Took you long enough."
    a "I heard you were back in town"
    e "I figured you'd find me if I stayed around here"
    a "Fully robed mages don't exactly vacation here. How was magic academy?"
    e "Better than here. How's the thiefs guild?"
    a "Would you believe I practically run the place?"
    e "Yes, judging by reactions when I asked for you."
    a "You'd make a great thief with a bit of perception like that."
    e "There's magic that let's you read minds."
    a "Not even I believe that one."
    e ""


    return
