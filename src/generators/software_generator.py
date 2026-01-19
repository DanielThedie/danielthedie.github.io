import yaml

from helpers import fill_html_template
from html_elements import opt_image, opt_button


class SoftwareGenerator:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            self.data = yaml.safe_load(f)
        self.events = self.data.get("software", [])

    def generate_software_html(self):
        page_title = "Software"
        software_items_html = ""
        for event in self.events:
            title = event.get("title", "")
            image = event.get("image", "")
            description = event.get("description", "")
            languages = event.get("languages", [])
            github = event.get("github", "")
            app = event.get("app", "")
            docs = event.get("docs", "")
            doi = event.get("doi", "")

            software_items_html += fill_html_template(
                "templates/software-item.html",
                title=title,
                image=opt_image(image, title, "software-image"),
                description=description,
                languages=languages,
                github=opt_button(github,
                                  'fab fa-github',
                                  'Code',
                                  'button'),
                app=opt_button(app,
                               'fa fa-globe',
                               'App',
                               'button'),
                docs=opt_button(docs,
                                'fa fa-book-open',
                                'Docs',
                                'button'),
                doi=opt_button(doi,
                               'fa fa-link',
                               'DOI',
                               'button')
            )

        return (f'<h2>{page_title}</h2>\n'
                f'<div class="software">\n'
                f'{software_items_html}</div>')
