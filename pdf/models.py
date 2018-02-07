from django.db import models

# Create your models here.
class Core(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=100)
    core = models.ForeignKey(Core)

    def __str__(self):
        return self.name

class Indicator(models.Model):
    name = models.TextField(verbose_name='Indicator')
    framework = models.ForeignKey(Framework)
    stage = models.ForeignKey(Stage)

    def __str__(self):
        return self.name

    def get_core(self):
        return self.framework.core

    get_core.short_description = 'Core'

class CoreDesc(models.Model):
    descriptor = models.TextField(verbose_name='descriptor')
    stage = models.ForeignKey(Stage)
    core = models.ForeignKey(Core)

    class Meta:
        verbose_name = 'Core Description'
        verbose_name_plural = 'Core Descriptions'

    def __str__(self):
        return self.descriptor

class FrameworkDesc(models.Model):
    descriptor = models.TextField(verbose_name='descriptor')
    stage = models.ForeignKey(Stage)
    framework = models.ForeignKey(Framework)

    def __str__(self):
        return self.descriptor