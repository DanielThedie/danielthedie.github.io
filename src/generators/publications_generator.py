import yaml

from helpers import fill_html_template
from html_elements import opt_button


class PublicationsGenerator:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            self.data = yaml.safe_load(f)
        self.events = self.data.get("publications", [])

    def generate_publications_html(self):
        page_title = "Publications"
        publications_items_html = ""
        for event in self.events:
            title = event.get("title", "")
            first_author = event.get("first_author", "")
            year = event.get("year", "")
            journal = event.get("journal", "")
            doi = event.get("doi", "")
            publications_items_html += fill_html_template(
                "templates/publications-item.html",
                title=title,
                first_author=first_author,
                year=year,
                journal=journal,
                doi=opt_button(doi,
                               'fa fa-link',
                               'DOI',
                               'button')
            )

        return (f'<h2>{page_title}</h2>\n'
                f'<div class="publications">\n'
                f'{publications_items_html}</div>')
