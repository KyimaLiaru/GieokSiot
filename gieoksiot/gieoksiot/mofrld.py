from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    # gender = models.CharField(max_length=1) # ex. M, F
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE) # sql 문법은 아직 잘 이해가 안 됨,,
                                                                         # University 라는 외부 키를 가져온다는 뜻

    def __str__(self):
        return self.username


class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name