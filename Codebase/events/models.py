from django.db import models
import base64

class Affiliated(models.Model):
    group_id = models.IntegerField(db_column='Group_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Group_ID, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey('Events', models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Affiliated'
        unique_together = (('group_id', 'event'),)

class ArrangesVendor(models.Model):
    v_name = models.OneToOneField('Vendors', models.DO_NOTHING, db_column='V_name', primary_key=True)  # Field name made lowercase. The composite primary key (V_name, Org_username) found, that is not supported. The first column is selected.
    org_username = models.ForeignKey('User', models.DO_NOTHING, db_column='Org_username')  # Field name made lowercase.
    booth_no = models.IntegerField(db_column='Booth_no')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arranges_Vendor'
        unique_together = (('v_name', 'org_username'),)


class Attends(models.Model):
    u_username = models.CharField(db_column='U_username', primary_key=True, max_length=255)  # Field name made lowercase. The composite primary key (U_username, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey('Events', models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attends'
        unique_together = (('u_username', 'event'),)


class Dates(models.Model):
    date_code = models.DateField(db_column='Date_Code', primary_key=True)  # Field name made lowercase.
    no_of_events = models.CharField(db_column='No_of_Events', max_length=255, blank=True, null=True)  # Field name made lowercase.
    events_occuring = models.CharField(db_column='Events_Occuring', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dates'


class Events(models.Model):
    event_id = models.IntegerField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    e_name = models.CharField(db_column='E_name', max_length=255)  # Field name made lowercase.
    org_username = models.ForeignKey('User', models.DO_NOTHING, db_column='Org_username')  # Field name made lowercase.
    venue_add = models.ForeignKey('LocationsVenue', models.DO_NOTHING, db_column='Venue_add')  # Field name made lowercase.
    e_site = models.CharField(db_column='E_site', max_length=255)  # Field name made lowercase.
    e_desc = models.CharField(db_column='E_desc', max_length=255)  # Field name made lowercase.
    e_date = models.DateTimeField(db_column='E_date')  # Field name made lowercase.
    e_category = models.CharField(db_column='E_category', max_length=255)  # Field name made lowercase.
    e_img = models.ImageField(upload_to='e_img/', null=True, blank=True, db_column='Event_img')

    def get_image(self):
        if self.e_img:
            return base64.b64encode(self.e_img).decode('utf-8')
        return None
    
    class Meta:
        managed = False
        db_table = 'Events'


class Guest(models.Model):
    guest_id = models.AutoField(db_column='Guest_ID', primary_key=True)  # Auto-incrementing primary key
    g_type = models.CharField(db_column='G_Type', max_length=255)
    g_name = models.CharField(db_column='G_name', max_length=255)
    g_info = models.TextField(db_column='G_info')

    class Meta:
        managed = False
        db_table = 'Guest'


class HasGuests(models.Model):
    guest = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Guest_ID, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Has_Guests'
        unique_together = (('guest', 'event'),)


class HasVendors(models.Model):
    v_name = models.ForeignKey('Vendors', models.DO_NOTHING, db_column='V_name', primary_key=True)  # Field name made lowercase. The composite primary key (V_name, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Has_Vendors'
        unique_together = (('v_name', 'event'),)


class IsAt(models.Model):
    l_address = models.ForeignKey('LocationsVenue', models.DO_NOTHING, db_column='L_Address', primary_key=True)  # Field name made lowercase. The composite primary key (L_Address, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Is_at'
        unique_together = (('l_address', 'event'),)


class IsOn(models.Model):
    date_code = models.OneToOneField(Dates, models.DO_NOTHING, db_column='Date_Code', primary_key=True)  # Field name made lowercase. The composite primary key (Date_Code, Event_ID) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Is_on'
        unique_together = (('date_code', 'event'),)


class LocationsVenue(models.Model):
    address = models.CharField(db_column='Address', primary_key=True, max_length=255)  # Field name made lowercase.
    l_owner = models.ForeignKey('User', models.DO_NOTHING, db_column='L_Owner')  # Field name made lowercase.
    l_name = models.CharField(db_column='L_Name', max_length=255)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.
    province_state = models.CharField(db_column='Province_state', max_length=255)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Locations_Venue'


class PartOf(models.Model):
    group = models.ForeignKey('UserGroups', models.DO_NOTHING, db_column='Group_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Group_ID, Username) found, that is not supported. The first column is selected.
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='Username')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Part_of'
        unique_together = (('group', 'username'),)


class Profile(models.Model):
    u_username = models.ForeignKey('User', models.DO_NOTHING, db_column='U_Username', db_comment='Username [->User] (req)')  # Field name made lowercase.
    attended_events = models.CharField(db_column='Attended_Events', max_length=255, blank=True, null=True, db_comment='Attended Events (opt)')  # Field name made lowercase.
    saved_events = models.CharField(db_column='Saved_Events', max_length=255, blank=True, null=True, db_comment='Saved Events (opt)')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profile'


class User(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=255, db_comment='Username (req)')  # Field name made lowercase.
    f_name = models.CharField(db_column='F.name', max_length=255, db_comment='First Name (req)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_name = models.CharField(db_column='M.Name', max_length=255, blank=True, null=True, db_comment='Middle Name (opt)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l_name = models.CharField(db_column='L.Name', max_length=255, db_comment='Last Name (req)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=255, db_comment='Email (req)')  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', db_comment='Birthday (req)')  # Field name made lowercase.
    ord_flag = models.IntegerField(db_column='Ord_flag', blank=True, null=True, db_comment='Ord Flag? (opt)')  # Field name made lowercase.
    org_id = models.IntegerField(db_column='Org_ID', blank=True, null=True, db_comment='Org ID (opt)')  # Field name made lowercase.

    USERNAME_FIELD = 'email'

    def set_password(self, force_pass):
        pass

    class Meta:
        managed = False
        db_table = 'User'


class UserGroups(models.Model):
    group_id = models.AutoField(db_column='Group_ID', primary_key=True)  # Field name made lowercase.
    ug_name = models.CharField(db_column='UG_Name', max_length=255)  # Field name made lowercase.
    g_desc = models.CharField(db_column='g_desc', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User_Groups'


class Vendors(models.Model):
    c_name = models.CharField(db_column='C_name', primary_key=True, max_length=255)  # Field name made lowercase.
    c_owner = models.CharField(db_column='C_owner', max_length=255)  # Field name made lowercase.
    types_of_product = models.CharField(db_column='Types_of_Product', max_length=255)  # Field name made lowercase.
    v_address = models.CharField(db_column='V_address', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendors'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
