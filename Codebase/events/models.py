from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Address', max_length=300)
    post_code = models.CharField('Postal Code', max_length=12)
    phone = models.CharField('Phone Number', max_length=25)
    web = models.URLField('Website Address')
    email = models.EmailField('Venue Email')

    def __str__(self):
        return self.name



class User(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.f_name + ' ' + self.l_name



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField('Manager', max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True)
    event_site = models.TextField(blank=True)
    event_type = models.TextField(blank=True)


    def __str__(self):
        return self.name