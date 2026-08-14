import pelican


def adicionar_ultimo_evento(generator):
    eventos = [a for a in generator.articles if a.category == "evento"]
    generator.context["ultimo_evento"] = eventos[0] if eventos else None


pelican.signals.article_generator_finalized.connect(adicionar_ultimo_evento)


AUTHOR = 'Perceu Bertoletti'
SITENAME = 'Grupy São Marcos'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['blog','eventos', 'patrocinadores']

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

C4PAPERS="https://github.com/grupy-sao-marcos/call4papers/issues"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
