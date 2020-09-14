from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='child')
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.parent:
            url = self.parent.get_url()
        else:
            return '{}/'.format(self.slug)
        return '{}{}/'.format(url, self.slug)

    def get_img(self):
        if self.image:
            return self.image.url
        elif self.parent.image:
            return self.parent.image.url
        else:
            return "http://placehold.it/100x100"


class Good(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='good')
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        url = '{}{}_{}/'.format(self.category.get_url(), self.slug, str(self.id))
        return url

    def get_img(self):
        if self.image:
            return self.image.url
        else:
            return self.category.get_img()
