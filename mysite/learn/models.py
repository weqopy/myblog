# 每次创建模块类之后，需要在'python manage.py shell' 中
# 运行'python manage.py makemigrations'及'python manage.py migrate'
# 以更新数据库

from django.db import models
import ast


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def my_property(self):
        return 'name is ' + self.name

    my_property.short_description = 'name description'

    # list_display = ('name_description', )显示非变量内容
    name_description = property(my_property)


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
    title = models.CharField('标题', max_length=255)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发布时间', auto_now=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
