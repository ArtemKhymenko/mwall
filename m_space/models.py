from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.ForeignKey(User)
    text = models.TextField(verbose_name='Текст сообщения')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.ForeignKey(User)
    body = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

class CommentComment(models.Model):
    comment = models.ForeignKey(Comment, related_name='commentcomment')
    name = models.ForeignKey(User)
    body = models.TextField(verbose_name='Текст ответа на комментарий')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.comment)
