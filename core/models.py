# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from middleware.current_user import CurrentUserMiddleware


class Timestamps(models.Model):
	date_created = models.DateTimeField('criado_em', auto_now_add=True)
	date_updated = models.DateTimeField('modificado_em', auto_now=True)

	class Meta:
		abstract = True


class TimestampsNoAutoNow(models.Model):
	date_created = models.DateTimeField('criado_em')
	date_updated = models.DateTimeField('modificado_em')

	class Meta:
		abstract = True


class AuditModel(models.Model):
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_criadopor',
								   on_delete=models.CASCADE, null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_modificadopor',
									   on_delete=models.CASCADE, null=True, blank=True)
	@staticmethod
	def get_current_user():
		return CurrentUserMiddleware.get_current_user()

	def set_user_fields(self, user):
		if user and user.pk:
			if not self.pk:
				self.created_by = user
			self.updated_by = user

	def save(self, *args, **kwargs):
		current_user = self.get_current_user()
		self.set_user_fields(current_user)
		super().save(*args, **kwargs)
        
    # class Meta:
    #     abstract = True


class Desire(models.Model):
    name = models.CharField('nome', max_length=150)
    weight = models.IntegerField('peso')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'desejo'
        verbose_name_plural = 'desejos'

class Job(models.Model):
    name = models.CharField('nome', max_length=150)
    level = models.IntegerField('nível')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'


class Status(models.Model):

    class Tipo(models.IntegerChoices):
        PENDENTE = 1
        CONCLUIDO = 2
        CANCELADO = 3
	
