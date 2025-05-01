do_nothing = 0
drink_coffee = 1
drink_beer = 2
sleep = 3

def vadim(step, max_iter=1000):
    """A reference strategy based on a certain PhD student named Vadim"""

    while i < max_iter:
        step(drink_coffee)
        
        for work_idx in range(31):
            step(do_nothing)

        step(sleep)