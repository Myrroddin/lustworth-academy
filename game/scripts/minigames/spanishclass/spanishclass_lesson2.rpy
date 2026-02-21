default persist.drop_zones = None
default persist.sprites = None

screen spanishclasslesson2:
    add SpanishClassLesson2()

label spanishclass_lesson2:
    play music MUSIC_SPANISH_CLASS
    call screen spanishclasslesson2
    return (_return == 5)

init python:
    import random

    class SpanishClassLesson2(Minigame):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            f = lambda x: round(x * self.scale)

            # Set background
            self.background = self.loadImage('spanishlesson2_background')
            
            # Define image spawns & verbs
            image_spawns = [
                (f(340), f(706)),
                (f(616), f(340)),
                (f(913), f(706)),
                (f(1226), f(374)),
                (f(1538), f(726))
            ]
            verbs = ['jump-saltar', 'fall-caer', 'sleep-dormir', 'yell-gritar', 'pickup-coger']

            # Initialize drop zone data
            if persist.drop_zones is None:
                w, h = (f(232), f(271))
                persist.drop_zones = [
                    {
                        'bounds': pygame.Rect(f(222), f(175), w, h),
                        'answer': verbs[0],
                        'sprite_id': None
                    },
                    {
                        'bounds': pygame.Rect(f(497), f(572), w, h),
                        'answer': verbs[1],
                        'sprite_id': None
                    },
                    {
                        'bounds': pygame.Rect(f(767), f(193), w, h),
                        'answer': verbs[2],
                        'sprite_id': None
                    },
                    {
                        'bounds': pygame.Rect(f(1098), f(575), w, h),
                        'answer': verbs[3],
                        'sprite_id': None
                    },
                    {
                        'bounds': pygame.Rect(f(1423), f(233), w, h),
                        'answer': verbs[4],
                        'sprite_id': None
                    }
                ]
            
            # Initialize sprite data
            if persist.sprites is None:
                persist.sprites = []
                random.shuffle(verbs)
                for i, verb in enumerate(verbs):
                    image = self.loadImage(f'spanishlesson2_{verb}')
                    sprite = GameSprite(image, pivot=(0.5, 0.5))
                    sprite_data = {
                        'verb': verb,
                        'sprite': sprite,
                        'spawn_loc': image_spawns[i],
                        'drop_zone_id': None
                    }
                    persist.sprites.append(sprite_data)

            # self.hovered_image_id = None
            self.dragging_image_id = None
            # self.hovered_drop_zone = None
        
        def _get_image_position(self, sprite_data):
            drop_zone_id = sprite_data['drop_zone_id']
            if drop_zone_id is not None:
                return persist.drop_zones[drop_zone_id]['bounds'].center
            return sprite_data['spawn_loc']

        def _get_image_bounds(self, sprite_data):
            x, y = self._get_image_position(sprite_data)

            sprite = sprite_data['sprite']
            dx, dy, w, h = sprite.bounds
            
            return pygame.Rect(x + dx, y + dy, w, h)

        def _is_mouse_over_image(self, sprite_data):
            bounds = self._get_image_bounds(sprite_data)
            return bounds.collidepoint(self.mousePos)
        
        def _is_mouse_over_drop_zone(self, drop_zone_data):
            bounds = drop_zone_data['bounds']
            return bounds.collidepoint(self.mousePos)

        def _drop_image_in_zone(self, drop_zone_id):
            sprite_id = self.dragging_image_id

            drop_zone_data = persist.drop_zones[drop_zone_id]
            sprite_data = persist.sprites[sprite_id]

            last_zone_id = sprite_data['drop_zone_id']
            old_sprite_id = drop_zone_data['sprite_id']

            if old_sprite_id is not None:
                persist.sprites[old_sprite_id]['drop_zone_id'] = last_zone_id
            
            if last_zone_id is not None:
                persist.drop_zones[last_zone_id]['sprite_id'] = old_sprite_id
            
            sprite_data['drop_zone_id'] = drop_zone_id
            drop_zone_data['sprite_id'] = sprite_id
            
            self.dragging_image_id = None
        
        def _is_game_over(self):
            return all([drop_zone['sprite_id'] is not None for drop_zone in persist.drop_zones])

        def _grade_answers(self):
            score = 0

            for drop_zone_data in persist.drop_zones:
                sprite_id = drop_zone_data['sprite_id']
                user_answer = persist.sprites[sprite_id]['verb']
                if user_answer == drop_zone_data['answer']:
                    score += 1

            return score

        def update(self, dt):
            # Render verb images
            for sprite_id, sprite_data in enumerate(persist.sprites):
                highlight_image = False
                if self._is_mouse_over_image(sprite_data):
                    if self.mousePressed:
                        self.dragging_image_id = sprite_id
                    elif not self.mouseDown:
                        highlight_image = True

                if sprite_id == self.dragging_image_id:
                    x, y = self.mousePos
                else:
                    x, y = self._get_image_position(sprite_data)

                sprite = sprite_data['sprite']
                self.draw(sprite, x, y)

                sprite.highlight = highlight_image
            
            # Handle image drop & drop zone highlights
            if self.dragging_image_id is not None:
                for drop_zone_id, drop_zone_data in enumerate(persist.drop_zones):
                    if not self._is_mouse_over_drop_zone(drop_zone_data):
                        continue
                    
                    if self.mouseReleased:
                        self._drop_image_in_zone(drop_zone_id)
                    else:
                        x, y, w, h = drop_zone_data['bounds']
                        highlight = FillRect('#fff3', (w, h))
                        self.draw(highlight, x=x, y=y)
                
                if self.mouseReleased:
                    self.dragging_image_id = None
            
            # Check for game end
            if self._is_game_over():
                score = self._grade_answers()
                renpy.end_interaction(score)
