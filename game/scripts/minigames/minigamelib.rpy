init python:
    import pygame

    def scale_rect(rect, scale):
        x, y, w, h = rect
        return pygame.Rect(x * scale, y * scale, w * scale, h * scale)

    class GameSprite(renpy.Displayable):
        def __init__(self, image, pivot=(0, 0), **kwargs):
            super().__init__(**kwargs)
        
            self.image = image
            self.pivot = pivot
            self.highlight = False

            self._size = None

        def render(self, width, height, st, at):
            x, y, w, h = self.bounds

            nextRender = renpy.Render(w, h)
            nextRender.place(self.image, x=x, y=y)

            if self.highlight:
                fillRect = Fixed(Solid('#fff3'), xsize=w, ysize=h)
                highlight = AlphaMask(fillRect, self.image)
                nextRender.place(highlight, x=x, y=y)

            return nextRender

        @property
        def size(self):
            if self._size is None:
                self._size = renpy.image_size(self.image)
            return self._size
        
        @property
        def bounds(self):
            w, h = self.size
            pivotX, pivotY = self.pivot
            x = -w * pivotX
            y = -h * pivotY
            return pygame.Rect(x, y, w, h)

    class FillRect(renpy.Displayable):
        def __init__(self, color, size, **kwargs):
            super().__init__(**kwargs)

            self.color = color
            self.size = size
        
        def render(self, width, height, st, at):
            w, h = self.size

            nextRender = renpy.Render(w, h)

            solid = Solid(self.color)
            nextRender.place(solid, width=w, height=h)

            return nextRender

    class Minigame(renpy.Displayable):
        DEFAULT_WIDTH = 1920

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background = None

            self.time_base = 0
            self.render_queue = []

            self.mousePos = (0, 0)
            self.mouseDown = False
            self.mousePressed = False
            self.mouseReleased = False

            self.scale = config.screen_width / self.DEFAULT_WIDTH

        def loadImage(self, name):
            return renpy.get_registered_image(name)

        def render(self, width, height, st, at):
            self.nextRender = renpy.Render(width, height)
            if self.background is not None:
                self.nextRender.place(self.background)
            # if time_base got reset to 0, jump back to st
            if self.time_base == 0 and st > 0:
                self.time_base = st
            # calculate delta time
            dt = st - self.time_base
            self.time_base = st
            # update game state
            if dt > 0:
                self.update(dt)
            # handle render queue
            for coord, displayable in self.render_queue:
                subrender = displayable.render(width, height, st, at)
                self.nextRender.blit(subrender, coord)
            self.render_queue = []
            # clear events
            self.mousePressed = False
            self.mouseReleased = False
            # continually update display
            renpy.redraw(self, 0)
            return self.nextRender
        
        def draw(self, sprite, x, y):
            self.render_queue.append(((x, y), sprite))
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEMOTION:
                self.mousePos = (x, y)
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.mouseDown = True
                self.mousePressed = True
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.mouseDown = False
                self.mouseReleased = True
