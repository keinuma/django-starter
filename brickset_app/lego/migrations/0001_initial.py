# Generated by Django 2.0.1 on 2018-03-04 06:02

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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField(verbose_name='セット番号')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('image_url', models.URLField(blank=True, verbose_name='画像URL')),
                ('rating', models.FloatField(default=0.0, verbose_name='レーティング')),
                ('piece_count', models.IntegerField(default=0, verbose_name='ピース数')),
                ('minifig_count', models.IntegerField(default=0, verbose_name='ミニフィグ数')),
                ('us_price', models.FloatField(default=0.0, verbose_name='US価格')),
                ('owner_count', models.IntegerField(default=0, verbose_name='オーナー数')),
                ('want_it_count', models.IntegerField(default=0, verbose_name='欲しい数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('items', models.ManyToManyField(to='lego.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
