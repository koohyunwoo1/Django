# 데이터베이스와 상호작용하는 부분 ! 데이터베이스 테이블의 구조를 담당하고 데이터를 관리하는 로직을 포함


from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200)  
    created_at = models.DateTimeField(auto_now_add=True)  
    completed = models.BooleanField(default=False)  

    def __str__(self):
        return self.task
