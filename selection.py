import csv

# ======================================
# 1. LOAD MOVIES
# ======================================
movies = {}

with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies[row['movieId']] = {
            'movieId': row['movieId'],
            'title': row['title'],
            'genres': row['genres'],
            'avg_rating': 0,
            'total_ratings': 0,
            'total_tags': 0,
            'imdbId': None
        }

# ======================================
# 2. LOAD RATINGS (Hitung rata-rata)
# ======================================
with open('ratings.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movieId = row['movieId']
        if movieId in movies:
            movies[movieId]['avg_rating'] += float(row['rating'])
            movies[movieId]['total_ratings'] += 1

for movie in movies.values():
    if movie['total_ratings'] > 0:
        movie['avg_rating'] /= movie['total_ratings']

# ======================================
# 3. LOAD TAGS (Hitung jumlah tag)
# ======================================
with open('tags.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movieId = row['movieId']
        if movieId in movies:
            movies[movieId]['total_tags'] += 1

# ======================================
# 4. LOAD LINKS (Ambil imdbId)
# ======================================
with open('links.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movieId = row['movieId']
        if movieId in movies:
            movies[movieId]['imdbId'] = row['imdbId']

# ======================================
# 5. Ubah ke List
# ======================================
data_movies = list(movies.values())

# ======================================
# 6. MENU SORTING
# ======================================
print("Pilih metode sorting:")
print("1. Movie ID (Ascending)")
print("2. Movie ID (Descending)")
print("3. Average Rating (Descending)")
print("4. Average Rating (Ascending)")
print("5. Total Tags (Descending)")
print("6. Title (A-Z)")
print("7. Genre (Z-A)")

pilihan = input("Masukkan pilihan (1-7): ")

# ======================================
# 7. SELECTION SORT MANUAL
# ======================================
n = len(data_movies)

for i in range(n):
    selected_index = i
    
    for j in range(i + 1, n):
        
        # Movie ID Asc
        if pilihan == "1":
            if int(data_movies[j]['movieId']) < int(data_movies[selected_index]['movieId']):
                selected_index = j
        
        # Movie ID Desc
        elif pilihan == "2":
            if int(data_movies[j]['movieId']) > int(data_movies[selected_index]['movieId']):
                selected_index = j
        
        # Rating Desc
        elif pilihan == "3":
            if data_movies[j]['avg_rating'] > data_movies[selected_index]['avg_rating']:
                selected_index = j
        
        # Rating Asc
        elif pilihan == "4":
            if data_movies[j]['avg_rating'] < data_movies[selected_index]['avg_rating']:
                selected_index = j
        
        # Total Tags Desc
        elif pilihan == "5":
            if data_movies[j]['total_tags'] > data_movies[selected_index]['total_tags']:
                selected_index = j
        
        # Title A-Z
        elif pilihan == "6":
            if data_movies[j]['title'] < data_movies[selected_index]['title']:
                selected_index = j
        
        # Genre Z-A
        elif pilihan == "7":
            if data_movies[j]['genres'] > data_movies[selected_index]['genres']:
                selected_index = j

    # Tukar posisi
    data_movies[i], data_movies[selected_index] = data_movies[selected_index], data_movies[i]

# ======================================
# 8. TAMPILKAN 10 DATA TERATAS
# ======================================
print("\nHasil Sorting:\n")

for movie in data_movies[:10]:
    print(f"""
Movie ID     : {movie['movieId']}
Title        : {movie['title']}
Genres       : {movie['genres']}
IMDB ID      : {movie['imdbId']}
Avg Rating   : {round(movie['avg_rating'], 2)}
Total Tags   : {movie['total_tags']}
-------------------------------------
""")