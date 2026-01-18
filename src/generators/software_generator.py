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
            languages = event.get("languages", [])
            software_items_html += fill_html_template(
                "templates/software-item.html",
                title=title,
                languages=languages
            )

        return f'<div class="software">\n{software_items_html}</div>'
