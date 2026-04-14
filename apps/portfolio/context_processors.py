"""
Context processors são funções que injetam dados em TODOS os templates do projeto.
Útil para informações que aparecem no header, footer, etc.
"""


def portfolio_info(request):
    """Informações pessoais disponíveis em qualquer template."""
    return {
        "owner": {
            "name":     "Henrique Callegari",
            "role":     "Desenvolvedor Python & Apprendiz de TI",
            "location": "Sorocaba – SP",
            "email":    "henriquecallegariprof@gmail.com",
            "phone":    "(11) 98383-7001",
            "github":   "https://github.com/henriquecallegari",   # ajuste se diferente
        }
    }
