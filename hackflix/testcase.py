from User import *
from sim import *

u1 = User()
u1.setName("bob")
movies1 = {"sw":4, "ij":5}
u1.setMovies(movies1)

u2 = User()
u2.setName("frank")
movies2 = {"sw":5, "ij":1}
u2.setMovies(movies2)

lineup = u1.movieKey()

tmp1 = u1.ratingVector(lineup)
tmp2 = u2.ratingVector(lineup)

euc(tmp1, tmp2)
