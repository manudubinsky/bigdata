#!/usr/bin/python

import h5py
from collections import Counter
from collections import defaultdict
import numpy as np
import math

#f = h5py.File('new.h5','r')
f = h5py.File('book.h5','r')

grp = f["data"]
data = grp["int0"]
(x,y) = data.shape
print str(x) + "," + str(y)
i = 0
libros= []
usuarios= []
user=''
i=0

while (i<2000):
        user=str(data[0][i])
        books=[]
        while (i<y and user== str(data[0][i])):
                books.append((data[1][i]))
                i=i+1
                print i
        usuarios.append(user)
        libros.append((books))

popular_books = Counter(books
                        for libros in libros
                        for books in libros).most_common()


def most_popular_new_interests(libros, max_results=5):
    suggestions = [(libro, frequency)
		   for libro, frequency in popular_books
		   if libro not in libros]
    return suggestions[:max_results]


def cosine_similarity(v, w):
    return np.dot(v, w) / math.sqrt(np.dot(v, v) * np.dot(w, w)) 

unique_libros = sorted(list({ libro
				 for libros in libros
				 for libro in libros }))

def make_user_libros_vector(libros):
    return [1 if libro in libros else 0
	    for libro in unique_libros]

user_libro_matrix = map(make_user_libros_vector, libros)



user_similarities = [[cosine_similarity(libros_vector_i, libros_vector_j)
		      for libros_vector_j in user_libro_matrix]
		     for libros_vector_i in user_libro_matrix]

i=0
for a in user_similarities:
        print i
        print a
        i=i+1


def most_similar_users_to(user_id):
    pairs = [(other_user_id, similarity)
	     for other_user_id, similarity in
		 enumerate(user_similarities[user_id])
	     if user_id != other_user_id and similarity > 0]
    
    resultado = sorted(pairs,
		  key=lambda (_, similarity): similarity,
		  reverse=True)

    cantidad_muestra = 5
    return resultado[:cantidad_muestra]

usuario=264

print most_similar_users_to(usuario)


def user_based_suggestions(user_id, include_current_interests=False):
    # sum up the similarities
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_id):
            for interest in libros[other_user_id]:
                    suggestions[interest] += similarity
	    
    # convert them to a sorted list
    suggestions = sorted(suggestions.items(),
			 key=lambda (_, weight): weight,
			 reverse=True)
    
    # and (maybe) exclude already-interests
    if include_current_interests:
            return suggestions
    else:
            return [(suggestion, weight)
                    for suggestion, weight in suggestions
                    if suggestion not in libros[user_id]]
#print user_based_suggestions(usuario)
