from django.db import models
from django.urls import reverse

class Clothes(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'clothes_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']

class Electronics(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'elec_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']

class Furnutures(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'fur_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']

class Sports(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'sport_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']

class Households(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'house_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']