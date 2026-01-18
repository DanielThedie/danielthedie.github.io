from generators.timeline_generator import TimelineGenerator
from generators.publications_generator import PublicationsGenerator
from generators.software_generator import SoftwareGenerator
from helpers import create_html


class WebsiteGenerator:
    def __init__(self):
        self.base_html = self.get_base_html()

    def get_base_html(self):
        with open("templates/base.html", "r", encoding="utf-8") as f:
            return f.read()

    def generate_index(self):
        tg = TimelineGenerator("content/timeline.yaml")
        timeline_html = tg.generate_timeline_html()
        page_html = self.base_html.replace("<!-- CONTENT -->", timeline_html)
        create_html("docs/index.html", page_html)

    def generate_publications(self):
        pg = PublicationsGenerator("content/publications.yaml")
        html = pg.generate_publications_html()
        page_html = self.base_html.replace("<!-- CONTENT -->", html)
        create_html("docs/publications.html", page_html)

    def generate_software(self):
        sg = SoftwareGenerator("content/software.yaml")
        html = sg.generate_software_html()
        page_html = self.base_html.replace("<!-- CONTENT -->", html)
        create_html("docs/software.html", page_html)

    def build(self):
        self.generate_index()
        self.generate_publications()
        self.generate_software()


if __name__ == "__main__":
    WebsiteGenerator().build()
