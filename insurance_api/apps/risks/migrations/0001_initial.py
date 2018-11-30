# Generated by Django 2.1.3 on 2018-11-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('t', 'text'), ('n', 'number'), ('d', 'date'), ('e', 'enum')], default='t', max_length=100)),
                ('default_value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('risk_name', models.CharField(blank=True, default='', max_length=100)),
                ('risk_type', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='riskfield',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_fields', to='risks.RiskType'),
        ),
    ]
