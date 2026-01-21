import yaml
import markdown
import re
from pathlib import Path

from html_elements import format_image, format_buttons
from helpers import format_date


class SiteGenerator:
    def __init__(self,
                 pages_yaml,
                 content_folder,
                 templates_folder,
                 docs_folder):
        self.content = Path(content_folder)
        self.templates = Path(templates_folder)
        self.docs = Path(docs_folder)
        self.base = self.templates / "base.html"
        self.pages = self.read_yaml(pages_yaml)['pages']

    def read_html(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def write_html(self, file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def update_html(self, page, placeholder, new_content):
        page_html = self.read_html(self.docs / f"{page}.html")
        page_html = page_html.replace(placeholder, new_content)
        self.write_html(self.docs / f"{page}.html", page_html)

    def fill_html_template(self, template_path, **kwargs):
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
        return template.format(**kwargs)

    def read_yaml(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def page_wrapper(self, title, content):
        return (f'<h2 class="page-title">{title.capitalize()}</h2>\n'
                f'<div class="{title}">\n'
                f'{content}</div>')

    def add_from_yaml(self, name):
        page = next((p for p in self.pages if p['name'] == name), None)
        title = page.get('title', name)
        content = self.read_yaml(self.content / f'{title}.yaml')
        items_html = ""
        for event in content.get(title, []):
            format_image(event, title)
            format_buttons(event)
            items_html += self.fill_html_template(
                self.templates / f'{title}-item.html',
                **event)
        content_html = self.page_wrapper(title, items_html)
        self.update_html(name, "<!-- CONTENT -->", content_html)

    def add_blog(self, name):
        blog_folder = self.content / name
        blog_posts = sorted(blog_folder.glob("*.md"), reverse=True)
        if not (self.docs / f"{name}.html").exists() or not blog_posts:
            return
        blog_html = ""
        for post in blog_posts:
            with open(post, 'r', encoding='utf-8') as f:
                md_text = f.read()
            html = markdown.markdown(md_text)

            blog_date = format_date(post.stem.split('_')[0])
            metadata_html = (f'\n<div class="metadata">'
                             f'Posted on {blog_date}</div>')
            html = re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1' + metadata_html,
                          html, count=1)
            blog_html += self.fill_html_template(
                self.templates / f'{name}-item.html', content=html
                )
        content_html = self.page_wrapper(name, blog_html)
        self.update_html(name, "<!-- CONTENT -->", content_html)

    def create_pages(self):
        for page in self.pages:
            title = page.get('title', page['name'])
            base_html = self.read_html(self.base)
            self.write_html(self.docs / f"{page['name']}.html", base_html)

            style_html = (f'<link href="styles/{title}.css" '
                          f'rel="stylesheet" />\n')
            self.update_html(page['name'], "<!-- STYLESHEET -->", style_html)
