# Generated by Django 5.1.2 on 2024-11-10 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_emptymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmptyModel',
        ),
        migrations.CreateModel(
            name='CollectionCombinations',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('collection.collection',),
        ),
    ]
