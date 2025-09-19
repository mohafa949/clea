from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField("Nom du produit", max_length=200)
    image = models.ImageField("Photo", upload_to="products/")

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField("Titre", max_length=200)
    image = models.ImageField("Image", upload_to="news/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"


class Partner(models.Model):
    name = models.CharField("Nom du partenaire", max_length=200)
    logo = models.ImageField("Logo", upload_to="partners/")

    def __str__(self):
        return self.name
