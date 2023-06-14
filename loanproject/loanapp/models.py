from django.db import models
from django.urls import reverse


class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def get_url(self):
            return reverse('loanapp:area_by_Branch', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Area(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='area', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shopapp:ProdCatdetail', args=[self.Branch.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'area'
        verbose_name_plural = 'areas'


    def __str__(self):
        return '{}'.format(self.name)

