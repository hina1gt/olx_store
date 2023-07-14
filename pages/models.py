from django.db import models

class Clothes(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    def str(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class Electronics(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    def str(self):
        return self.title
    class Meta:
        ordering = ['-id']

class Furnutures(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    def str(self):
        return self.title
    class Meta:
        ordering = ['-id']

class Sports(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    def str(self):
        return self.title
    class Meta:
        ordering = ['-id']

class Households(models.Model):
    class Status(models.TextChoices):
        NEW = 'New', 'NEW'
        USED = 'Used', 'USED'
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='clothes/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    author_num = models.PositiveIntegerField()
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.NEW, blank=True, null=True)
    def str(self):
        return self.title
    class Meta:
        ordering = ['-id']