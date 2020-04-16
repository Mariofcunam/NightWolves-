# Generated by Django 3.0.5 on 2020-04-16 02:42

from django.db import migrations, models
import django.db.models.deletion
import food.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, validators=[food.models.unique_name])),
                ('descripcion', models.CharField(max_length=200, validators=[food.models.unique_name])),
                ('precio', models.CharField(max_length=200, validators=[food.models.unique_name])),
                ('foto', models.ImageField(blank=True, null=True, upload_to=food.models.direccion_imagenes_comida)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoDeCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenComida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.IntegerField()),
                ('alimentos', models.ManyToManyField(related_name='articulos', to='food.Alimento')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Cliente')),
                ('id_repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, validators=[food.models.unique_name])),
                ('alimentos', models.ManyToManyField(related_name='miembros', to='food.Alimento')),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.ManyToManyField(related_name='clasificacion', to='food.Categoria'),
        ),
    ]