from django.db import models
from django.contrib.auth.models import User
from core.models import Desire, Job, Timestamps, AuditModel

class JobExec(Timestamps, AuditModel):
    user_id = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE, null=True, blank=True)
    job_id = models.ForeignKey(Job, related_name='job_name', on_delete=models.CASCADE)
    desire_id = models.ForeignKey(Desire, related_name='desire_name', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField('descrição', max_length=150, null=True, blank=True)
    percent_done = models.FloatField('realizado')

    def __str__(self):
        return self.job_id.name
    
    class Meta:
        verbose_name = "movimento"
        verbose_name_plural = "movimentos"

    @property
    def desire_name(self):
        return self.desire_id.name
    
    @property
    def job_name(self):
        return self.job_id.name

    @property
    def user_name(self):
        return self.user_id.first_name
