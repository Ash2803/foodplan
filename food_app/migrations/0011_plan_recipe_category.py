# Generated by Django 3.2.16 on 2023-03-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0010_auto_20230317_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='recipe_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plans', to='food_app.recipecategory', verbose_name='Меню'),
        ),
    ]