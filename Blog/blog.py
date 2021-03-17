class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def json(self):
        return {
            'title':self.title,
            'author':self.author,

        }