# Generated by Django 3.2.7 on 2021-09-06 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoDataset',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('string_id', models.CharField(max_length=150, unique=True)),
                ('db_table', models.CharField(max_length=200)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='geodatasets_uploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=50)),
                ('description', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GeoDatasetColumn',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('dtype', models.CharField(max_length=100)),
                ('geodataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_geodatasets.geodataset')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAdminMetadata',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='admin_geodatasets.project')),
                ('grant_access_users_pk', models.CharField(default='', max_length=300)),
                ('grant_access_users_type', models.CharField(default='', max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
