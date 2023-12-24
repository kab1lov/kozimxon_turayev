from django.core.validators import URLValidator
from django.db.models import Model, ImageField, CharField, TextField, IntegerField, URLField, ForeignKey, CASCADE
import uuid


def image_filename(instance, filename):
    extension = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return f"images/{unique_filename}"


# Create your models here.

class Header(Model):
    subtitle = CharField(max_length=255)
    title = CharField(max_length=255)
    long_description = CharField(max_length=255)
    short_description = CharField(max_length=255)
    image = ImageField(upload_to=image_filename)

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name_plural = 'headers'


class WhyWe(Model):
    sub_title = CharField(max_length=255)
    title = CharField(max_length=255)
    num_company = IntegerField()
    students = IntegerField()
    experiences = IntegerField()
    link = URLField(validators=(URLValidator,), null=True, blank=True)
    image = ImageField(upload_to=image_filename)
    description = TextField()

    def __str__(self):
        return self.sub_title

    class Meta:
        verbose_name_plural = 'Why We'


class Result(Model):
    ord_number = IntegerField()
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Results'


class ResultChild(Model):
    title = CharField(max_length=255, null=True, blank=True)
    result = ForeignKey(Result, CASCADE, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ResultChildren'


class Feedback(Model):
    author = CharField(max_length=255)
    comment = TextField()
    link = URLField(validators=(URLValidator,), null=True, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = 'Feedbacks'


class Service(Model):
    title = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Services'


class ServiceChild(Model):
    text = CharField(max_length=255)
    service = ForeignKey(Service, CASCADE, related_name='service_children')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Service Children'


class About(Model):
    text = CharField(max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'About'


class Contact(Model):
    phone = CharField(max_length=255)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'contact'
