"""
Views do portfólio.

Usamos Class-Based Views (CBV) — padrão Django para melhor organização.
"""

from django.views.generic import TemplateView
from .models import Skill, Experience, Project


class HomeView(TemplateView):
    """
    Página principal do portfólio.
    TemplateView já cuida do render — só precisamos passar o contexto.
    """
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        # Sempre chame super() para não perder o contexto padrão do Django
        context = super().get_context_data(**kwargs)

        # Agrupa skills por categoria para facilitar a exibição no template
        context["skills_by_category"] = self._get_skills_grouped()

        # Experiências ordenadas pela data (mais recente primeiro)
        context["experiences"] = Experience.objects.all()

        # Projetos em destaque aparecem primeiro
        context["projects"] = Project.objects.all()
        context["featured_projects"] = Project.objects.filter(featured=True)

        return context

    @staticmethod
    def _get_skills_grouped():
        """
        Retorna um dicionário {label_categoria: [skills]}.
        Organiza as skills por categoria para renderizar seções separadas.
        """
        grouped = {}
        for skill in Skill.objects.all():
            label = skill.get_category_display()
            grouped.setdefault(label, []).append(skill)
        return grouped
