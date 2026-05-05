import numpy as np
import random

movie_matrix = []

for user in range(50):
    movies_rated_by_me = np.full(200, -1)
    num_movies_rated = random.randint(0, 199)
    movies_that_i_will_rate = random.sample(range(0, 200), num_movies_rated)

    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(1, 5)
    movie_matrix.append(movies_rated_by_me)

movie_matrix = np.array(movie_matrix)
print(movie_matrix)
print('Shape of the array:', movie_matrix.shape)
