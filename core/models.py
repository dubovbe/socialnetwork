from django.db import models


class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    nickname = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    email = models.EmailField()
    birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'{self.nickname} ({self.first_name} {self.second_name})'

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-id']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    topic = models.CharField(max_length=20)
    text = models.TextField(max_length=2000)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-creation_date']


class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    avatar = models.ImageField(blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    members = models.ManyToManyField(User, related_name='Members')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} ({self.admin})'

    class Meta:
        verbose_name_plural = 'Groups'
        verbose_name = 'Group'
        ordering = ['-creation_date']
