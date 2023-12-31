from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(
        Tag, related_name="tasks", null=True, blank=True
    )

    def toggle_status(self) -> None:
        self.is_done = not self.is_done
        self.save()

    class Meta:
        ordering = ("is_done", "datetime")
