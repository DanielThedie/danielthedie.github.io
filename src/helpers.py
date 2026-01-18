def fill_html_template(template_path, **kwargs):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)


def create_html(file_path, body):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(body)
