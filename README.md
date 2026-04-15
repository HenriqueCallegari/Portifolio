# 🐍 Portfólio — Henrique Callegari

Portfólio pessoal construído com **Django 5.2** seguindo boas práticas de estrutura, separação de responsabilidades e dados gerenciáveis pelo admin.

---

## 📁 Estrutura do projeto

```
portfolio_henrique/
│
├── manage.py                        # Ponto de entrada CLI do Django
├── requirements.txt
├── .env.example                     # Copie para .env e configure
│
├── config/                          # Configurações do projeto
│   ├── settings/
│   │   ├── base.py                  # Configs compartilhadas
│   │   └── local.py                 # Configs de desenvolvimento
│   ├── urls.py                      # URLs raiz
│   └── wsgi.py
│
└── apps/
    └── portfolio/                   # App principal
        ├── models.py                # Skill, Experience, Project
        ├── views.py                 # HomeView (Class-Based View)
        ├── urls.py
        ├── admin.py                 # Painel /admin/
        ├── apps.py
        ├── context_processors.py    # Dados globais (nome, email...)
        ├── fixtures/
        │   └── initial_data.json    # Dados iniciais prontos
        ├── templates/portfolio/
        │   ├── base.html            # Nav + Footer
        │   └── home.html            # Página principal
        └── static/portfolio/
            ├── css/main.css
            └── js/main.js
```

---

## 🚀 Como rodar

### 1. Clone e crie o ambiente virtual

```bash
git clone <seu-repo>
cd portfolio_henrique

python -m venv .venv
source .venv/bin/activate        # Linux/Mac
# .venv\Scripts\activate         # Windows
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

```bash
cp .env.example .env
# Edite .env e troque o SECRET_KEY por uma chave aleatória
```

Gere uma chave segura com:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Crie o banco e carregue os dados iniciais

```bash
python manage.py migrate
python manage.py loaddata apps/portfolio/fixtures/initial_data.json
```

### 5. Crie um superuser para acessar o admin

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor

```bash
python manage.py runserver
```

Acesse:
- **Portfólio:** http://localhost:8000
- **Admin:**     http://localhost:8000/admin

---

## ✏️ Personalizando o conteúdo

Todo o conteúdo (projetos, skills, experiências) é gerenciado pelo **Django Admin** em `/admin/`.  
Para alterar nome, e-mail e localização, edite `apps/portfolio/context_processors.py`.

---

## 🧩 Conceitos Django utilizados

| Conceito | Onde |
|---|---|
| Models + ORM | `models.py` — Skill, Experience, Project |
| Class-Based Views | `views.py` — HomeView |
| URL namespacing | `urls.py` — `app_name = "portfolio"` |
| Template inheritance | `base.html` → `home.html` |
| Context processors | `context_processors.py` — dados globais |
| Django Admin | `admin.py` — CRUD pelo painel |
| Fixtures | `initial_data.json` — dados de seed |
| Static files | `static/portfolio/css` e `js` |
| python-decouple | `.env` — segredos fora do código |
| whitenoise | Serve estáticos sem configurar nginx |
