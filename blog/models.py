import uuid

from django.db import models
from tinymce import models as tinymce_fields

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

    def __str__(self):
        for choice in self.REGION_CHOICES:
            if choice[0] == self.region:
                return choice[1]

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

    def __str__(self):
        for choice in self.CHOICES:
            if choice[0] == self.choice:
                return choice[1]


class Blogpost(models.Model):
    # Fields for the model object
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogposts")
    title = models.CharField(max_length=128)
    briefing = models.CharField(max_length=512)
    content = tinymce_fields.HTMLField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    must_view = models.BooleanField(default=False)
    
    related_posts = models.ManyToManyField('self' , blank=True)

    region = models.ForeignKey(Region, related_name="blogposts", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Type, related_name="blogposts", on_delete=models.SET_NULL, null=True)

    ups = models.IntegerField(verbose_name="claps", default=0)

    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']

    # Functions
    def get_author_photo(self, *args):
        return self.author.photo

    # String represntation in Editor
    def __str__(self):
        name = f"{self.title} by {self.author}"
        return name

    def get_related_post(self):
        title_of_post = f"{self.related_posts.title}"
        return title_of_post

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, null= True, blank = True)
    content = models.TextField(max_length=2048)
    time_created = models.DateTimeField(auto_now_add= True)

    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)