from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Address', max_length=300)
    post_code = models.CharField('Postal Code', max_length=12)
    phone = models.CharField('Phone Number', max_length=25)
    web = models.URLField('Website Address')
    email = models.EmailField('Venue Email')

    class Meta:
        managed = False
        db_table = 'Venue'


    def __str__(self):
        return self.name
    
class User(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.f_name + ' ' + self.l_name
    class Meta:
        managed = False
        db_table = 'User'




class Events(models.Model):
    event_id = models.IntegerField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    e_name = models.CharField(db_column='E_name', max_length=255)  # Field name made lowercase.
    org_username = models.ForeignKey('User', models.DO_NOTHING, db_column='Org_username')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'



    def __str__(self):
        return str(self.event_id)