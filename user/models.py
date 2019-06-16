from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    admin = models.BooleanField(default=False)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f'{self.first_name} ({self.id})'
        
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user', args=[str(self.id)])
