from django.db import models

# Create your models here.

from django.db import models

class Train(models.Model):
    case1 = models.TextField()
    case2 = models.TextField()
    case3 = models.TextField()

    def __str__(self):
        return f"Train {self.id, self.case1, self.case2, self.case3}"

#一个表Words，包含了5列，分别是自增的id，word，词性， 实体，出现次数
class Words(models.Model):
    word = models.CharField(max_length=50)
    pos = models.CharField(max_length=50)
    entity = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return f"Words {self.id, self.word, self.pos, self.entity}"

#一个表Sentences，包含了3列，分别是自增的id和sentence、emotion、及其对应的英文翻译
class Sentences(models.Model):
    sentence = models.TextField()
    emotion = models.CharField(max_length=10)
    translation = models.TextField()

    def __str__(self):
        return f"Sentences {self.id, self.sentence}"

#一个表Emotion，包含了3列，分别是自增的id和emotion、count
class Emotion(models.Model):
    emotion = models.CharField(max_length=10)
    count = models.IntegerField()

    def __str__(self):
        return f"Emotion {self.id, self.emotion, self.count}"




