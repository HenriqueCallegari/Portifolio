"""
Models do portfólio.

Cada classe vira uma tabela no banco de dados.
O Django ORM cuida de toda a SQL por baixo dos panos.
"""

from django.db import models


class Skill(models.Model):
    """Uma habilidade técnica ou ferramenta."""

    class Category(models.TextChoices):
        LINGUAGEM   = "linguagem",   "Linguagem"
        FRAMEWORK   = "framework",   "Framework / Biblioteca"
        BANCO       = "banco",       "Banco de Dados"
        INFRA       = "infra",       "Infraestrutura"
        FERRAMENTA  = "ferramenta",  "Ferramenta"
        IA          = "ia",          "IA / LLM"
        IDIOMA      = "idioma"       "Idioma"   

    name      = models.CharField("Nome", max_length=80)
    category  = models.CharField("Categoria", max_length=20, choices=Category.choices)
    # Nível de 1 a 5 — exibido como barras/estrelas no front
    level     = models.PositiveSmallIntegerField("Nível (1–5)", default=3)
    icon      = models.CharField("Ícone (emoji ou classe CSS)", max_length=30, blank=True)
    order     = models.PositiveSmallIntegerField("Ordem de exibição", default=0)

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
        ordering = ["category", "order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    @property
    def level_range(self):
        """Retorna range(level) para iterar no template e desenhar estrelas."""
        return range(self.level)

    @property
    def empty_level_range(self):
        return range(5 - self.level)


class Experience(models.Model):
    """Experiência profissional ou acadêmica."""

    class ExperienceType(models.TextChoices):
        TRABALHO   = "trabalho",  "Trabalho"
        EDUCACAO   = "educacao",  "Educação"

    company     = models.CharField("Empresa / Instituição", max_length=120)
    role        = models.CharField("Cargo / Curso", max_length=120)
    exp_type    = models.CharField("Tipo", max_length=10, choices=ExperienceType.choices, default=ExperienceType.TRABALHO)
    start_date  = models.DateField("Início")
    end_date    = models.DateField("Término", null=True, blank=True)  # null = atual
    description = models.TextField("Descrição")
    is_current  = models.BooleanField("Emprego/curso atual?", default=False)
    order       = models.PositiveSmallIntegerField("Ordem", default=0)

    class Meta:
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
        ordering = ["-is_current", "-start_date"]

    def __str__(self):
        return f"{self.role} @ {self.company}"

    @property
    def period(self):
        """Exibe '11/2025 – Atualmente' ou '02/2025 – 10/2025'."""
        start = self.start_date.strftime("%m/%Y")
        end = "Atualmente" if self.is_current else self.end_date.strftime("%m/%Y")
        return f"{start} – {end}"


class Project(models.Model):
    """Um projeto do portfólio."""

    class Status(models.TextChoices):
        CONCLUIDO  = "concluido",   "Concluído"
        EM_ANDAMENTO = "andamento", "Em andamento"
        ACADEMICO  = "academico",   "Acadêmico"

    title       = models.CharField("Título", max_length=120)
    slug        = models.SlugField("Slug (URL)", unique=True)
    description = models.TextField("Descrição curta")
    details     = models.TextField("Detalhes completos", blank=True)
    status      = models.CharField("Status", max_length=15, choices=Status.choices, default=Status.CONCLUIDO)
    # Tags de tecnologias usadas (texto livre separado por vírgula)
    tech_stack  = models.CharField("Stack (separado por vírgula)", max_length=255, blank=True)
    github_url  = models.URLField("Link GitHub", blank=True)
    demo_url    = models.URLField("Link Demo", blank=True)
    order       = models.PositiveSmallIntegerField("Ordem", default=0)
    featured    = models.BooleanField("Destaque?", default=False)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["order", "-featured"]

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        """Retorna a stack como lista para iterar no template."""
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]
