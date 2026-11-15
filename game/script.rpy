define e = Character("Bobo")
define n = Character("Narrator")

label start:

    scene intro

    n "Welcome to BOUNCE BACKKKK!"

    scene bobo

    e "Holaaa! I am Bobo."

    e "I get lost in the forest... for 6 months ."

    e "Can you help me find my way home i so scared here and lonely :( ?"

scene forest

menu:
    "Let's start!"

    "Yes!":
        jump question

    "No.":
        e "Oh no! Please help me to find the right way!"
        jump question


label question:

    n "Bobo sees two paths."

    e "Which path should I choose?"

    scene forest and dark path
    
menu:
    "The forest path":
        e "Let's go!"
        jump next_question

    "The dark path":
        e "Oh no! Wrong path!"
        e "Let's try again."
        jump question

label next_question:

    n "Bobo finds a magic crystallllll."

    e "What should I do?"

    scene crystal

menu:
    "Take the crystal":
        e "Great! I found a crystal!"
        jump ending

    "Leave the crystal":
        e "I think I should take it."
        jump next_question


label ending:

    scene jungle to home

    n "Bobo finally finds the way home!"

    e "Thank you for helping me!"

    scene black
    n "Bobo mom finally found boboooo"
    n "They feel really happy when bobo safty"
    return