from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone

class Section(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")


class Post(models.Model):

    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    title = models.CharField(_("Title"), max_length=90)
    slug = models.SlugField(_("Slug"), max_length=90, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        verbose_name=_("Author"),
        on_delete=models.CASCADE
    )

    teaser = models.TextField()
    content = models.TextField()

    created = models.DateTimeField(_("Created"), default=timezone.now, editable=False)  # when first revision was created
    published = models.DateTimeField(_("Published"), null=True, blank=True)  # when last published
    view_count = models.IntegerField(_("View count"), default=0, editable=False)

    def __str__(self):
    	return self.title

    def inc_views(self):
        self.view_count += 1
        self.save()
        self.current().inc_views()