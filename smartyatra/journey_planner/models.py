from django.db import models

# Create your models here.

class Nodes(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    geohash = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Edges(models.Model):
    vehicle_name = models.CharField(max_length=100)
    node1 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='outgoing_edges')
    node2 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='incoming_edges')
    weight = models.FloatField()

    def __str__(self):
        return (self.node1.name + ' - ' + self.node2.name)
    


