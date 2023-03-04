# Generated by Django 4.1.6 on 2023-03-04 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название пункта')),
                ('parent', models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.item', verbose_name='Лежит в')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
