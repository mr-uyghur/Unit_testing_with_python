class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # convert our post to dictionary (json)
    def json(self):
        return {
            'title':self.title,
            'content':self.content,
        }