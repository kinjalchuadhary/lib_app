from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class LibUser(User):
    PROVINCE_CHOICES = (
        ('AB','Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),

    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    phone = models.IntegerField(null=True)
    postalcode = models.CharField(null=True,blank=True,max_length=7)

class Libitem(models.Model):
    TYPE_CHOICES = (
        ('Book', 'Book'),
        ('DVD','DVD'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Book')
    checked_out=models.BooleanField(default=False)
    user=models.ForeignKey(LibUser, default=None, null=True, blank=True)
    duedate=models.DateField(default=None, null=True, blank=True)
    last_chkout = models.DateField(default=None, null=True, blank=True)
    date_acquired = models.DateField(default=datetime.date.today())
    pubyr = models.IntegerField()
    num_chkout = models.IntegerField(blank=False,default=0)

    def overdue(self):
        if self.checked_out == True and self.duedate < datetime.date.today():
            return 'Yes'
    overdue.short_description = 'Overdue'




class Book(Libitem):
    CATEGORY_CHOICES = (
        (1, 'Fiction'),
        (2, 'Biography'),
        (3, 'Self Help'),
        (4, 'Education'),
        (5, 'Children'),
        (6, 'Teen'),
        (7, 'Other'),
    )
    author = models.CharField(max_length=100)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)

    def __str__(self):
        return self.title + ' by ' + self.author

class Dvd(Libitem):
    maker = models.CharField(max_length=100)
    duration = models.IntegerField()
    rating_choices = (
        (1,'G'),
        (2,'PG'),
        (3,'PG-13'),
        (4,'14A'),
        (5,'R'),
        (6,'NR'),
    )
    rating = models.IntegerField(choices=rating_choices,default=1)

    def __str__(self):
        return self.title + ' by ' + self.maker

class Suggestion(models.Model):

    TYPE_CHOICES = (
        (1, 'Book'),
        (2,'DVD'),
        (3, 'Other'),
    )
    title = models.CharField(max_length=100)
    pubyr = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(default=1, choices=TYPE_CHOICES)
    cost = models.IntegerField()
    num_interested = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username