# Generated by Django 4.0.5 on 2022-06-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/')),
                ('slug', models.SlugField(unique=True)),
                ('preco_marketing', models.FloatField()),
                ('preco_marketing_promocional', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('V', 'Variação'), ('S', 'Simples')], default='V', max_length=1)),
            ],
        ),
    ]
