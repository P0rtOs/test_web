from bs4 import BeautifulSoup

with open('ze_celso_e_internado_apos_incendio_atingir_apartamento_onde_mora.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

for script in soup.find_all('script'):
    script.decompose()

for img in soup.find_all(['img', 'amp-img']):
    img.decompose()

for player in soup.find_all('bs-player'):
    player.decompose()

ad_selectors = [
    '.tag-manager-publicidade-container',
    '[data-block-type="ads"]',
    'glb-ad',
    '.publicidade',
    '.content-ads',
    '.banner',
    '.mc-side-item__container',
    '.mais-lidas',
    '.next-article',
    '.push-web-notification',
    '.tp-threshold',
    '#glb-tp-bottom',
    '#menu-curtain',
    '#menu-container',
    '#menu-content-overlay'
]
for selector in ad_selectors:
    for ad in soup.select(selector):
        ad.decompose()

with open('cleaned_site.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Cleaned HTML saved as 'cleaned_site.html'.")
