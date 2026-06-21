from django.db import models


class AIResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.result
