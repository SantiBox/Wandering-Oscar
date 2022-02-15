class Track:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        def mover(self, delta_x, delta_y):
            return Track(self.x + delta_y, self.y + delta_y)

            def distancia(self, other_track):
                delta_x = self_x - other_track.x
                delta_y = self_y - other_track.y

                return (delta_x**2 + delta_y**2)**0.5