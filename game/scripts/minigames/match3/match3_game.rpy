define match3.imageDir = 'images/sprites/minigames/match3/'

default match3.grid = None
default match3.bars = None

style match3_recipename is text:
    font 'fonts/Freestyle Script.ttf'
    size 100
    color '#000'
    outlines []

screen match3_minigame(recipe):
    add Match3Game(recipe)

init python:
    import pygame

    class Match3Icon:
        def __init__(self, color):
            self.color = color
            self.image = Image(match3.imageDir + 'icons/match3_{}_icon.webp'.format(self.color))

            self.pos = Vector(0, 0)
            self.inMatch = False
        
        def __eq__(self, other):
            if isinstance(other, Match3Icon):
                return self.color == other.color
            return NotImplemented
    
    class Match3ScoreBar:
        def __init__(self, color):
            self.color = color
            self.value = 0.0
            self.image = Image(match3.imageDir + 'bars/match3_{}_bar.webp'.format(self.color))

    class Match3Game(renpy.Displayable):
        def __init__(self, recipe, **kwargs):
            super(Match3Game, self).__init__(**kwargs)

            self.time_base = 0
            self.numRows = 8
            self.numCols = 8

            self.colors = ['red', 'yellow', 'green', 'blue', 'purple']
            # ensure bars persists between scene reloads
            if match3.bars is None:
                self.scoreBars = [Match3ScoreBar(color) for color in self.colors]
            else:
                self.scoreBars = match3.bars
            match3.bars = self.scoreBars
                
            self.gridBounds = pygame.Rect(896, 56, 968, 960)
            self.background   = Image(match3.imageDir + 'match3_background.webp')
            self.testtubes    = Image(match3.imageDir + 'match3_testtubes.webp')
            self.testtuberack = Image(match3.imageDir + 'match3_testtuberack.webp')
            self.cursor       = Image(match3.imageDir + 'match3_cursor.webp')

            self.recipe = recipe
            self.recipeName = Text(self.recipe['name'], style='match3_recipename')

            # ensure grid persists between scene reloads
            if match3.grid is None:
                self._randomize_grid()
            else:
                self.grid = match3.grid
            match3.grid = self.grid

            self.scoredIcons = []
            self.animating = False
            self.selectedCell = None
            self.mousePos = (0, 0)
            self.mouseDown = False

        def _randomize_grid(self):
            self.grid = [[] for _ in range(self.numCols)]
            for row, col in self._get_cells():
                icon = self._get_random_icon(row, col, allowMatch=False)
                icon.pos = self._get_grid_pos(row, col)
                self.grid[row].append(icon)
        
        def _get_random_icon(self, row, col, allowMatch=True):
            colors = self.colors[:]
            if not allowMatch:
                # prevent vertical matches
                if row > 1:
                    colorU1 = self.grid[row - 1][col].color
                    colorU2 = self.grid[row - 2][col].color
                    if colorU1 == colorU2:
                        colors.remove(colorU1)
                # prevent horizontal matches
                if col > 1:
                    colorL1 = self.grid[row][col - 1].color
                    colorL2 = self.grid[row][col - 2].color
                    if colorL1 == colorL2 and colorL1 in colors:
                        colors.remove(colorL1)
            color = renpy.random.choice(colors)
            icon = Match3Icon(color)
            return icon

        def _get_cells(self):
            cells = tuple((i, j)
                        for i in range(self.numRows) 
                        for j in range(self.numCols))
            return cells

        def render(self, width, height, st, at):
            # if time_base got reset to 0, jump back to st
            if self.time_base == 0 and st > 0:
                self.time_base = st
            self.nextRender = renpy.Render(width, height)
            # draw background, test tubes, recipe name
            self.nextRender.place(self.background)
            self.nextRender.place(self.testtubes)
            self.nextRender.place(self.recipeName, x=250, y=90)
            # draw icons
            self._render_icons()
            # draw test tube rack in front of color bars
            self._render_color_bars()
            self.nextRender.place(self.testtuberack)
            # draw cursors
            self._render_cursor1()
            if self.selectedCell is not None:
                self._render_cursor2()
            # calculate delta time
            dt = st - self.time_base
            self.time_base = st
            # update game state
            self.update(dt)
            # continually update display
            renpy.redraw(self, 0)
            return self.nextRender
        
        def _render_cursor1(self):
            if self.selectedCell is not None:
                row, col = self.selectedCell
                self._place_cursor(row, col)
            else:
                hoveredCell = self._get_hovered_cell()
                if hoveredCell is not None:
                    row, col = hoveredCell
                    self._place_cursor(row, col)
        
        def _render_cursor2(self):
            hoveredCell = self._get_hovered_cell()
            if hoveredCell is not None and self._adjacent_cells(self.selectedCell, hoveredCell):
                hoverRow, hoverCol = hoveredCell
                self._place_cursor(hoverRow, hoverCol)
        
        def _place_cursor(self, row, col):
            gridX, gridY, _, _ = self.gridBounds
            xpos = col * 121 + gridX
            ypos = row * 120 + gridY
            self.nextRender.place(self.cursor, x=xpos, y=ypos)

        def _render_color_bars(self):
            for i in range(len(self.scoreBars)):
                bar = self.scoreBars[i]
                xpos = 72 + i * 152
                yoffset = 336
                ymax = 608
                # target range
                min_, max_ = self.recipe[bar.color]
                ## win range
                ypos = yoffset + round((1.0 - max_ / 100) * ymax)
                ysize = round((max_ - min_) / 100 * ymax)
                color = '#0f09' if bar.value > min_ and bar.value <= max_ else '#0f03'
                winRange = Solid(color, xsize=96, ysize=ysize)
                self.nextRender.place(winRange, x=xpos, y=ypos)
                ## lose range
                ysize = round((100 - max_) / 100 * ymax)
                color = '#f009' if bar.value > max_ else '#f003'
                loseRange = Solid(color, xsize=96, ysize=ysize)
                self.nextRender.place(loseRange, x=xpos, y=yoffset)
                # current value
                ysize = round(bar.value / 100 * ymax)
                colorBar = Transform(bar.image, ysize=ysize)
                ypos = yoffset + ymax - ysize
                self.nextRender.place(colorBar, x=xpos, y=ypos)
        
        def _render_icons(self):
            for row, col in self._get_cells():
                icon = self.grid[row][col]
                x, y = icon.pos - Vector(60, 60)
                self.nextRender.place(icon.image, x=x, y=y)
            for icon in self.scoredIcons:
                x, y = icon.pos - Vector(60, 60)
                self.nextRender.place(icon.image, x=x, y=y)

        def update(self, dt):
            if dt == 0:
                return
            
            self.animating = False

            # move out-of-place icons into position
            cells = self._get_cells()
            for row, col in cells:
                icon = self.grid[row][col]
                targetPos = self._get_grid_pos(row, col)
                if targetPos != icon.pos:
                    dist = (targetPos - icon.pos).magnitude()
                    step = 1000 * dt
                    if dist < step:
                        icon.pos = targetPos
                    else:
                        self.animating = True
                        dir = (targetPos - icon.pos) / dist
                        icon.pos += step * dir
            
            # move scored icons to their respective test tubes
            for i in range(len(self.scoredIcons) - 1, -1, -1):
                icon = self.scoredIcons[i]
                posX, posY = icon.pos
                colorIdx = self.colors.index(icon.color)
                targetX = 120 + colorIdx * 152
                targetY = 270
                if not hasattr(icon, 'pathParams'):
                    icon.pathParams = self._get_path_params(posX, posY, targetX, targetY)
                a, h, k = icon.pathParams
                dist = abs(targetX - posX)
                step = 2500 * dt
                if dist < step:
                    self.scoredIcons.pop(i)
                    self.scoreBars[colorIdx].value += 2.0
                    # cap at 100%
                    if self.scoreBars[colorIdx].value > 100.0:
                        self.scoreBars[colorIdx].value = 100.0
                    posX = targetX
                    posY = targetY
                else:
                    self.animating = True
                    dir = (targetX - posX) / dist
                    # maintain a (close to) constant speed
                    dydx = 2 * a * (posX - h)
                    dx = step / math.sqrt(1 + dydx ** 2) * dir
                    posX += dx
                    posY += dydx * dx
                icon.pos = Vector(posX, posY)
            
            # let animations play out before continuing with game logic
            if self.animating:
                return
            
            # check for game end
            won = True
            for bar in self.scoreBars:
                min_, max_ = self.recipe[bar.color]
                if bar.value < min_:
                    won = False
                elif bar.value > max_:
                    renpy.end_interaction(False) # loss
            if won:
                renpy.end_interaction(True) # win

            # remove matches
            matches = self._get_matches()
            for match in matches:
                for row, col in match:
                    icon = self.grid[row][col]
                    if icon is not None:
                        self.scoredIcons.append(icon)
                    self.grid[row][col] = None

            # shift icons down
            for row, col in cells[::-1]:
                count = 0
                while self.grid[row][col] is None:
                    count += 1
                    # shift all icons in the column down 1
                    for i in range(row, 0, -1):
                        self.grid[i][col] = self.grid[i - 1][col]
                    # add new icon at the top of the column
                    newIcon = self._get_random_icon(row, col)
                    newIcon.pos = self._get_grid_pos(-count, col)
                    self.grid[0][col] = newIcon

        def _get_path_params(self, x1, y1, x2, y2):
            k = 60
            c = math.sqrt((y2 - k) / (y1 - k))
            h = (c * x1 + x2) / (c + 1)
            a = (y1 - k) / (x1 - h) ** 2
            return (a, h, k)

        def _get_grid_pos(self, row, col):
            gridX, gridY, _, _ = self.gridBounds
            x = col * 121 + gridX + 60
            y = row * 120 + gridY + 60
            return Vector(x, y)

        def _swap_cells(self, cell1, cell2):
            row1, col1 = cell1
            row2, col2 = cell2
            color1 = self.grid[row1][col1]
            color2 = self.grid[row2][col2]
            self.grid[row1][col1] = color2
            self.grid[row2][col2] = color1

        def _get_matches(self):
            horizMatches = self._get_horiz_matches()
            vertMatches = self._get_vert_matches()
            return horizMatches | vertMatches

        def _get_horiz_matches(self):
            matches = set()
            for row in range(self.numRows):
                # only need to check every third cell
                # since minimum match length is 3
                for col in range(0, self.numCols, 3):
                    match = self._get_horiz_match(row, col)
                    if len(match) >= 3:
                        matches.add(match)
            return matches

        def _get_horiz_match(self, row, col):
            match = [(row, col)]
            icon = self.grid[row][col]
            # look left
            stop = max(0, col - 4)
            for i in range(col - 1, stop - 1, -1):
                if self.grid[row][i].color != icon.color:
                    break
                match.insert(0, (row, i))
            # look right
            stop = min(7, col + 4)
            for i in range(col + 1, stop + 1):
                if self.grid[row][i].color != icon.color:
                    break
                match.append((row, i))
            return tuple(match)

        def _get_vert_matches(self):
            matches = set()
            for col in range(self.numCols):
                # only need to check every third cell
                # since minimum match length is 3
                for row in range(0, self.numRows, 3):
                    match = self._get_vert_match(row, col)
                    if len(match) >= 3:
                        matches.add(match)
            return matches

        def _get_vert_match(self, row, col):
            match = [(row, col)]
            icon = self.grid[row][col]
            # look up
            stop = max(0, row - 4)
            for i in range(row - 1, stop - 1, -1):
                if self.grid[i][col].color != icon.color:
                    break
                match.insert(0, (i, col))
            # look down
            stop = min(7, row + 4)
            for i in range(row + 1, stop + 1):
                if self.grid[i][col].color != icon.color:
                    break
                match.append((i, col))
            return tuple(match)
        
        def _adjacent_cells(self, cell1, cell2):
            row1, col1 = cell1
            row2, col2 = cell2
            return ((row1 == row2 and abs(col2 - col1) == 1)
                or (col1 == col2 and abs(row2 - row1) == 1))

        def _get_hovered_cell(self):
            if not self.gridBounds.collidepoint(self.mousePos):
                return None
            mouseX, mouseY = self.mousePos
            gridX, gridY, _, _ = self.gridBounds
            row = (mouseY - gridY) // 121
            col = (mouseX - gridX) // 120
            return (row, col)

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEMOTION:
                self.mousePos = (x, y)
            if not self.animating:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseDown = pygame.mouse.get_pressed()[0]
                elif ev.type == pygame.MOUSEBUTTONUP:
                    self.mouseDown = pygame.mouse.get_pressed()[0]
                    hoveredCell = self._get_hovered_cell()
                    if self.selectedCell is None:
                        self.selectedCell = hoveredCell
                    else:
                        if hoveredCell is not None and self._adjacent_cells(self.selectedCell, hoveredCell):
                            self._swap_cells(self.selectedCell, hoveredCell)
                        self.selectedCell = None
            # reduce freezing on web version
            if st - self.time_base > 0.25:
                renpy.restart_interaction()
            return None
        
        def visit(self):
            return []
