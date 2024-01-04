from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from app.models import (
    About,
    Contact,
    Feedback,
    Header,
    Result,
    ResultChild,
    Service,
    ServiceChild,
    WhyWe,
)


@admin.register(Header)
class HeaderAdmin(ModelAdmin):
    list_display = ("id", "sub_title", "title", "image")
    list_display_links = ("id", "title")


@admin.register(WhyWe)
class WhyWeAdmin(ModelAdmin):
    list_display = ("id", "sub_title", "title")
    list_display_links = ("id", "title")


class ResultChildrenAdmin(StackedInline):
    model = ResultChild


@admin.register(Result)
class ResultAdmin(ModelAdmin):
    list_display = ("id", "ord_number", "title")
    list_display_links = ("id", "title")
    inlines = (ResultChildrenAdmin,)


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        "id",
        "author",
    )
    list_display_links = ("id", "author")


class ServiceChildrenAdmin(StackedInline):
    model = ServiceChild


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("id", "title", "price")
    list_display_links = ("id", "title")
    inlines = (ServiceChildrenAdmin,)


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = (
        "id",
        "text",
    )
    list_display_links = ("id", "text")


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = (
        "id",
        "phone",
    )
    list_display_links = ("id", "phone")
