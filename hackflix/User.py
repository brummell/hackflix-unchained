from collections import OrderedDict
import numpy as np

class User:
    
    def setName(self,name):
        self.name = name

    def setMovies(self, movies):
        self.movies = movies
        
    def movieKey(self):
        return sorted(self.movies.keys())
    
    def ratingVector(self, lineup):
        tmp = []
        for a in lineup:
            tmp.append(self.movies[a])
        ra = np.array(tmp)
        return ra
