import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Datos de ejemplo (puedes reemplazar esto con un conjunto de datos más realista)
data = {
    'Usuario': [1, 1, 2, 2, 3],
    'Película': ['Pelicula1', 'Pelicula2', 'Pelicula2', 'Pelicula3', 'Pelicula1'],
    'Rating': [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Crear una matriz de usuario-película
matrix = df.pivot_table(index='Usuario', columns='Película', values='Rating')

# Rellenar valores nulos con 0
matrix = matrix.fillna(0)

# Calcular la similitud coseno entre usuarios
user_similarity = cosine_similarity(matrix)

# Crear un modelo de vecinos más cercanos
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(matrix)

def recomendacion_peliculas(usuario, n=1):
    distances, indices = model_knn.kneighbors([matrix.loc[usuario]], n_neighbors=n + 1)
    recommended_movies = []
    for i in range(1, len(distances.flatten())):
        recommended_movies.append((matrix.index[indices.flatten()[i]], distances.flatten()[i]))
    return recommended_movies

# Ejemplo de recomendación para el usuario 1
usuario_ejemplo = 1
recomendaciones = recomendacion_peliculas(usuario_ejemplo, n=2)

print(f"Recomendaciones para el Usuario {usuario_ejemplo}:")
for movie, similarity in recomendaciones:
    print(f"Película: {movie}, Similaridad: {1 - similarity}")
