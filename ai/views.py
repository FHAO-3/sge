from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from ai import models


class AIListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.AIResult
    template_name = 'list_ai.html'
    permission_required = 'ai.view_ai'
    context_object_name = 'ai'
