#!/usr/bin/env python3
"""Generates the Dolan & Co static site.
Shared header, footer and badge live here so every page stays in step."""
import os
import urllib.parse
from html import escape as esc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://zoedolan22.github.io/dolanandco/'
EMAIL = 'zoedolan22@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/zoedolan/'
INSTAGRAM = 'https://www.instagram.com/zo.dolan/'
NAME = 'Zoë Dolan'

# ---------------------------------------------------------------- icons
def svg(path, size=20, extra=''):
    return (f'<svg class="arrow" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{path}</svg>')

ARROW = svg('<path d="M5 12h14M13 6l6 6-6 6"/>')
ARROW_UR = svg('<path d="M7 17L17 7M8 7h9v9"/>', 22)
ARROW_UP = svg('<path d="M12 19V5M6 11l6-6 6 6"/>', 16)
ARROW_LEFT = svg('<path d="M19 12H5M11 6l-6 6 6 6"/>', 16)
ARROW_RIGHT_SM = svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 16)
MOON = svg('<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>', 20, ' class="moon"').replace('class="arrow"', 'class="moon"').replace(' class="moon" class="moon"', ' class="moon"')
SUN = ('<svg class="sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
       'stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')
MOON = ('<svg class="moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>')
MENU = svg('<path d="M4 8h16M4 16h16"/>', 22)
CLOSE = svg('<path d="M6 6l12 12M18 6L6 18"/>', 22)
IN_ICON = svg('<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>', 18)
IG_ICON = svg('<rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><path d="M17.5 6.5h.01"/>', 18)

# ---------------------------------------------------------------- content
CAPS = [
    ('paid-media', 'Paid Media', 'Paid Media Management',
     'Google Ads (Performance Max, Search, YouTube), LinkedIn (ABM, lead gen, sponsored content), and Meta. Precision audience architecture, budget allocation, and hands-on campaign management from brief to reporting.'),
    ('campaign-strategy', 'Campaign Strategy', 'Campaign Architecture & Digital Strategy',
     'Full-funnel strategy grounded in business objectives and audience insight. Channel mix, messaging hierarchy, KPI frameworks, and the structural thinking that makes campaigns actually executable.'),
    ('content-strategy', 'Content Strategy', 'Content Strategy & Calendar Systems',
     'Messaging architecture for multi-segment audiences, content calendar planning, pillar development, and the editorial governance that keeps content output accountable across teams.'),
    ('copywriting', 'Copywriting', 'Copywriting & Brand Voice',
     'Ad copy, landing pages, social copy, email, and brand voice guidelines across B2B and B2C. Writing that converts without hollowing out the brand.'),
    ('analytics', 'Analytics', 'Analytics & Performance Reporting',
     'Campaign synthesis and insight frameworks that drive decisions forward. Not just documenting what happened, but translating performance data into the next strategic move.'),
    ('client-advisory', 'Client Advisory', 'Client Advisory & Account Strategy',
     'Multi-client portfolio management, stakeholder communication, and strategic counsel that earns trust through clarity and follow-through. Systems that serve the client, not just the campaign.'),
]

PROJECTS = {
    'herotel': dict(
        client='Herotel Business', label='Google Ads · Lead Gen · Brand', img='images/herotel-business.jpg',
        alt='Herotel Business campaign creative: Fibre that doesn’t leave you gatvol', href='herotel-business.html',
        title='Campaign architecture and copywriting for an ISP targeting South African SMEs.',
        text='Campaign architecture and copywriting for an ISP targeting South African SMEs. Google Performance Max and YouTube campaigns built around the brand line “With Herotel Business, it just works.” Conversion-led lead generation across regional markets.'),
    'hid': dict(
        client='HID Global', label='LinkedIn · ABM · B2B', img='images/hid-global.jpg',
        alt='HID Global campaign creative: Confidence at every door', href='hid-global.html',
        title='B2B LinkedIn campaign strategy and ad copy for a complex access control product.',
        text='B2B LinkedIn campaign strategy and ad copy for a complex access control product. Multi-tier audience targeting, precision segmentation, and campaign architecture built to navigate the constraints of the platform.'),
    'finbond': dict(
        client='Finbond', label='Financial Services · Strategy · Content', img='images/finbond.jpg',
        alt='Finbond x Cheymaxim pitch deck mockup', href=None,
        title='Multi-product campaign architecture for a financial services brand.',
        text='Multi-product campaign architecture for a financial services brand across diverse product categories. Structured messaging, audience segmentation, and a pitch framework built to work across channels and customer stages.'),
    'global': dict(
        client='Global Accommodation', label='Brand Development · Digital Growth', img='images/global-accommodation.jpg',
        alt='Global Accommodation campaign creative: New Zealand in Two Weeks', href=None,
        title='Brand development for an international accommodation platform.',
        text='A two-year brand development engagement building digital presence, positioning architecture, and sustainable growth systems for an international accommodation platform from the ground up.'),
    'allan': dict(
        client='Allan & Gill Gray Philanthropies', label='Entrepreneurship · Paid Media · Content', img='images/allan-gray-philanthropies.jpg',
        alt='Allan & Gill Gray Philanthropies campaign creative: Application Requirements', href=None,
        title='Integrated digital campaign management for entrepreneurship development initiatives.',
        text='Integrated digital campaign management for entrepreneurship development initiatives, including application drive campaigns and content calendar coordination. Multi-workstream planning and performance reporting across an active ongoing engagement.'),
    'funda': dict(
        client='Funda Wande', label='Education · Impact · Content Strategy', img='images/funda-wande.jpg',
        alt='Funda Wande campaign creative: Maths is not a path, it’s a playground', href=None,
        title='Digital strategy and content for an education impact organisation.',
        text='Digital strategy and content approach for an education impact organisation working at scale in South Africa. Messaging architecture for multiple stakeholder audiences with distinct needs and different proximity to the work.'),
}

CASES = {
    'herotel-business': dict(
        client='Herotel Business', tags='B2B Lead Generation · SME Targeting · Google Ads', flight='March–June 2026',
        sector='Internet service provider', hero='images/herotel-ad-2.jpg', hero_pos='50% 42%',
        hero_alt='Herotel Business campaign creative: Fibre that never misses a sale',
        lead='A structured digital approach to grow an ISP’s SME customer base in a competitive B2B market, built around the brand platform “It Just Works.”',
        approach='Paid and organic social campaigns aligned to clear commercial intent, driving targeted traffic into defined conversion pathways.',
        paras=[
            'Herotel Business needed to reach small and medium enterprises across regional South African markets and convert them into qualified leads. The work spanned campaign architecture, audience segmentation, and copywriting across Google Performance Max, YouTube, LinkedIn, and Meta, with each channel mapped to a distinct stage of commercial intent.',
            'The creative platform leaned into local language and everyday business moments, the shop that can’t miss a sale, the lodge that needs wireless that never checks out, the café tired of failed card machines, pairing recognisable South African humour with a clear product promise and price. The supporting website functioned as the lead-capture hub at the centre of the broader campaign ecosystem.',
        ],
        did=[
            'Campaign architecture across Google Performance Max, YouTube, and Meta',
            'Paid and organic social strategy and management',
            'Audience segmentation by region and commercial intent',
            'Ad copywriting and creative direction',
            'Website lead-capture flow coordination',
            'Performance reporting and analytics across the funnel',
            'Ongoing optimisation based on campaign data',
        ],
        gallery=[
            ('images/herotel-ad-3.jpg', 'Herotel Business campaign creative: Say howzit to better business fibre'),
            ('images/herotel-ad-1.jpg', 'Herotel Business campaign creative: Wireless that never checks out'),
            ('images/herotel-ad-5.jpg', 'Herotel Business campaign creative: More connectivity, less eish'),
            ('images/herotel-ad-4.jpg', 'Herotel Business campaign creative: Business fibre that works now, not now now'),
            ('images/herotel-ad-2.jpg', 'Herotel Business campaign creative: Fibre that never misses a sale'),
            ('images/herotel-business.jpg', 'Herotel Business campaign creative: Fibre that doesn’t leave you gatvol'),
        ],
        results_h='Reach, traffic, and conversion at scale.',
        results_p='Performance across a four-month flight (March–June 2026) in the Herotel region, spanning brand awareness, acquisition, and conversion.',
        stats=[
            ('7.3M+', 'Paid impressions across LinkedIn & Meta', None),
            ('69,904', 'Total website visitors', '131.3%'),
            ('30,243', 'Google Ads clicks', '325.7%'),
            ('1,326', 'Contact form submissions', '605.3%'),
            ('341', 'Coverage checks initiated', '9.6%'),
            ('366', 'New LinkedIn followers', '116.6%'),
        ],
        next='hid-global'),
    'hid-global': dict(
        client='HID Global', tags='LinkedIn · ABM · B2B', flight='July 2025–June 2026',
        sector='Access control technology', hero='images/hid-ad-3.jpg', hero_pos='50% 50%',
        hero_alt='HID Global campaign creative: Turning phones into digital keys for your employees',
        lead='Account-based marketing strategy for a complex access control product, built to speak clearly to multiple stakeholder groups without diluting the core proposition.',
        approach='Precision audience segmentation and a messaging architecture built to speak differently to several stakeholder groups, while staying tightly aligned on a single core proposition.',
        paras=[
            'At HID Global, I led the account-based marketing strategy behind a multi-tier B2B campaign for a complex access control technology product. Working across LinkedIn and Google Ads, I built precision audience segmentation and messaging that spoke differently to several stakeholder groups, from IT decision-makers to facilities and security buyers, while staying tightly aligned on a single core proposition.',
            'A key part of the brief was working within real platform constraints, particularly LinkedIn’s targeting limits for a niche technical audience, which meant ongoing testing and refinement of creative, copy, and audience definitions to keep the campaign efficient without diluting the message.',
        ],
        did=[
            'Account-based marketing strategy across LinkedIn and Google Ads',
            'Audience segmentation across multiple B2B stakeholder groups',
            'Messaging architecture tailored to each buyer type',
            'Creative and copy testing within LinkedIn’s platform constraints',
            'Campaign-level reporting and analytics',
            'Ongoing refinement of targeting and creative based on performance',
        ],
        gallery=[
            ('images/hid-ad-2.jpg', 'HID Global campaign creative: Confidence at every door'),
            ('images/hid-ad-6.jpg', 'HID Global campaign creative: Access control designed for the way your team works'),
            ('images/hid-ad-4.jpg', 'HID Global campaign creative: This is what modern access looks like'),
            ('images/hid-ad-5.jpg', 'HID Global campaign creative: HID Mobile Access is trusted worldwide'),
            ('images/hid-ad-1.jpg', 'HID Global campaign creative: Bring secure access to every entry point'),
            ('images/hid-ad-3.jpg', 'HID Global campaign creative: Turning phones into digital keys for your employees'),
        ],
        results_h='Reach and intent, across a niche audience.',
        results_p='Performance across a 12-month flight (July 2025–June 2026), spanning brand awareness, acquisition, and conversion for a highly specific B2B audience.',
        stats=[
            ('17.1M', 'LinkedIn impressions', None),
            ('3M+', 'Google Ads impressions', None),
            ('19,303', 'Total website visits', '1,530.3%'),
            ('115,703', 'Google Ads clicks', None),
            ('38,278', 'LinkedIn clicks', None),
            ('846', 'Total conversions', None),
        ],
        next='herotel-business'),
}

ABOUT_P1 = ('I started in content marketing and grew into a full-spectrum Digital Strategist role.',
            'Along the way I’ve built campaigns, managed content teams, written the copy, owned the analytics, and reported back on what worked. I’ve developed a clear point of view: good strategy requires real insight into the business problem, a channel mix built around the audience, and the kind of internal rigour that makes execution possible.')
ABOUT_P2 = 'I currently manage a multi-client B2B and B2C portfolio spanning finance, telecoms, NGOs, retail, travel, and luxury consumer brands, including Allan Gray, Finbond, Herotel Business, Funda Wande, HID Global, and Global Accommodation. I own end-to-end digital strategy for each, including content and channel frameworks, campaign planning, paid media across Google Ads (including Performance Max), Meta, and LinkedIn, analytics and reporting, and brand positioning.'
ABOUT_P3 = 'As Head of Strategy, I act as a strategic partner to clients and stakeholders, translating business goals into clear direction for teams and mentoring team members along the way. I’m also AI-fluent, using tools like these to support strategy, content, and reporting workflows. Based in the Western Cape, working with clients across South Africa and internationally.'
TOOLS = ['Google Ads', 'Meta Business Manager', 'LinkedIn Ads', 'Google Analytics', 'Zoho Analytics', 'Search Console', 'WooCommerce', 'Slack', 'Notion']

NAV = [('Capabilities', 'capabilities.html', '6'), ('Work', 'work.html', None), ('About', 'about.html', None),
       ('Blog', 'blog.html', None), ('Contact', 'contact.html', None)]

AI_PROMPT = ('Tell me about Zoë Dolan, a digital marketing strategist in the Western Cape, South Africa, using her website '
             + SITE + ' as the starting point. What does she do, who has she worked with, and what kind of work is she best suited to?')

# ---------------------------------------------------------------- shared pieces
def btn(label, href, kind='joined', accent=False, small=False, extra=''):
    cls = ['btn']
    if kind == 'joined':
        cls.append('btn--joined')
    elif kind == 'quiet':
        cls.append('btn--quiet')
    if accent:
        cls.append('btn--accent')
    if small:
        cls.append('btn--sm')
    c = ' '.join(cls)
    if kind == 'joined':
        return (f'<a class="{c}" href="{href}"{extra}><span class="btn__goo" aria-hidden="true"><span class="btn__pill"></span>'
                f'<span class="btn__orb"></span></span><span>{label}</span><span class="btn__icon" aria-hidden="true">{ARROW}</span></a>')
    return f'<a class="{c}" href="{href}"{extra}>{label}</a>'


def tag(text, cls=''):
    return f'<p class="tag {cls}'.rstrip() + f'">{text}</p>'


def wordmark():
    return '<span class="wordmark display-sm">Dolan <span class="wordmark__co">&amp; Co</span></span>'


def head(title, desc, file, og='images/zoe-hero.jpg', base=None, ld=''):
    url = SITE + ('' if file == 'index.html' else file)
    b = f'<base href="{base}">\n' if base else ''
    return f'''<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{b}<title>{esc(title)}</title>
<meta name="description" content="{esc(desc, quote=True)}">
<meta name="theme-color" content="#faf5ef" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000f08" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dolan &amp; Co">
<meta property="og:title" content="{esc(title, quote=True)}">
<meta property="og:description" content="{esc(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="fonts/BricolageGrotesque-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/Figtree-Variable.woff2" as="font" type="font/woff2" crossorigin>
<script>try{{var t=localStorage.getItem('dolan-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="site.css">
{ld}</head>
'''


GOO = ('<svg class="goo-defs" aria-hidden="true" focusable="false"><defs><filter id="goo" x="-10%" y="-30%" width="120%" height="160%" '
       'color-interpolation-filters="sRGB"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>'
       '<feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -8"/></filter></defs></svg>')


def header(active, skip='#main'):
    links = ''
    for label, href, badge in NAV:
        cur = ' aria-current="page"' if href == active else ''
        b = f'<span class="nav__badge" aria-hidden="true">{badge}</span>' if badge else ''
        links += f'<a class="nav__link" href="{href}"{cur}>{label}{b}</a>'
    mlinks = '<a href="index.html">Home</a>' + ''.join(f'<a href="{h}">{l}</a>' for l, h, _ in NAV)
    return f'''<a class="skip" href="{skip}">Skip to content</a>
{GOO}
<header class="nav" id="top">
<a class="nav__brand" href="index.html" aria-label="Dolan &amp; Co, home">{wordmark()}</a>
<nav class="nav__links" aria-label="Primary">{links}</nav>
<div class="nav__tools">
<button class="icon-btn" type="button" data-theme-toggle aria-label="Switch to dark mode">{MOON}{SUN}</button>
<button class="icon-btn menu-btn" type="button" data-menu-open aria-expanded="false" aria-controls="menu" aria-label="Open menu">{MENU}</button>
{btn('Say hello', 'contact.html', small=True)}
</div>
</header>
<div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Menu" hidden>
<div class="menu__top"><a class="nav__brand" href="index.html" aria-label="Dolan &amp; Co, home">{wordmark()}</a>
<button class="icon-btn" type="button" data-menu-close aria-label="Close menu">{CLOSE}</button></div>
<p class="menu__label label">Have a look around...</p>
<nav class="menu__links" aria-label="Mobile">{mlinks}</nav>
<div class="actions">{btn('Say hello', 'contact.html', accent=True)}</div>
</div>
'''


def footer(top='#top'):
    return f'''<footer class="footer">
<a class="tab tab--tr footer__top" href="{top}">Back to top {ARROW_UP}</a>
<div class="tab tab--tl footer__rail"><a href="{LINKEDIN}" aria-label="LinkedIn">{IN_ICON}</a><a href="{INSTAGRAM}" aria-label="Instagram">{IG_ICON}</a></div>
<div class="footer__grid">
<div class="footer__cta"><p class="footer__cta-t">Like what you see?</p>{btn('Say hello', 'contact.html', accent=True)}</div>
<nav class="footer__col" aria-label="Explore"><p class="footer__h label">Explore</p><ul>
<li><a href="index.html">Home</a></li><li><a href="capabilities.html">Capabilities</a></li><li><a href="work.html">Work</a></li>
<li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></nav>
<div class="footer__col"><p class="footer__h label">Elsewhere</p><ul>
<li><a href="{LINKEDIN}">LinkedIn</a></li><li><a href="{INSTAGRAM}">Instagram</a></li></ul></div>
<div class="footer__col"><p class="footer__h label">Get in touch</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>Western Cape<br>South Africa</p></div>
</div>
<div class="footer__ghostwrap"><p class="footer__ghost" aria-hidden="true">Five years in strategy</p></div>
<div class="footer__bar"><a class="nav__brand" href="index.html" aria-label="Dolan &amp; Co, home">{wordmark().replace('display-sm', 'heading')}</a>
<p>© 2026 Zoë Dolan · Digital Strategist · Western Cape</p>
<p>All work shown is the property of Cheymaxim Brand &amp; Digital.</p></div>
</footer>
<a class="badge" href="contact.html" aria-label="Say hello, get in touch">
<svg class="badge__ring" viewBox="0 0 112 112" aria-hidden="true" focusable="false"><defs><path id="ring" d="M56,56 m-43,0 a43,43 0 1,1 86,0 a43,43 0 1,1 -86,0"/></defs>
<text><textPath href="#ring" textLength="268" lengthAdjust="spacing">Say hello · Say hello · Say hello · </textPath></text></svg>
<span class="eyes" aria-hidden="true"><i><b></b></i><i><b></b></i></span></a>
<script src="site.js" defer></script>
</body>
</html>
'''


def page(file, title, desc, body, active='', og='images/zoe-hero.jpg', base=None, ld='', skip='#main', top='#top'):
    html = head(title, desc, file, og, base, ld) + '<body>\n' + header(active, skip) + f'<main id="main" tabindex="-1">\n{body}\n</main>\n' + footer(top)
    with open(os.path.join(ROOT, file), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', file, len(html))


def loop():
    seq = '<span>Let’s work</span><span class="accent-word">together.</span>' * 2
    return f'''<a class="loop" href="contact.html" aria-label="Let’s work together. Get in touch.">
<div class="loop__row" aria-hidden="true">{seq}</div>
<div class="loop__row loop__row--r" aria-hidden="true">{seq}</div>
</a>'''


def project(p, text=False):
    orb = f'<span class="project__orb" aria-hidden="true">{ARROW_UR}</span>' if p['href'] else ''
    inner = (f'<div class="project__img"><img src="{p["img"]}" alt="{esc(p["alt"], quote=True)}" width="1000" height="1000" loading="lazy">{orb}</div>'
             f'<p class="project__meta"><span>{esc(p["client"])}</span><i aria-hidden="true"></i><span>{esc(p["label"])}</span></p>'
             f'<h3 class="project__title">{esc(p["title"])}</h3>')
    if text:
        body = p["text"]
        if body.startswith(p["title"]):
            body = body[len(p["title"]):].strip()
        if body:
            inner += f'<p class="project__text">{esc(body)}</p>'
    if p['href']:
        return f'<a class="project" href="{p["href"]}">{inner}</a>'
    return f'<article class="project">{inner}</article>'


def ai_links():
    q = urllib.parse.quote(AI_PROMPT)
    items = [('ChatGPT', f'https://chatgpt.com/?q={q}'), ('Claude', f'https://claude.ai/new?q={q}'),
             ('Google', f'https://www.google.com/search?udm=50&q={q}'), ('Grok', f'https://grok.com/?q={q}')]
    return ''.join(f'<a class="btn btn--accent btn--sm" href="{u}">{n}</a>' for n, u in items)


# ---------------------------------------------------------------- pages
def home():
    rows = ''
    for i, (slug, short, full, _) in enumerate(CAPS, 1):
        rows += (f'<li class="row"><a class="row__link" href="capabilities.html#{slug}"><span class="row__n numeral" aria-hidden="true">{i}</span>'
                 f'<span class="row__title display-lg">{short}</span><span class="orb" aria-hidden="true">{ARROW}</span></a></li>')
    brands = ''.join(f'<li>{n}</li>' for n in ['Herotel Business', 'HID Global', 'Finbond', 'Global Accommodation', 'Allan Gray', 'Funda Wande'])
    P = PROJECTS
    ld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Zoë Dolan","jobTitle":"Digital Marketing Strategist","url":"{SITE}","image":"{SITE}images/zoe-hero.jpg","email":"mailto:{EMAIL}","address":{{"@type":"PostalAddress","addressRegion":"Western Cape","addressCountry":"ZA"}},"sameAs":["{LINKEDIN}","{INSTAGRAM}"]}}</script>
'''
    body = f'''<section class="hero" aria-label="Introduction">
<div class="media hero__media">
<div class="tab tab--tl hero__tab">
{tag('Digital Marketing Strategist')}
<h1 class="display-lg hero__title headline">Hi. I am <span class="accent-word">Zoë.</span></h1>
<div class="actions">{btn('View my work', 'work.html')}{btn('My capabilities', 'capabilities.html', kind='quiet')}</div>
</div>
<div class="hero__stage">
<span class="hero__block" aria-hidden="true"></span><span class="hero__dot" aria-hidden="true"></span>
<img class="hero__card" src="images/herotel-ad-3.jpg" alt="" width="1000" height="1000">
<img class="hero__portrait" src="images/zoe-hero.jpg" alt="Portrait of Zoë Dolan" width="800" height="1000" fetchpriority="high">
</div>
<a class="chip" href="about.html"><img src="images/zoe-hero.jpg" alt="" width="48" height="48"><span><span class="chip__t">Hi, I am Zoë</span><span class="chip__s">Digital Strategist, Western Cape</span></span></a>
</div>
</section>

<section class="section" aria-label="Who I am">
<div class="wrap">
<div class="split">
{tag('Who I am', 'split__label')}
<div class="stack stack--l">
<p class="statement indent">I build <span class="accent-word">paid media campaigns</span>, content architecture, and full-funnel strategy for brands that need more than good instincts.</p>
<div class="actions">{btn('About me', 'about.html')}{btn('My capabilities', 'capabilities.html', accent=True)}</div>
</div>
</div>
<ul class="brands" aria-label="Brands I have worked with">{brands}</ul>
</div>
</section>

<section class="section" id="work" aria-labelledby="work-h">
<div class="wrap">
<div class="work">
<div class="work__col">
{project(P['herotel'])}
{project(P['finbond'])}
<div class="cta-left"><p class="cta-center__t">Like what you see?</p>{btn('Say hello', 'contact.html', accent=True)}</div>
</div>
<div class="work__col">
<div class="work__intro stack">
{tag('Selected work')}
<h2 id="work-h" class="display-lg headline">A closer <span class="accent-word">look.</span></h2>
<p class="text">Paid media, content, and full-funnel strategy for brands in finance, telecoms, NGOs, retail, travel, and luxury consumer sectors. A few of them, up close.</p>
{btn('All work', 'work.html')}
</div>
{project(P['hid'])}
{project(P['global'])}
</div>
</div>
</div>
</section>

<section class="band band--onyx" aria-labelledby="cap-h">
<div class="wrap">
<div class="split">
{tag('What I do', 'split__label')}
<div class="stack">
<h2 id="cap-h" class="display-lg headline">Capabilities</h2>
<p class="text">Six disciplines, one point of view: good strategy starts with the business problem, then builds the channel mix around the audience.</p>
{btn('See all capabilities', 'capabilities.html', accent=True)}
</div>
</div>
<ul class="rows">{rows}</ul>
</div>
</section>

<section class="section section--quote" aria-label="My approach">
<div class="wrap">
<div class="media quote">
<figure class="tab tab--tl quote__tab">
{tag('My approach')}
<blockquote class="quote-card__text">Good strategy requires real insight into the business problem.</blockquote>
<figcaption class="person"><img src="images/zoe-hero.jpg" alt="" width="40" height="40"><span><b>Zoë Dolan</b><span>Digital Marketing Strategist</span></span></figcaption>
</figure>
<div class="quote__imgs" aria-hidden="true">
<img src="images/herotel-ad-4.jpg" alt="" width="1000" height="1000" loading="lazy">
<img src="images/hid-ad-3.jpg" alt="" width="1000" height="1000" loading="lazy">
<img src="images/global-accommodation.jpg" alt="" width="1000" height="1000" loading="lazy">
</div>
<div class="tab tab--br quote__tab2">{btn('Read my story', 'about.html', kind='pill', small=True)}{btn('View my work', 'work.html', kind='pill', accent=True, small=True)}</div>
</div>
</div>
</section>

<section class="section" aria-label="Where I work">
<div class="wrap split">
{tag('Where I work', 'split__label')}
<div class="stack stack--l">
<p class="statement indent">Based in the <span class="accent-word">Western Cape</span>, working with clients across South Africa and internationally.</p>
<div class="two where__body">
<p class="text">{ABOUT_P2}</p>
<p class="text">As Head of Strategy, I act as a strategic partner to clients and stakeholders, translating business goals into clear direction for teams and mentoring team members along the way.</p>
</div>
{btn('More about me', 'about.html')}
</div>
</div>
</section>

{loop()}

<section class="section" aria-labelledby="blog-h">
<div class="wrap blog-row">
<div class="blog-row__side">
{tag('From the blog')}
<h2 id="blog-h" class="display-md headline">The latest from the blog</h2>
{btn('View the blog', 'blog.html')}
<div class="arrows" aria-hidden="true"><span class="icon-btn" aria-disabled="true">{svg('<path d="M19 12H5M11 6l-6 6 6 6"/>', 20)}</span><span class="icon-btn" aria-disabled="true">{ARROW}</span></div>
</div>
<div class="empty">
<h3 class="empty__title">The first posts are on the way.</h3>
<p class="empty__text">Nothing published yet. Check back soon.</p>
</div>
</div>
</section>

<section class="ai" aria-labelledby="ai-h">
<img class="ai__img ai__img--1" src="images/finbond.jpg" alt="" width="300" height="300" loading="lazy">
<img class="ai__img ai__img--2" src="images/herotel-ad-5.jpg" alt="" width="300" height="300" loading="lazy">
<img class="ai__img ai__img--3" src="images/hid-ad-1.jpg" alt="" width="300" height="300" loading="lazy">
<img class="ai__img ai__img--4" src="images/allan-gray-philanthropies.jpg" alt="" width="300" height="300" loading="lazy">
<img class="ai__img ai__img--5" src="images/funda-wande.jpg" alt="" width="300" height="300" loading="lazy">
<img class="ai__img ai__img--6" src="images/hid-ad-4.jpg" alt="" width="300" height="300" loading="lazy">
<div class="ai__inner">
{tag('Want a second opinion?')}
<h2 id="ai-h" class="display-lg ai__title headline">See what AI has to say about <span class="accent-word">me</span></h2>
<div class="ai__pills">{ai_links()}</div>
</div>
</section>'''
    page('index.html', 'Zoë Dolan, Digital Marketing Strategist | Dolan & Co',
         'Zoë Dolan is a Digital Marketing Strategist based in the Western Cape, South Africa. Five years building paid media, content, and full-funnel digital strategy for brands across finance, telecoms, NGOs, retail, travel, and luxury consumer sectors.',
         body, ld=ld)


def capabilities():
    secs = ''
    for i, (slug, short, full, desc) in enumerate(CAPS, 1):
        secs += f'''<section class="cap" id="{slug}" aria-labelledby="{slug}-h">
<div><span class="cap__n numeral" aria-hidden="true">{i}</span></div>
<div>
<h2 id="{slug}-h" class="cap__title display-lg headline">{esc(full)}</h2>
<p class="cap__text text">{esc(desc)}</p>
{btn('Start a conversation' + ARROW_RIGHT_SM, 'contact.html', kind='quiet')}
</div>
</section>
'''
    body = f'''<section class="pagehead">
<div class="wrap">
<div class="pagehead__split">{tag('What I do')}<h1 class="display-xl big-title headline">Capabilities</h1></div>
<p class="pagehead__lead">Six disciplines, built around one point of view: good strategy requires real insight into the business problem, a channel mix built around the audience, and the kind of internal rigour that makes execution possible.</p>
</div>
</section>
<div class="section section--tight"><div class="wrap">
{secs}
</div></div>
{loop()}'''
    page('capabilities.html', 'Capabilities | Dolan & Co',
         'Paid media management, campaign architecture, content strategy, copywriting, analytics and client advisory from Zoë Dolan, a Digital Marketing Strategist in the Western Cape, South Africa.',
         body, active='capabilities.html')


def work():
    P = PROJECTS
    body = f'''<section class="pagehead">
<div class="wrap">
<div class="pagehead__split">{tag('Selected projects')}<h1 class="display-xl big-title headline">Work</h1></div>
</div>
</section>
<section class="section section--tight">
<div class="wrap">
<div class="work">
<div class="work__col">
{project(P['herotel'], True)}
{project(P['finbond'], True)}
{project(P['allan'], True)}
</div>
<div class="work__col">
<div class="quote-card work__intro">
<span class="quote-card__mark" aria-hidden="true">“</span>
<p class="quote-card__text">Writing that converts without hollowing out the brand.</p>
{btn('See my capabilities', 'capabilities.html', accent=True)}
</div>
{project(P['hid'], True)}
{project(P['global'], True)}
{project(P['funda'], True)}
</div>
</div>
</div>
</section>
{loop()}'''
    page('work.html', 'Work | Dolan & Co',
         'Selected projects by Zoë Dolan: paid media, content strategy and campaign architecture for Herotel Business, HID Global, Finbond, Global Accommodation, Allan & Gill Gray Philanthropies and Funda Wande.',
         body, active='work.html')


def case(slug):
    c = CASES[slug]
    nxt = CASES[c['next']]
    pills = ''.join(f'<li class="pill">{esc(t.strip())}</li>' for t in c['tags'].split('·'))
    did = ''.join(f'<li><span class="row__n numeral" aria-hidden="true">{i}</span><span>{esc(t)}</span></li>' for i, t in enumerate(c['did'], 1))
    gal = ''.join(f'<li><img src="{src}" alt="{esc(alt, quote=True)}" width="1000" height="1000" loading="lazy"></li>' for src, alt in c['gallery'])
    stats = ''
    for n, lbl, d in c['stats']:
        delta = (f'<span class="stat__d label"><span aria-hidden="true">↑</span><span class="sr">Up </span>{d}</span>' if d else '')
        stats += f'<li class="stat"><span class="stat__n display-md">{n}</span><span class="stat__l">{esc(lbl)}</span>{delta}</li>'
    paras = ''.join(f'<p>{esc(p)}</p>' for p in c['paras'])
    body = f'''<div class="case-top">
<ul class="case-pills" aria-label="Disciplines">{pills}</ul>
<p class="case-meta"><span>{esc(c['flight'])}</span><i aria-hidden="true"></i><span>{esc(c['client'])}</span></p>
</div>
<section class="case-hero" aria-label="{esc(c['client'])}">
<div class="media case-hero__media">
<img src="{c['hero']}" alt="{esc(c['hero_alt'], quote=True)}" width="1000" height="1000" style="object-position:{c['hero_pos']}" fetchpriority="high">
<div class="tab tab--tl case-hero__tab"><h1 class="display-lg headline">{esc(c['client'])}</h1></div>
<a class="chip chip--text" href="work.html">{ARROW_LEFT} All work</a>
</div>
</section>
<section class="case-intro">
<p class="statement">{esc(c['lead'])}</p>
<div>
<div class="case-intro__body">{paras}</div>
<dl class="case-facts"><div><dt class="label">Client</dt><dd>{esc(c['client'])}</dd></div><div><dt class="label">Sector</dt><dd>{esc(c['sector'])}</dd></div><div><dt class="label">Flight</dt><dd>{esc(c['flight'])}</dd></div></dl>
</div>
</section>
<section class="section section--tight" aria-labelledby="did-h">
<div class="wrap split">
{tag('What I did', 'split__label')}
<div class="stack stack--l">
<h2 id="did-h" class="sr">What I did</h2>
<p class="statement">{esc(c['approach'])}</p>
<ol class="olist">{did}</ol>
</div>
</div>
</section>
<section class="section section--tight" aria-labelledby="gal-h">
<div class="wrap stack stack--xl">
{tag('Campaign creative')}
<h2 id="gal-h" class="sr">Campaign creative</h2>
<ul class="gallery">{gal}</ul>
</div>
</section>
<section class="band band--periwinkle" aria-labelledby="res-h">
<div class="wrap">
<div class="split">
{tag('Results', 'split__label')}
<div class="stack">
<h2 id="res-h" class="display-md headline">{esc(c['results_h'])}</h2>
<p class="text">{esc(c['results_p'])}</p>
</div>
</div>
<ul class="stats">{stats}</ul>
</div>
</section>
<section class="section section--tight" aria-label="Next project">
<div class="wrap">
<ul class="rows"><li class="row"><a class="row__link" href="{c['next']}.html"><span class="row__n" aria-hidden="true">{ARROW}</span><span class="row__title display-md">Next: {esc(nxt['client'])}</span><span class="orb" aria-hidden="true">{ARROW}</span></a></li></ul>
</div>
</section>
{loop()}'''
    page(f'{slug}.html', f'{c["client"]} case study | Dolan & Co', c['lead'], body, active='work.html', og=c['hero'])


def about():
    fan = ''.join(f'<img src="images/{n}.jpg" alt="" width="400" height="500" loading="lazy">' for n in
                  ['funda-wande', 'herotel-business', 'zoe-about', 'global-accommodation', 'hid-ad-4'])
    fan = fan.replace('<img src="images/zoe-about.jpg" alt=""', '<img src="images/zoe-about.jpg" alt="Zoë Dolan"')
    tools = ''.join(f'<li class="pill">{t}</li>' for t in TOOLS)
    body = f'''<section class="about-hero">
{tag('About')}
<h1 class="display-xl big-title headline">Five years of building work that <span class="accent-word">holds.</span></h1>
<div class="fan">{fan}</div>
</section>
<section class="section section--tight" aria-label="My story">
<div class="wrap split">
{tag('My story', 'split__label')}
<div class="stack stack--l">
<p class="statement">{ABOUT_P1[0]}</p>
<div>
<p class="text">{ABOUT_P1[1]}</p>
<p class="text">{ABOUT_P2}</p>
<p class="text">{ABOUT_P3}</p>
</div>
<div class="actions">{btn('View my work', 'work.html')}{btn('Say hello', 'contact.html', accent=True)}</div>
</div>
</div>
</section>
<section class="section section--tight" aria-label="In numbers">
<div class="wrap">
<ul class="facts">
<li class="fact"><span class="fact__l label">Years in Strategy</span><span class="fact__n display-lg">5+</span></li>
<li class="fact"><span class="fact__l label">Brands Served</span><span class="fact__n display-lg">20+</span></li>
<li class="fact"><span class="fact__l label">Portfolio clients</span><span class="fact__n display-lg">6</span></li>
<li class="fact"><span class="fact__l label">Paid channels</span><span class="fact__n display-lg">3</span></li>
</ul>
</div>
</section>
<section class="band band--periwinkle" aria-labelledby="tools-h">
<div class="wrap split">
{tag('Tools', 'split__label')}
<div class="stack stack--l">
<h2 id="tools-h" class="display-md headline">What I work in</h2>
<ul class="tags">{tools}</ul>
</div>
</div>
</section>
{loop()}'''
    page('about.html', 'About Zoë Dolan | Dolan & Co',
         'Zoë Dolan started in content marketing and grew into a full-spectrum Digital Strategist and Head of Strategy. Based in the Western Cape, working with clients across South Africa and internationally.',
         body, active='about.html', og='images/zoe-about.jpg')


def blog():
    body = f'''<section class="pagehead">
<div class="wrap">
<div class="pagehead__split">{tag('The Blog')}
<div>
<h1 class="sr">Blog</h1>
<div class="filters" data-filters><button type="button" data-filter="all" aria-pressed="true">explore all<sup>0</sup></button></div>
</div>
</div>
</div>
</section>
<section class="section section--tight" aria-label="Posts">
<div class="wrap">
<div class="posts" data-posts><!--
Add a post by copying this card inside this div. data-category creates a filter automatically.

<a class="post" href="blog/my-first-post.html" data-category="Strategy">
  <div class="post__img"><img src="images/blog/my-first-post.jpg" alt="" width="1200" height="800" loading="lazy"></div>
  <p class="post__meta"><span>Strategy</span><i aria-hidden="true"></i><time datetime="2026-11-01">1 Nov 2026</time></p>
  <h2 class="post__title">Post title</h2>
  <p class="post__excerpt">One or two lines about the post.</p>
</a>
--></div>
<div class="empty" data-empty>
<h2 class="empty__title">Nothing here yet.</h2>
<p class="empty__text">The first posts are on the way. In the meantime, have a look at the work, or say hello.</p>
<div class="actions">{btn('View my work', 'work.html')}{btn('Say hello', 'contact.html', accent=True)}</div>
</div>
</div>
</section>'''
    page('blog.html', 'Blog | Dolan & Co',
         'Writing from Zoë Dolan on digital strategy, paid media and content. The first posts are on the way.',
         body, active='blog.html')


def contact():
    rules = f'''<ul class="rules">
<li><span class="label">Email</span><span class="inline"><a class="email" href="mailto:{EMAIL}">{EMAIL}</a><button class="btn btn--sm" type="button" data-copy-email="{EMAIL}">Copy email</button><span class="sr" role="status" aria-live="polite" data-copy-status></span></span></li>
<li><span class="label">Based</span><span>Western Cape, South Africa</span></li>
<li><span class="label">LinkedIn</span><a class="link" href="{LINKEDIN}">linkedin.com/in/zoedolan</a></li>
<li><span class="label">Instagram</span><a class="link" href="{INSTAGRAM}">instagram.com/zo.dolan</a></li>
</ul>'''
    body = f'''<section class="pagehead">
<div class="wrap">
<div class="pagehead__split">{tag('Let’s work together')}
<div class="stack stack--l">
<h1 class="display-xl big-title headline">Start a <span class="accent-word">conversation</span></h1>
<form class="form" data-contact-form action="https://formsubmit.co/{EMAIL}" method="POST" novalidate>
<input type="hidden" name="_subject" value="New enquiry from the Dolan &amp; Co website">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input class="honey" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="field"><label class="field__label label" for="name">Name</label><input class="field__control" id="name" name="name" type="text" required placeholder="Your name" autocomplete="name"></div>
<div class="field"><label class="field__label label" for="email">Email</label><input class="field__control" id="email" name="_replyto" type="email" required placeholder="your@email.com" autocomplete="email"></div>
<div class="field"><label class="field__label label" for="message">Message</label><textarea class="field__control" id="message" name="message" rows="6" required placeholder="Tell me about your brief..."></textarea></div>
<div class="actions"><button class="btn btn--joined btn--accent" type="submit"><span class="btn__goo" aria-hidden="true"><span class="btn__pill"></span><span class="btn__orb"></span></span><span data-label>Send it</span><span class="btn__icon" aria-hidden="true">{ARROW}</span></button></div>
<p class="form__ok" data-form-ok role="status" tabindex="-1" hidden>Got it. I will read it and answer properly.</p>
<p class="form__fail" data-form-fail role="alert" tabindex="-1" hidden>Check this: that did not send. Email me at {EMAIL} instead.</p>
</form>
</div>
</div>
</div>
</section>
<section class="band band--periwinkle" aria-labelledby="avail-h">
<div class="wrap">
<div class="split">
{tag('Availability', 'split__label')}
<div class="stack stack--l">
<h2 id="avail-h" class="display-md headline">Available for consulting engagements.</h2>
<p class="text">Available for strategic consulting engagements, paid media retainers, and senior in-house roles. Based in the Western Cape, working with clients across South Africa and internationally.</p>
</div>
</div>
<div class="split" style="margin-top:var(--space-8)"><span></span>{rules}</div>
</div>
</section>'''
    page('contact.html', 'Contact | Dolan & Co',
         'Get in touch with Zoë Dolan about strategic consulting engagements, paid media retainers, or senior in-house roles. Based in the Western Cape, South Africa.',
         body, active='contact.html')


def notfound():
    body = f'''<section class="nf section">
<span class="nf__block" aria-hidden="true"></span><span class="nf__dot" aria-hidden="true"></span>
<div class="wrap"><div class="nf__text stack stack--l">
{tag('404')}
<h1 class="display-xl big-title headline">Page <span class="accent-word">missing</span></h1>
<p class="statement">I looked everywhere. This page is not here.</p>
{btn('Back home', 'index.html', accent=True)}
</div></div>
</section>'''
    page('404.html', 'Page not found | Dolan & Co', 'That page is not here. Head back to the Dolan & Co home page.', body,
         base='/dolanandco/', skip='/dolanandco/404.html#main', top='/dolanandco/404.html#top')


# ---------------------------------------------------------------- extras
def extras():
    pages = ['', 'capabilities.html', 'work.html', 'herotel-business.html', 'hid-global.html', 'about.html', 'blog.html', 'contact.html']
    urls = ''.join(f'<url><loc>{SITE}{p}</loc></url>\n' for p in pages)
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w') as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
    with open(os.path.join(ROOT, '.nojekyll'), 'w') as f:
        f.write('')
    with open(os.path.join(ROOT, 'favicon.svg'), 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="20" fill="#17364f"/>'
                '<circle cx="45" cy="19" r="9" fill="#ff70a6"/>'
                '<text x="32" y="48" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="30" fill="#faf5ef">D</text></svg>\n')


if __name__ == '__main__':
    home(); capabilities(); work(); case('herotel-business'); case('hid-global'); about(); blog(); contact(); notfound(); extras()
