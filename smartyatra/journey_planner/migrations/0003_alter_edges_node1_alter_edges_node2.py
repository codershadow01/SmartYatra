# Generated by Django 5.0.2 on 2024-02-26 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey_planner', '0002_alter_nodes_geohash_edges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edges',
            name='node1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_edges', to='journey_planner.nodes'),
        ),
        migrations.AlterField(
            model_name='edges',
            name='node2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_edges', to='journey_planner.nodes'),
        ),
    ]
