from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import unique_slug_generator


# User = settings.AUTH_USER_MODEL

class Room(models.Model):
    room_name = models.CharField(max_length=120, null=True, blank=True)
    room_cost = models.IntegerField()
    room_description = models.TextField(max_length=300, blank=True, null=True)
    height_field = models.IntegerField(null=True, blank=True)
    width_field = models.IntegerField(null=True, blank=True)
    height_field1 = models.IntegerField(null=True, blank=True)
    width_field1 = models.IntegerField(null=True, blank=True)
    room_thumImg = models.ImageField(null=True, blank=True, width_field="width_field1", height_field="height_field1")
    room_img1 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    room_img2 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    room_img3 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    room_img4 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    room_img5 = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    room_facilities = models.TextField(help_text='seperate each item by comma')
    room_availability = models.IntegerField(null=True, blank=True)
    room_accomadete = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.room_name

    def get_room_facilities(self):
        return self.room_facilities.split(",")

    @property
    def title(self):
        return self.room_name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Room)


class RoomCheck(models.Model):
    room_name = models.CharField(max_length=120, null=True, blank=True)
    room_accomadete = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.room_name
