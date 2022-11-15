class movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres

    def __dir__(self):
        return {'test': self.id, 'tilte': self.title, 'genres': self.genres}
