from django.db import models

from user_auth.models import User

# Create your models here.

# The following are the categories that are able to be given to the blog post
class Region(models.Model):
    HOKKAIDO = "HO"
    TOHOKU = "TO"
    KANTO = "KT"
    CHUBU = "CU"
    KANSAI = "KS"
    CHUGOKU = "CG"
    SHIKOKU = "SK"
    KYUSHU = "KY"
    REGION_CHOICES = [
        (HOKKAIDO, "Hokkaido"),
        (TOHOKU, "Tohoku"),
        (KANTO, "Kanto"),
        (CHUBU, "Chubu"),
        (KANSAI, "Kansai"),
        (CHUGOKU, "Chugoku"),
        (SHIKOKU, "Shiokoku"),
        (KYUSHU, "Kyushu"),
    ]

    region = models.CharField(max_length=2, choices=REGION_CHOICES, default=KANTO, primary_key=True)

class Type(models.Model):
    GENERAL = "GEN"
    ENTERTAINMENT = "ENT"
    FOOD = "FOD"
    SPORTS = "SPT"
    BUSINESS = "BUS"
    LEGAL = "LGL"
    TIPS = "TIP"
    CHOICES = [
        (GENERAL, "General"),
        (ENTERTAINMENT, "Entertainment"),
        (FOOD, "Food"),
        (SPORTS, "Sports"),
        (BUSINESS, "Business"),
        (LEGAL, "Legal"),
        (TIPS, "Tips"),
    ]

    choice = models.CharField(max_length=3, choices=CHOICES, default=GENERAL, primary_key=True)

class Blogpost(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogposts")
    title = models.CharField(max_length=128)
    Markdown = models.FileField(upload_to='blogposts')
    related_posts = models.URLField(max_length=200)

    region = models.ForeignKey(Region, related_name="blogposts", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Type, related_name="blogposts", on_delete=models.SET_NULL, null=True)

    ups = models.IntegerField(verbose_name="claps")