class location:

    def __init__(self):
        self.location_Wandering = {}

        def add_wandering(self, wandering, location):
            self.location_wandering[wandering] = location}

            def move_wandering(self, wandering):
                delta_x, delta_y = wandering.walk()
                location_now = self.location_wandering(wandering)
                new_location = location_now_move(delta_x, delta_y)

                self.location_wandering[wandering] = new_location

                def get_location(self, wandering):
                    return self.location_wandering[wandering]