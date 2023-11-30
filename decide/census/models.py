from django.db import models

#Conflicto rama rq2
class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)
