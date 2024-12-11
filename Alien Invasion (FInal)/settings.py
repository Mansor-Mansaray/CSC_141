class Settings:
    """class to store settings for Alien Invasion"""

    def __init__(self):
   
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128, 0, 32)

        """ship settings"""
        self.ship_limit = 3

        """Bullet settings"""
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (57, 255, 20)
        self.bullets_allowed = 6

        """Clown settings"""
        self.fleet_drop_speed = 16

        """level speed up scale"""
        self.speedup_scale = 1.15
        
        """score scale"""
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize variable settings"""
        self.ship_speed = 5
        self.bullet_speed = 6
        self.alien_speed = 1.0

        """fleet_direction uses a positive 1 represents right and -1 is left"""
        self.fleet_direction = 1

        """Scoring settings"""
        self.alien_points = 100

    def increase_speed(self):
        """increase the values according to levels"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)