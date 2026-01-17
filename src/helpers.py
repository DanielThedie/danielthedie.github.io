def fill_html_template(template_path, **kwargs):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)
