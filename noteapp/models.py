from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NOTES(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]

    title = models.CharField(max_length=50)
    status =models.CharField(max_length=2, choices=status_choices)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
    image=models.ImageField(upload_to ='photo',default='default.jpg')
    description =models.CharField(max_length=200)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.title
