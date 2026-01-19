import yaml

from helpers import fill_html_template


class TimelineGenerator:
    def __init__(self, yaml_file):
        with open(yaml_file, 'r', encoding='utf-8') as f:
            self.data = yaml.safe_load(f)
        self.events = self.data.get("timeline", [])

    def generate_timeline_html(self):
        page_title = "About"
        timeline_items_html = ""
        for event in self.events:
            image = event.get("image", "")
            title = event.get("title", "")
            location = event.get("location", "")
            dates = event.get("dates", "")
            text = event.get("text", "")
            timeline_items_html += fill_html_template(
                "templates/timeline-item.html",
                image=image,
                title=title,
                location=location,
                dates=dates,
                text=text)

        return (f'<h2>{page_title}</h2>\n'
                f'<div class="timeline">\n'
                f'{timeline_items_html}</div>')
