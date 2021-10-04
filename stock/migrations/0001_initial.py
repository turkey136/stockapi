# Generated by Django 3.2.7 on 2021-10-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=10)),
                ('name', models.TextField(max_length=100)),
                ('industry', models.TextField(max_length=500)),
                ('url', models.TextField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.market')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.sector')),
            ],
        ),
        migrations.CreateModel(
            name='DailyStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('low', models.FloatField()),
                ('high', models.FloatField()),
                ('amount_of_change', models.FloatField(null=True)),
                ('rsi', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_stocks', to='stock.stock')),
            ],
        ),
    ]
