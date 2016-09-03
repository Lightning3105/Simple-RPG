import pygame as py
import variables as v

class Button(py.sprite.Sprite):

    def __init__(self, text, pos, size, normalcolour, hovercolour, font, ID, centred = False, bsize=(0,0)):
        """
        Create a simple button.
        
        Arguments:
            text <str> -- the button's text
            pos (x, y) -- the position of the button
            size <int> -- the font size of the text
            normalcolour (r, g, b) -- the colour of the button
            hovercolour (r, g, b) -- the colour of the button when it is hovered
            font <str> -- the font file to use (use None for default font)
            ID <str|int> -- a unique identifier for this button
            centred <bool> -- whether the origin of the button is its topleft corner or centre (default=False)
            bsize (w, h) -- a set size for the button (default=(0, 0) - automatic)
        """
        super().__init__()
        self.ID = ID
        self.hovered = False
        self.text = text
        self.pos = pos
        self.hcolour = hovercolour
        self.ncolour = normalcolour
        self.font = font
        self.font = py.font.Font(font, int(size)) #Creates a new font object using font file and font size
        self.centred = centred
        self.size = bsize
        self.rend = self.font.render(self.text, True, (0,0,0)) #Creates a new surface with the text on
        self.set_rect()
    
    def update(self):
        if self.hovered: #Changes the button colour if it is being hovered
            colour = self.hcolour
        else:
            colour = self.ncolour
        py.draw.rect(v.screen, colour, self.rect) #Draws a rectangle
        v.screen.blit(self.rend, self.rect) #Blits the text onto the screen
        if self.rect.collidepoint(py.mouse.get_pos()): #Detects if the mouse is over the button
            self.hovered = True
        else:
            self.hovered = False

    def set_rect(self): #Calculates the size and position of the button
        self.rect = self.rend.get_rect()
        if not self.centred:
            self.rect.topleft = self.pos
        if self.centred:
            self.rect.center = self.pos
        
        if not self.size[0] == 0:
            self.rect.width = self.size[0]
        if not self.size[1] == 0:
            self.rect.height = self.size[1]

    def pressed(self): #Detects if the button is pressed
        for event in v.events:
            if self.hovered:
                if event.type == py.MOUSEBUTTONDOWN:
                    return True
        return False

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color (r, g, b) -- starting color
    gradient (r, g, b) -- final color
    rect <pygame.Rect> -- area to fill (default=Surface's rect)
    vertical <bool> -- True=vertical, False=horizontal (default=True)
    forward <bool> -> True=forward, False=reverse (default=True)

    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = py.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))

class textLabel(py.sprite.Sprite):
    
    def __init__(self, text, pos, colour, font, size, centred=False):
        """
        Create a simple text label.
        
        Arguments:
            text <str> -- the label's text
            pos (x, y) -- the position of the text
            size <int> -- the font size of the text
            colour (r, g, b) -- the colour of the text
            font <str> -- the font file to use (use None for default font)
            centred <bool> -- whether the origin of the text is its topleft corner or centre (default=False)
        """
        super().__init__()
        self.text = text
        self.pos = pos
        self.colour = colour
        self.font = font
        self.size = size
        self.centred = centred
        
    def update(self):
        pos = self.pos
        font = py.font.Font(self.font, self.size) #Creates a new font with given file and size
        label = font.render(self.text, 1, self.colour) #Renders given text with font
        if self.centred:
            #Centres text
            pos = list(self.pos)
            pos[0] -= font.size(self.text)[0] / 2
            pos[1] -= font.size(self.text)[1] / 2
            pos = tuple(pos)
        v.screen.blit(label, pos) #Blits label to screen