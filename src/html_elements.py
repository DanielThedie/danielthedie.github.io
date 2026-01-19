def opt_image(image_url, alt_text="", css_class=""):
    if image_url:
        return f'<img src="{image_url}" alt="{alt_text}" class="{css_class}"/>'
    return ""


def opt_button(url, icon, label, css_class):
    if url:
        return (f'<a href="{url}" class="{css_class}" '
                f'target="_blank" rel="noopener">'
                f'<span class="{icon}" '
                f'style="margin-right:0.4em;"></span>{label}</a>')
    return ""
