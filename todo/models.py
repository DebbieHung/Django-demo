from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    # id會自動產生(內建於models)不須另外寫
    # 預設欄位都不可為空(null=False)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    # 建立時間會自動增加，並只有日期
    created = models.DateField(auto_now_add=True)
    # 完成時間要自己去勾選，不能自動增加，可以為空
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)

    # 關連到User資料表 user_id<=>todo_id;user消失資料一起消失
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.created}] {self.title}-({self.user})"
