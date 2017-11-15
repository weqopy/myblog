from django.db import models
import ast


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class ListField(models.TextField):
    # __metaclass__ = models.Field.f
    description = "Store a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, object):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Article(models.Model):
    labels = ListField()
