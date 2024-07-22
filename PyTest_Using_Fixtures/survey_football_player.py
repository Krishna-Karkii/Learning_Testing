class FavoritePlayer:
    def __init__(self, question):
        self.question = question
        self.result = []

    def get_question(self):
        return self.question

    def store(self, response):
        self.result.append(response)

    def get_list(self):
        return self.result

