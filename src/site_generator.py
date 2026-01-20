import yaml
from pathlib import Path

from html_elements import format_image, format_buttons


class SiteGenerator:
    def __init__(self, content_folder, templates_folder, docs_folder):
        self.content = Path(content_folder)
        self.templates = Path(templates_folder)
        self.docs = Path(docs_folder)
        self.base = self.templates / "base.html"

    def read_html(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def create_html(self, file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def fill_html_template(self, template_path, **kwargs):
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
        return template.format(**kwargs)

    def read_yaml(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def page_wrapper(self, title, content):
        return (f'<h2>{title.capitalize()}</h2>\n'
                f'<div class="{title}">\n'
                f'{content}</div>')

    def create_content(self, title):
        content = self.read_yaml(self.content / f'{title}.yaml')
        items_html = ""
        for event in content.get(title, []):
            format_image(event, title)
            format_buttons(event)
            items_html += self.fill_html_template(
                self.templates / f'{title}-item.html',
                **event)
        return self.page_wrapper(title, items_html)

    def create_page(self, title, page_title=None):
        page_title = title if page_title is None else page_title
        content = self.create_content(page_title)
        base_html = self.read_html(self.base)
        page_html = base_html.replace("<!-- CONTENT -->", content)
        self.create_html(self.docs / f"{title}.html", page_html)
