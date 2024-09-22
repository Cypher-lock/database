# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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

class Softmatterdata(models.Model):
    identifier = models.AutoField(primary_key=True)
    composition = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    name = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    acquired = models.DateField()
    lastupdate = models.DateField(auto_now=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    lock = models.BooleanField(blank=True, null=True, default=False)
    sample_image = models.ImageField(null=True, blank=True, upload_to="images/")
    meta_data = models.FileField(null=True, blank=True, upload_to="metadata/")
    additional_resources1 = models.FileField(null=True, blank=True, upload_to="add_rec/")
    additional_resources2 = models.FileField(null=True, blank=True, upload_to="add_rec/")
    additional_resources3 = models.FileField(null=True, blank=True, upload_to="add_rec/")
    barcode = models.FileField(null=True, blank=True, upload_to="barcode/")
    barcode_display = models.FileField(null=True, blank=True, upload_to="display/")

    class Meta:
        managed = True
        db_table = 'softmatterdata'


class WebsiteMaterialsdb(models.Model):
    id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', primary_key=True, max_length=200)  # Field name made lowercase.
    materialname = models.CharField(db_column='MaterialName', max_length=100)  # Field name made lowercase.
    researchername = models.ForeignKey(User, models.DO_NOTHING, db_column='ResearcherName_id', blank=True, null=True)  # Field name made lowercase.
    dateacquired = models.DateField(db_column='DateAcquired')  # Field name made lowercase.
    dateupdated = models.DateField(db_column='DateUpdated')  # Field name made lowercase.
    doi = models.TextField(db_column='DOI')  # Field name made lowercase.
    acquisitionmethod = models.CharField(db_column='AcquisitionMethod', max_length=100)  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website_materialsdb'


class WebsiteWebsite(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'website_website'
