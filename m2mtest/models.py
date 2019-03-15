from django.db import models


class Foo(models.Model):
    name = models.CharField(max_length=50)


class Bar(models.Model):
    some_m2m_field = models.ManyToManyField(Foo)
