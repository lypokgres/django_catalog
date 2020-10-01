from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='child')
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if not self.parent:
            return '/{}/'.format(self.slug)
        return '{}{}/'.format(self.parent.get_absolute_url(), self.slug)

    def get_img(self):
        if self.image:
            return self.image.url.split('/')[-1]
        if self.parent.image:
            return self.parent.image.url.split('/')[-1]
        return "net-foto.png"

    def get_indent(self, nesting=0):
        if not self.parent:
            return str(nesting)
        return self.parent.get_indent(nesting + 1)

    def find_parent(self):
        parents = [self]
        if self.parent:
            parent = self.parent
            parents.extend(parent.find_parent())
        return parents

    def clean(self):
        if int(self.get_indent()) > 2:
            raise ValidationError('OMG Слишком много категорий в категориях')


class Good(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='good')
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        url = '{}{}_{}/'.format(self.category.get_absolute_url(), self.slug, str(self.id))
        return url

    def get_img(self):
        if self.image:
            return self.image.url.split('/')[-1]
        else:
            return self.category.get_img()

    def find_parent(self):
        parents = [self]
        if self.category:
            parent = self.category
            parents.extend(parent.find_parent())
        return parents
