import requests
from bs4 import BeautifulSoup

from django.core.exceptions import ValidationError
from scraper.models import Post

URL_ELTIEMPO = "https://www.eltiempo.com/mundo"
URL_ELPAIS = "https://elpais.com/tag/c/15148420ba519668342b7a63149cad97"
URL_TWP = "https://www.washingtonpost.com/world/"

WEBSITE_URLS = (URL_ELTIEMPO, URL_ELPAIS, URL_TWP)

class ScraperManager:
    def __init__(self):
        self.requests = list()
        self.errors = list()

    def run_requests(self):
        for url in WEBSITE_URLS:
            request = requests.get(url)
            self.requests.append(request)

        self._parse_manager()
        return self.errors

    def _parse_manager(self):
        for request in self.requests:
            if URL_ELTIEMPO in request.url:
                base_url = "https://www.eltiempo.com/"
                post = Post()
                post_type = "ETP"
                post.post_type = post_type

                errors = self._parse_eltiempo(request, post, base_url)
                if errors and "original_post_url" not in errors.keys():
                    errors["type"] = post_type
                    self.errors.append(errors)

            elif URL_ELPAIS in request.url:
                base_url = "https:"
                post = Post()
                post_type = "EPS"
                post.post_type = post_type

                errors = self._parse_elpais(request, post, base_url)
                if errors and "original_post_url" not in errors.keys():
                    errors["type"] = post_type
                    self.errors.append(errors)

            elif URL_TWP in request.url:
                post = Post()
                post_type = "TWP"
                post.post_type = post_type

                self._parse_twp(request, post, base_url)
                pass

    def _parse_eltiempo(self, request, post, base_url):
        soup = BeautifulSoup(request.text, "html.parser")

        # Cover image
        try:
            cover_url = soup.select_one(
                "figure.foto-seccion-home.image-container"
            ).select_one("img")["data-original"]
        except AttributeError:
            cover_url = soup.select_one(
                "figure.foto-seccion-home-video.image-container"
            ).select_one("img")["data-original"]

        post.cover_img_url = f"{base_url}{cover_url}"

        # Principal post anchor
        principal_anchor = soup.select_one("a.boton.page-link")

        # Build principal post url
        principal_post_url = f'{base_url}{principal_anchor["href"]}'
        post.original_post_url = principal_post_url

        # Redirect to principal post
        principal_post = requests.get(principal_post_url)
        post_soup = BeautifulSoup(principal_post.text, "html.parser")
        # Title
        post_title = post_soup.select_one("h1.titulo").string
        post.title = post_title
        # Subtitle
        post_subtitle = post_soup.select_one("p.info").string
        post.subtitle = post_subtitle
        # Author
        post_author = post_soup.select_one("span.nombre").string
        post.author = post_author
        # Pub Date
        post_pub_date = post_soup.select_one("span.fecha").string.strip()
        post.original_post_date = post_pub_date

        post_body = post_soup.select("p.contenido")
        for content in post_body:
            post.body += content.get_text()

        try:
            post.full_clean()
            post.save()
            return dict()
        except ValidationError as error:
            return dict(error)

    def _parse_elpais(self, request, post, base_url):
        soup = BeautifulSoup(request.text, "html.parser")
        principal_art = soup.select_one(
            "#principal > section > div > div.articulos.articulos_apertura"
        )
        post_anchor = principal_art.select_one("h2.articulo-titulo > a")

        # Build principal post url
        principal_post_url = f"{base_url}{post_anchor['href']}"
        post.original_post_url = principal_post_url
        # Redirect to principal post
        principal_post = requests.get(principal_post_url)
        post_soup = BeautifulSoup(principal_post.text, "html.parser")
        # Title
        post.title = post_soup.select_one("h1.articulo-titulo").string
        # Subtitle
        post.subtitle = post_soup.select_one("h2.articulo-subtitulo").string
        # Cover Img
        post_img = post_soup.select_one("figure.foto > img")[
            "data-src"
        ]
        print(post_img)
        post.cover_img_url = f"{base_url}{post_img}"
        # Author
        post.author = post_soup.select_one("span.autor-nombre > a").string
        # Pub Date
        post_pub_date = post_soup.select_one("div.articulo-datos > time > a").get_text()
        post.original_post_date = post_pub_date.replace("\n", "").replace("\t", "")
        # Body
        post_body = post_soup.select("div.articulo-cuerpo > p")
        for content in post_body:
            post.body += content.get_text()

        try:
            post.full_clean()
            post.save()
            return dict()
        except ValidationError as error:
            return dict(error)


    def _parse_twp(self, request, post, base_url):
        soup = BeautifulSoup(request.text, "html.parser")
        post_anchor = soup.select_one("h1.headline > a")["href"]

        # Original post url
        post.original_post_url = post_anchor
        # Redirect to principal post
        principal_post = requests.get(post_anchor)
        post_soup = BeautifulSoup(principal_post.text, "html.parser")

        # Title
        post.title = post_soup.select_one("h1").string
        # Cover Img
        post.cover_img_url = post_soup.select_one("article > figure > img")["src"]
        # Author
        post.author = " & ".join([author.string for author in post_soup.select("span.author-name")])
        # Pub Date
        post.original_post_date = post_soup.select_one("div.display-date").get_text()
        # Body
        post.body = post_soup.select_one("div.article-body").get_text()

        try:
            post.full_clean()
            post.save()
            return dict()
        except ValidationError as error:
            return dict(error)
