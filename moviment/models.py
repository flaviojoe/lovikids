from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from core.models import Desire, Job, Timestamps, AuditModel

class JobExec(Timestamps, AuditModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    desire_id = models.ForeignKey(Desire, on_delete=models.CASCADE)
    name = models.CharField('nome', max_length=150)
    percent_done = models.FloatField('percentual_realizado')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "movimento"
        verbose_name_plural = "movimentos"
