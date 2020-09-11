from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='child')
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_url(self):
        url = []
        if self.parent:
            url += [self.parent.get_url()]
            url += [self.slug]
        else:
            return self.slug
        return '/'.join(url)

    def __str__(self):
        return self.name


class Good(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_url(self):
        url = self.category.get_url() + '/' + str(self.id)
        return url

    def __str__(self):
        return self.name
