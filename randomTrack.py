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
        origin = Track(0,0)
        distance = []

        for _ in range(number_attempts):
            location = location()
            location.add_wandering(wandering, origin)
            simulations_walk = walking(location, wandering, steps)
            distance.append(round(simulations_walk, 1))
            return distance

        def graph(x, y):
            graphics = figure (title = 'Camiino del Errante', x_axis_label='Steps', y_axis_label='Distance')
            graphics.line(x, y, legend='Distance')
            show(graphics)

            def main(distance_walk, number_attempts, type_wandering):
                average_walking_distance = []

                for steps in  distance_walk:
                    distance = simulate_walk(steps, number_attempts, type_wandering)
                    middle_distance = round(sum(distance)/ len(distance), 4)
                    max_distance = max(distance)
                    min_distance = min(distance)
                    average_walking_distance.append(middle_distance)
                    print(f'{type_wandering._name_} Caminata aleatoria de {steps} pasos')
                    print(f'media = {middle_distance}')
                    print(f'max = {max_distance}')
                    print(f'min = {min_distance}')

                    graph(distance_walk, average_walking_distance)

                    if __name__ == '__main__':
                        distance_walk = [10, 100, 1000, 10000]
                        number_attempts = 100
                        main(distance_walk, number_attempts, comunWandering)


                    


