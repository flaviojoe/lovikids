from django.db import models
from core.models import Desire, Timestamps, AuditModel, Status
from django.contrib.auth.models import User

class DesireUser(Timestamps, AuditModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    desire_id = models.ForeignKey(Desire, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField('descricao', max_length=150, null=True, blank=True)
    status = models.IntegerField(choices=Status.Tipo.choices, default=1)

    def __str__(self):
        return self.desire_id.name

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
    
    @property
    def user_name(self):
        return self.user_id.first_name
    
    @property
    def desire_name(self):
        return self.desire_id.name

