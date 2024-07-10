from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    """Таблица с темами, которые изучает пользователь"""
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='topics', null=True, default=None)
    
    def __str__(self) -> str:
        """Возвращает строковое представление модели"""
        return self.title
    
    
class Entry(models.Model):
    """Записи в каждой теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entries')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self) -> str:
        """Возвращает строковое представление модели"""
        return self.text