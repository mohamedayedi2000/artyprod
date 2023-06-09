# Generated by Django 4.1.7 on 2023-04-30 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0007_alter_categorie_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Cv', models.ImageField(blank=True, upload_to='')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('linkedin_profile', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_registered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('project', models.ManyToManyField(through='magasin.Detail', to='magasin.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.user'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='Personnel',
            field=models.ManyToManyField(to='magasin.personnel'),
        ),
        migrations.AddField(
            model_name='detail',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.project'),
        ),
        migrations.AddField(
            model_name='detail',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.service'),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.personnel')),
            ],
        ),
    ]
