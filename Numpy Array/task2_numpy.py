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

expert_matrix = []
for user in range(5):
    movies_rated_by_me = np.full(200, -1)
    num_movies_rated = random.randint(0, 199)
    movies_that_i_will_rate = random.sample(range(0, 200), num_movies_rated)
    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(1, 5)
    expert_matrix.append(movies_rated_by_me)
expert_matrix = np.array(expert_matrix)

movie_matrix = np.vstack([movie_matrix, expert_matrix])

new_movies_matrix = []
for user in range(55):
    movies_rated_by_me = np.full(20, -1)
    num_movies_rated = random.randint(0, 19)
    movies_that_i_will_rate = random.sample(range(0, 20), num_movies_rated)
    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(1, 5)
    new_movies_matrix.append(movies_rated_by_me)
new_movies_matrix = np.array(new_movies_matrix)

movie_matrix = np.hstack([movie_matrix, new_movies_matrix])

print(movie_matrix.shape)

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(np.amin(arr))
print(np.amax(arr, axis=1))
print(arr.mean())
print(arr.std())
print(np.median(arr))
