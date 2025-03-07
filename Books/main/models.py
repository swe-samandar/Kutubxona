from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'book'

    def __str__(self):
        return f"{self.title} ({self.author})"