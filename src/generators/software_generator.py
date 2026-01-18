import yaml

from helpers import fill_html_template


class SoftwareGenerator:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            self.data = yaml.safe_load(f)
        self.events = self.data.get("software", [])

    def generate_software_html(self):
        software_items_html = ""
        for event in self.events:
            title = event.get("title", "")
            image = event.get("image", "")
            languages = event.get("languages", [])
            github = event.get("github", "")
            app = event.get("app", "")
            docs = event.get("docs", "")

            image_html = f'<img src="{image}" alt="{title} logo" class="software-image"/>' if image else ""

            software_items_html += fill_html_template(
                "templates/software-item.html",
                title=title,
                image_html=image_html,
                languages=languages,
                github=github,
                app=app,
                docs=docs
            )

        return f'<div class="software">\n{software_items_html}</div>'
