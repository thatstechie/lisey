# Generated by Django 4.1.1 on 2022-09-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Məzmun'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(verbose_name='Paylaşılma tarixi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=120, verbose_name='Üz qapağı'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Bu post paylaşılsın ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_contest',
            field=models.BooleanField(default=False, verbose_name='Bu müsabiqədir ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_event',
            field=models.BooleanField(default=False, verbose_name='Bu tədbirdir ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Bu xəbərdir ?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Başlığı'),
        ),
    ]