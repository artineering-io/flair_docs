"""Convert the Jekyll/just-the-docs Maya docs (C:/DEV/flair-docs/flair) into Starlight pages.

Re-runnable: it replaces src/content/docs/maya, src/partials/maya and the copied media. Run with python 3.
"""
import os
import posixpath
import re
import shutil
import sys

OLD = 'C:/DEV/flair-docs'
NEW = 'C:/DEV/flair_docs'
OUT = f'{NEW}/src/content/docs/maya'
PARTIALS = f'{NEW}/src/partials/maya'
DISCORD = 'https://discord.gg/6FJZCscQUM'

media_refs = set()
effect_variants = set()

# Effect includes that exist in both hosts: include name -> (title, /effects/ page, anchor).
SHARED_EFFECTS = {
    'ao': ('Ambient Occlusion', 'ambient-occlusion', None),
    'atmosphere': ('Atmospheric Effects', 'atmosphere', None),
    'bleeding': ('Bleeding', 'bleeding', None),
    'edge-darkening': ('Edge Darkening', 'edge-darkening', None),
    'lines': ('Lines', 'lines', None),
    'advanced-line-controls': ('Advanced Line Controls', 'lines', 'advanced-controls'),
    'sketch-lines': ('Rough Lines', 'sketch-lines', None),
    'pigment': ('Pigment', 'pigment', None),
}
# Maya content of each shared /effects/ page: page -> includes (watercolor is the reference style).
EFFECT_PAGES = {
    'ambient-occlusion': ['ao'],
    'atmosphere': ['atmosphere'],
    'bleeding': ['bleeding'],
    'edge-darkening': ['edge-darkening-watercolor'],
    'lines': ['lines', 'advanced-line-controls'],
    'sketch-lines': ['sketch-lines'],
    'pigment': ['pigment-watercolor'],
}
# Maya pages of tools that exist in both hosts: old path -> /tools/ page.
TOOL_PAGES = {
    'art-direction/noisefx': 'noisefx',
    'styles/presets': 'style-presets',
}
report = []


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read().replace('\r\n', '\n')


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def split_frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n?', text, re.S)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'(\w+):\s*(.*)', line)
        if kv:
            data[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return data, text[m.end():]


def youtube(attrs):
    url = re.search(r'url="([^"]*)"', attrs)
    cap = re.search(r'caption="([^"]*)"', attrs)
    url = url.group(1) if url else ''
    cap = cap.group(1) if cap else ''
    title = cap or 'Video'
    out = f'<figure class="video-embed">\n<iframe src="{url}" title="{title}" allowfullscreen loading="lazy"></iframe>\n'
    if cap:
        out += f'<figcaption>{cap}</figcaption>\n'
    return out + '</figure>'


def faq_section(name):
    """Old FAQ include: 'Question' line followed by a <div markdown="1"> answer."""
    body = read(f'{OLD}/_includes/faq/{name}')
    out = []
    pattern = re.compile(r'^([^\n<][^\n]*)\n<div markdown="1">\n(.*?)\n</div>\s*$', re.S | re.M)
    pos = 0
    # Answers can hold nested <div>s, so match each question to its closing </div> by depth.
    lines = body.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if i + 1 < len(lines) and lines[i + 1].strip() == '<div markdown="1">' and line.strip():
            question = line.strip()
            depth, j, answer = 1, i + 2, []
            while j < len(lines):
                l = lines[j]
                depth += len(re.findall(r'<div\b', l)) - len(re.findall(r'</div>', l))
                if depth == 0:
                    break
                answer.append(l)
                j += 1
            out.append(f'<details>\n<summary>{question}</summary>\n\n' + '\n'.join(answer).strip() + '\n\n</details>\n')
            i = j + 1
        elif line.strip():
            # One entry in faq/activation.md has its answer as a plain paragraph instead of a <div>.
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            answer = lines[j].strip() if j < len(lines) else ''
            if answer and lines[j + 1:j + 2] != ['<div markdown="1">']:
                out.append(f'<details>\n<summary>{line.strip()}</summary>\n\n{answer}\n\n</details>\n')
                i = j + 1
            else:
                report.append(f'faq/{name}: stray line kept: {line.strip()[:60]}')
                out.append(line)
                i += 1
        else:
            i += 1
    return '\n'.join(out)


def wrap_callouts(text):
    """`{: .info}` after a block styles that block; turn it into a Starlight aside."""
    lines = text.split('\n')
    out = []
    for line in lines:
        m = re.match(r'^\s*\{:\s*\.?\s*(info|warning|notice--warning)\s*\}\s*$', line)
        if not m:
            out.append(line)
            continue
        kind = 'note' if m.group(1) == 'info' else 'caution'
        block = []
        while out and out[-1].strip():
            block.insert(0, out.pop())
        if not block:
            report.append('callout with no preceding block')
            continue
        out.extend([f':::{kind}', *block, ':::'])
    return '\n'.join(out)


def absolute_links(body, base):
    """Relative links resolved against the page's old URL, for content that moves to another page."""

    def fix(m):
        url = m.group(2)
        if re.match(r'(/|#|[a-z]+:)', url):
            return m.group(0)
        path, _, frag = url.partition('#')
        resolved = posixpath.normpath(posixpath.join(base, path)) + '/'
        for old, new in TOOL_PAGES.items():
            resolved = resolved.replace(f'/maya/{old}/', f'/tools/{new}/')
        return m.group(1) + resolved + (f'#{frag}' if frag else '') + m.group(3)

    return re.sub(r'(\]\(|href=")([^)"\s]+)(\)|")', fix, body)


def slugify(heading):
    """Heading anchor id, as Starlight's slugger makes it."""
    text = re.sub(r'<[^>]+>|`', '', heading).strip().lower()
    text = re.sub(r'[^\w\- ]', '', text)
    return text.replace(' ', '-')


def heading_slugs(text):
    return {slugify(h) for h in re.findall(r'^#{1,6} (.+)$', text, re.M)}


def retarget_anchors():
    """Point anchor links at the page that now holds the heading.

    Shared effects and tools moved off the Maya style pages, so links like
    /maya/styles/library/lines/#line-width now belong on /effects/lines/.
    """
    pages = {}  # page URL -> heading slugs, including the partials it imports
    files = {}  # page URL -> files whose content renders on that page
    docs = f'{NEW}/src/content/docs'
    for root, _, names in os.walk(docs):
        for name in names:
            path = os.path.join(root, name).replace('\\', '/')
            rel = path[len(docs) + 1:].rsplit('.', 1)[0]
            url = '/' + (rel[:-len('index')] if rel.endswith('index') else rel + '/')
            text = read(path)
            sources = [path]
            for imp in re.findall(r"from '([^']+\.md)'", text):
                sources.append(os.path.normpath(os.path.join(os.path.dirname(path), imp)).replace('\\', '/'))
            pages[url] = set().union(*(heading_slugs(read(s)) for s in sources))
            files[url] = sources

    def owner(slug, prefer):
        for url in prefer:
            if slug in pages.get(url, ()):
                return url
        hits = [u for u, slugs in pages.items() if slug in slugs]
        return hits[0] if len(hits) == 1 else None

    effect_urls = [f'/effects/{p}/' for p in EFFECT_PAGES]
    for url, sources in files.items():
        for path in sources:
            if not path.startswith((OUT, PARTIALS)):
                continue
            text = read(path)

            def fix(m):
                target, slug = m.group(1) or url, m.group(2)
                if slug in pages.get(target, ()):
                    return m.group(0)
                new = owner(slug, effect_urls)
                if not new:
                    report.append(f'{url}: anchor #{slug} has no page')
                    return m.group(0)
                return f'({new}#{slug})' if new != url else f'(#{slug})'

            new_text = re.sub(r'\((/(?:maya|effects|tools)/[\w/-]*)?#([\w-]+)\)', fix, text)
            if new_text != text:
                write(path, new_text)


def before_after(m):
    """Old jQuery twentytwenty sliders become .before-after blocks, driven by public/scripts/before-after.js.

    The labels come from the old pages' init scripts, which keyed them by id or class.
    """
    tag = m.group(0)
    if 'flair-comparison' in tag:
        return '<div class="before-after" data-hover>'
    if 'comparison-1-0-3' in tag:
        labels = ('Flair 1.0.2', 'Flair 1.0.3')
    elif 'comparison-1-1-3' in tag:
        labels = ('Flair 1.1.2', 'Flair 1.1.3')
    else:
        labels = ('Before', 'After')
    return f'<div class="before-after" data-before="{labels[0]}" data-after="{labels[1]}">'


TAG_LINE = re.compile(r'^[ \t]+(</?(figure|img|video|source|figcaption|div|iframe|details|summary|span|p|a|br|table|tr|td|th|ul|li)\b)')
LIST_ITEM = re.compile(r'^\s*([-*+]|\d+\.)\s')


def dedent_html(body):
    """Indented HTML lines become code blocks in CommonMark (kramdown tolerated them).

    Lines that continue a list item keep their indentation, since un-indenting would end the list.
    Fenced code is left alone.
    """
    out, in_fence, in_list = [], False, False
    for line in body.split('\n'):
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
        if in_fence:
            out.append(line)
            continue
        if LIST_ITEM.match(line):
            in_list = True
        elif line.strip() and not line[0].isspace():
            in_list = False
        if TAG_LINE.match(line) and not in_list:
            line = line.lstrip()
        out.append(line)
    return '\n'.join(out)


def convert_body(body, rel, effect_imports):
    # Old page heading (Starlight renders the title) and its no_toc marker.
    body = re.sub(r'\A\s*#\s+[^\n]*\n(\{:\s*\.no_toc\s*\}\n)?', '', body)
    # Table-of-contents blocks.
    body = re.sub(r'<details[^>]*>\s*<summary>\s*Table of contents\s*</summary>.*?</details>\n?', '', body, flags=re.S)
    body = re.sub(r'^\s*\{:\s*\.no_toc\s*\}\s*\n', '', body, flags=re.M)

    body = body.replace('{{site.discord-invite}}', DISCORD).replace('{{ site.discord-invite }}', DISCORD)
    # Page-level styles/scripts only drove the jQuery before/after slider; comments aren't valid MDX.
    body = re.sub(r'<style>.*?</style>\n?', '', body, flags=re.S)
    body = re.sub(r'<script\b.*?</script>\n?', '', body, flags=re.S)
    body = re.sub(r'<link\b[^>]*twentytwenty[^>]*>\n?', '', body)
    body = re.sub(r'[ \t]*<!--.*?-->[ \t]*\n?', '', body, flags=re.S)
    body = body.replace('https://docs.artineering.io/media/', '/media/')
    body = re.sub(r'<div\b[^>]*class="twentytwenty-container[^"]*"[^>]*>', before_after, body)
    # The hero comparison's inline width only served the jQuery plugin.
    body = re.sub(r'(<img [^>]*?)\s*style="width: 100vw"', r'\1', body)

    body = re.sub(r'\{%-?\s*include\s+responsive-embed\s+(.*?)-?%\}', lambda m: youtube(m.group(1)), body)
    body = re.sub(r'\{%-?\s*include\s+faq/section\.html\s+file="([^"]+)"[^%]*%\}', lambda m: faq_section(m.group(1)), body)
    body = re.sub(r'\{%-?\s*include\s+faq/_(header|footer)\.html\s*-?%\}\n?', '', body)
    body = re.sub(r'\{%-?\s*include\s+api/([\w-]+\.md)\s*-?%\}', lambda m: read(f'{OLD}/_includes/api/{m.group(1)}'), body)

    def effect(m):
        name = m.group(1)
        if name in SHARED_EFFECTS:
            # Effects found in both Flair for Maya and Flair for Unreal Engine live on shared
            # /effects/ pages, so style pages link there instead of repeating them.
            title, slug, anchor = SHARED_EFFECTS[name]
            target = f'/effects/{slug}/' + (f'#{anchor}' if anchor else '')
            return f'### {title}\n\nSee [{title}]({target}) for its attributes.'
        style = re.search(r'style="([^"]+)"', m.group(2) or '')
        if style and 'include.style' in read(f'{OLD}/_includes/effects/{name}.md'):
            name = f'{name}-{style.group(1)}'
            effect_variants.add(name)
        component = 'Effect' + ''.join(p.capitalize() for p in name.split('-'))
        effect_imports[component] = name
        return f'<{component} />'

    body = re.sub(r'\{%-?\s*include\s+/?effects/([\w-]+)\.md([^%]*?)-?%\}', effect, body)
    # Rouge highlight blocks.
    body = re.sub(r'\{%\s*highlight\s+(\w+)\s*%\}', r'```\1', body)
    body = re.sub(r'\{%\s*endhighlight\s*%\}', '```', body)
    # [Art-directable](#...){: .btn .btn-label} pill links.
    body = re.sub(r'^\[([^\]]+)\]\(([^)]+)\)\n\{:\s*\.btn \.btn-label\s*\}', r'<a class="pill-link" href="\2">\1</a>', body, flags=re.M)
    # Block IDs nobody links to.
    body = re.sub(r'^\{:\s*#[\w-]+\s*\}\s*\n', '', body, flags=re.M)
    # A callout marker before its block (instead of after) styles the following block.
    body = re.sub(r'\n\n(\{:\s*\.?\s*(?:info|warning)\s*\})\n((?:[^\n]+\n)+)', r'\n\n\2\1\n', body)

    # "Flair 1.2" + {: .label .label-green} marks a feature as new in that version.
    body = re.sub(r'^(Flair [\d.]+)\n\{:\s*\.label[^}]*\}\s*$', r'<span class="new-label">New in \1</span>', body, flags=re.M)
    # Link buttons: [text](url){: .aio-btn .d-block}
    body = re.sub(r'(\[[^\]]+\]\([^)]+\))\n?\{:[^}]*aio-btn[^}]*\}', r'\1', body)

    body = wrap_callouts(body)
    body = re.sub(r'^\s*\{:\s*\.text-delta\s*\}\s*\n', '', body, flags=re.M)

    # Kramdown's markdown="1" switch; CommonMark parses Markdown inside HTML blocks when blank lines separate it.
    body = re.sub(r'\s+markdown="(1|block|span)"', '', body)
    body = re.sub(r'^([ \t]*<(div|details)[^>]*>)[ \t]*$', r'\1\n', body, flags=re.M)
    body = re.sub(r'^([ \t]*</(div|details)>)[ \t]*$', r'\n\1', body, flags=re.M)
    body = dedent_html(body)

    # Void tags closed, so the same HTML also works in MDX pages.
    body = re.sub(r'<(img|source|br|hr|col|input)\b([^>]*?)\s*/?>', r'<\1\2 />', body)

    # Old docs lived under /flair/, Maya pages now live under /maya/.
    body = re.sub(r'(\]\(|href=")/flair/', r'\1/maya/', body)
    body = re.sub(r'(\]\(|href=")/flair(\)|")', r'\1/maya/\2', body)
    # Anchors that were already broken on the old site, where the target page is clear.
    body = body.replace('/maya/setup/#for-all-users', '/maya/setup/installation/#for-all-users')
    body = body.replace('/maya/setup/#re-activation', '/maya/setup/activation/')
    # Tools found in both hosts moved to the shared /tools/ section.
    for old, new in TOOL_PAGES.items():
        body = re.sub(rf'/maya/{old}(/|(?=[)#"]))', f'/tools/{new}/', body)

    for ref in re.findall(r'/media/[^\s)"\'<>]+', body):
        media_refs.add(ref)

    leftovers = sorted(set(re.findall(r'\{:[^}]*\}|\{%.*?%\}|\{\{.*?\}\}', body)))
    for lo in leftovers:
        report.append(f'{rel}: leftover {lo[:60]}')
    return re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'


def yaml_str(value):
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def convert_page(src, dst_rel, is_group_index):
    data, body = split_frontmatter(read(src))
    effect_imports = {}
    body = convert_body(body, dst_rel, effect_imports)
    title = data.get('title', 'Flair for Maya')
    sidebar = []
    # Pages that open with a hero image put their full title in a level-one heading below it
    # ("Watercolor shader style"). Starlight renders the title itself, so that heading becomes the
    # title and the old short title stays as the sidebar label. API module headings are left alone.
    h1 = re.search(r'^# (?!<kbd>)(.+)\n', body, re.M)
    if h1 and not re.search(r'^#{2,} ', body[:h1.start()], re.M):
        body = (body[:h1.start()] + body[h1.end():]).strip() + '\n'
        if h1.group(1).strip() != title:
            sidebar.append(f'  label: {yaml_str(title)}')
            title = h1.group(1).strip()
    fm = ['---', f'title: {yaml_str(title)}']
    if data.get('description'):
        fm.append(f'description: {yaml_str(data["description"])}')
    if is_group_index:
        sidebar = ['  label: Overview', '  order: 0']
    elif data.get('nav_order'):
        sidebar.append(f'  order: {data["nav_order"]}')
    if sidebar:
        fm += ['sidebar:', *sidebar]
    fm.append('---')
    ext = '.md'
    head = ''
    if effect_imports:
        ext = '.mdx'
        depth = dst_rel.count('/') + 3  # src/content/docs/maya/<rel> -> src
        up = '../' * depth
        head = '\n'.join(f"import {{ Content as {c} }} from '{up}partials/maya/effects/{n}.md';" for c, n in sorted(effect_imports.items())) + '\n\n'
    write(f'{OUT}/{dst_rel}{ext}', '\n'.join(fm) + '\n' + head + body)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    if os.path.exists(PARTIALS):
        shutil.rmtree(PARTIALS)
    for root, _, files in os.walk(f'{OLD}/flair'):
        for name in files:
            if not name.endswith('.md'):
                continue
            src = os.path.join(root, name).replace('\\', '/')
            rel = src[len(f'{OLD}/flair/'):-3]
            if rel in TOOL_PAGES:
                # The Maya half of a shared /tools/ page: body only, the page itself is hand-written.
                _, body = split_frontmatter(read(src))
                body = absolute_links(convert_body(body, rel, {}), f'/maya/{rel}/')
                write(f'{PARTIALS}/tools/{TOOL_PAGES[rel]}.md', body)
                continue
            is_group_index = name == 'index.md' and rel != 'index'
            convert_page(src, rel, is_group_index)
    effect_variants.update(n for names in EFFECT_PAGES.values() for n in names if n.endswith('-watercolor'))
    for name in os.listdir(f'{OLD}/_includes/effects'):
        source = read(f'{OLD}/_includes/effects/{name}')
        base = name[:-3]
        variants = [(v, v[len(base) + 1:]) for v in effect_variants if v.startswith(base + '-') and '-' not in v[len(base) + 1:] and 'include.style' in source]
        for out_name, style in variants or [(base, None)]:
            text = source
            if style:
                # Evaluate the include's Liquid for this style.
                text = re.sub(r'\{%\s*if include\.style == "(\w+)"\s*%\}(.*?)\{%\s*endif\s*%\}',
                              lambda m: m.group(2) if m.group(1) == style else '', text, flags=re.S)
                text = text.replace('{{include.style}}', style)
            body = convert_body(text, f'effects/{out_name}', {})
            write(f'{PARTIALS}/effects/{out_name}.md', body)

    for page, names in EFFECT_PAGES.items():
        parts = []
        for i, name in enumerate(names):
            body = read(f'{PARTIALS}/effects/{name}.md')
            if i == 0:
                # The shared page title replaces the include's own heading.
                body = re.sub(r'\A### [^\n]*\n+', '', body)
            parts.append(body)
        body = '\n'.join(parts)
        # The "Art-directable" pills pointed at a section of the Maya style pages.
        body = re.sub(r'<a class="pill-link" href="[^"]*">([^<]*)</a>', r'<span class="pill-link">\1</span>', body)
        body = body.replace('](#line-width)', '](/effects/lines/#line-width)')
        write(f'{PARTIALS}/effect-pages/{page}.md', body)

    retarget_anchors()

    missing = []
    for ref in sorted(media_refs):
        src = f'{OLD}{ref}'
        if os.path.isfile(src):
            dst = f'{NEW}/public{ref}'
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        else:
            missing.append(ref)
    print(f'media copied: {len(media_refs) - len(missing)}, missing: {len(missing)}')
    for m in missing:
        print('  missing', m)
    for r in report:
        print(r)

    # Media is copied to the old site's paths above; this moves it next to the pages that use it.
    import organize_media
    organize_media.main()


if __name__ == '__main__':
    sys.exit(main())
