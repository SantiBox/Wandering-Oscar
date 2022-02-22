from wandering import comunWandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering,  steps):
    begin = location.get_location(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)
        return begin.distance(location.get_location(wandering))
