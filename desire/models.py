from django.db import models
from core.models import Desire, Timestamps, AuditModel, Status
from django.contrib.auth.models import User

class DesireUser(Timestamps, AuditModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    desire_id = models.ForeignKey(Desire, on_delete=models.CASCADE)
    name = models.CharField('nome', max_length=150)
    status = models.IntegerField(choices=Status.Tipo.choices, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

