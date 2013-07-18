from pprint import pprint

class DB:

    def __init__(self):
        #constructor
        self.users = []
        self.usermovs = {}
        self.ratings = {}
        self.titlemap = {}

        #keys are users
        #values are lists of
        #movies that user has seen
        self.movies = {}

    def load(self, critdict):
        self.users = critdict.keys();    
        for a in self.users:
            self.usermovs[a] = critdict[a].keys()
        for a in self.users:
            self.ratings[a] = critdict[a]
    
    
    def get_title_map(self, item_path):
        self.tmp_map = {}    
        for line in open(item_path):
            fields = line.split('|')
            self.tmp_map[fields[0]] = fields[1]
        return self.tmp_map

     
    def load(self, item_path, data_path):
        self.titlemap = self.get_title_map(item_path)
        for line in open(data_path):
            fields = line.split('\t')
            if (fields[1] not in self.usermovs):
                self.usermovs[fields[1]] = {}
            self.usermovs[fields[1]][self.titlemap[fields[0]]] = fields[2]
        return self.usermovs
        
    def get_ratings(self, user, movie):
        return self.ratings[user][movie]
        
    def get_movies_for(self, user):
        return self.usermovs[user]
        
    def get_users(self):
        return self.users

if __name__ == '__main__':

    from critics import littledb
    
    db = DB()
    #db.load(littledb)
    #print db.get_ratings("Lisa Rose", "Snakes on a Plane")

    db.load('ml-100k/u.item', 'ml-100k/u.data')
    ''' b = 0
    for key in db.usermovs:
        a = len(db.usermovs[key].values())
        b = b + a
    print b'''
    print db.titlemap['196']
    pprint(db.get_movies_for('242'))
