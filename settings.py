class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height= 600
        self.bg_color = (230, 230, 230)
        # Настройка корабля
        self.ship_speed =3
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 17
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_colour = (60, 60, 60)
        self.bullet_allowed = 3
        # Настройки корабля
        self.alien_speed = 10.0
        self.fleet_drop_speed = 1
        # Темп ускорения корабля
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """Инициализирует настройки,измняющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        # fleet_direction = 1 обозначает движение вправо; а -1 влево.
        self.fleet_direction = 1


    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


