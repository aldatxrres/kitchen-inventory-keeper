# Generated by Django 5.0.3 on 2024-04-25 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_description_inventorymodel_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'shopping_list',
            },
        ),
        migrations.CreateModel(
            name='ShoppingListItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('purchased', models.BooleanField()),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.shoppinglistmodel')),
            ],
            options={
                'db_table': 'shopping_list_items',
            },
        ),
        migrations.CreateModel(
            name='UserShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shopping_list_owner', models.BooleanField(default=False)),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.shoppinglistmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_shopping_list',
            },
        ),
        migrations.AddField(
            model_name='shoppinglistmodel',
            name='users',
            field=models.ManyToManyField(through='api.UserShoppingList', to=settings.AUTH_USER_MODEL),
        ),
    ]
