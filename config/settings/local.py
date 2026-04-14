# Importa tudo de base e sobrescreve apenas o necessário para desenvolvimento local
from .base import *  # noqa

DEBUG = True

# Sem restrição de host em desenvolvimento
ALLOWED_HOSTS = ["*"]
