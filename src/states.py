import pygame as py #import pygame with a short, easy to type name
import variables as v #import the variables file with a short, easy to type name
import menuItems

def mainMenu(): #define the mainMenu function
    py.init() #initialise pygame
    v.screen = py.display.set_mode((640, 480), py.HWSURFACE|py.DOUBLEBUF|py.RESIZABLE) #create a screen
    
    buttons = py.sprite.Group() #The button sprite group
    buttons.add(menuItems.Button("Play", (320, 240), 50, (0, 0, 255), (0, 100, 200), "assets/fonts/MorrisRoman.ttf", "play", centred=True)) #Create a play button and add it to the buttons group
    
    text = py.sprite.Group() #The text sprite group
    text.add(menuItems.textLabel("Fantasy RPG Tutorial", (320, 150), (255, 255, 0), "assets/fonts/MorrisRoman.ttf", 70, centred=True)) #Create title text
    while True: #This state's game loop
        py.event.pump() #Gets any inputs
        v.events = [] #Clears the events list
        v.events = py.event.get() #Puts all of this tick's events into a public variable
        
        menuItems.fill_gradient(v.screen, (100, 255, 255), (0, 100, 255)) #Fills the screen with a gradient
        
        buttons.update() #Updates and renders every sprite in the 'buttons' group
        text.update() #Updates and renders every sprite in the 'text' group
        
        for button in buttons: #Iterate through the buttons group
            if button.pressed(): #If the button is pressed
                if button.ID == "play": #If the button ID is 'play'
                    print("Play button pressed")
                    playGame() #Run the 'playGame' function
        
        py.display.flip() #Renders the contents of 'v.screen' onto the display