from wandering import comunWandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering,  steps):
    begin = location.get_location(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)
        return begin.distance(location.get_location(wandering))

    def simulate_walk(steps, number_attempts, type_wandering):
        wandering = type_wandering(name='Velasquez')
        origin = location(0,0)
        distance = []

        for _ in range(number_attempts)
            track = Track()
            track.add_wandering(wandering, origin)
            simulations_walk = walking(track, wandering, steps)
            distance.append(round(simulations_walk, 1))
            return distance

        def graph(x, y):
            graphs = figure (title = 'Camiino del Errante', x_axis_label='Steps', y_axis_label='Distance')
            graphics.line(x, y, legend='Distance')
            show(graphics)


