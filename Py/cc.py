# class practice, class of torso, method of change clothing
class Torso:
    def __init__(self, article):
        self.article = article
    def change(self, newArticle):
        self.article = newArticle
torsoA = Torso.change(None,"Sweater")
print(torsoA.article)