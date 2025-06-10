from bs4 import BeautifulSoup

html_filename = "ze_celso_e_internado_apos_incendio_atingir_apartamento_onde_mora.html"  # ← заміни на свою назву

with open(html_filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

style_tags = soup.find_all("style")
css_content = "\n\n".join(tag.string for tag in style_tags if tag.string)

with open("styles.css", "w", encoding="utf-8") as css_file:
    css_file.write(css_content)

for tag in style_tags:
    tag.decompose()

head_tag = soup.head
if head_tag:
    link_tag = soup.new_tag("link", rel="stylesheet", href="styles.css")
    head_tag.append(link_tag)

with open("cleaned_with_external_css.html", "w", encoding="utf-8") as output_file:
    output_file.write(str(soup.prettify()))
