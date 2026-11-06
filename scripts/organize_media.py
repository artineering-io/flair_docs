"""Move every file in public/media into a folder that mirrors the page that uses it, and rewrite links.

Layout: /media/<page path>/<file>, e.g. /media/maya/styles/library/watercolor/brush.png or
/media/effects/pigment/granulation.png. Pages that import partials count as using the partial's media.

Owner of a file used by several pages: a shared /effects/ or /tools/ page if one uses it (that page is
the effect's or tool's home), otherwise the deepest section all its pages sit in (/media/shared/ only
when they span hosts). Idempotent: run it after moving or renaming pages. Pass --dry-run to print
the plan without touching anything.
"""
import filecmp
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
DOCS = f'{ROOT}/src/content/docs'
PARTIALS = f'{ROOT}/src/partials'
PUBLIC = f'{ROOT}/public'
MEDIA = f'{PUBLIC}/media'

REF = re.compile(r'/media/[^\s)"\'<>#?]+')
IMPORT = re.compile(r'''^import\s+.*?\s+from\s+['"]([^'"]+\.md)['"]''', re.M)
SHARED_SECTIONS = ('effects', 'tools')


def read(path):
	with open(path, encoding='utf-8') as f:
		return f.read()


def write(path, text):
	with open(path, 'w', encoding='utf-8', newline='\n') as f:
		f.write(text)


def walk(directory, extensions):
	for root, _, files in os.walk(directory):
		for name in files:
			if name.endswith(extensions):
				yield os.path.join(root, name).replace('\\', '/')


def page_path(file):
	"""Content file -> the page's URL path without slashes, e.g. 'maya/styles' for maya/styles/index.md."""
	rel = re.sub(r'\.mdx?$', '', file[len(DOCS) + 1:])
	return re.sub(r'(^|/)index$', '', rel)


def media_users():
	"""Map each referenced /media/ path to the set of pages that show it."""
	partial_pages = defaultdict(set)
	pages = list(walk(DOCS, ('.md', '.mdx')))
	for file in pages:
		for target in IMPORT.findall(read(file)):
			partial = os.path.normpath(os.path.join(os.path.dirname(file), target)).replace('\\', '/')
			partial_pages[partial].add(page_path(file))

	users = defaultdict(set)
	for file in pages:
		for ref in REF.findall(read(file)):
			users[ref].add(page_path(file))
	for file in walk(PARTIALS, ('.md',)):
		for ref in REF.findall(read(file)):
			users[ref] |= partial_pages.get(file, set())
	return users


def owner(pages):
	# The home page (path '') only showcases images that belong to other pages, so it never owns one
	# unless nothing else uses it.
	pages = {p for p in pages if p} or pages
	if len(pages) == 1:
		return next(iter(pages))
	shared = sorted(p for p in pages if p.split('/')[0] in SHARED_SECTIONS)
	if len(shared) == 1:
		return shared[0]
	# The deepest section all the pages sit in, e.g. maya/materials for flair-shader and proxy-material.
	# This keeps a file inside its host's tree; only media spanning hosts lands in /media/shared/.
	common = os.path.commonpath(pages).replace('\\', '/')
	return common or 'shared'


def plan_moves(users):
	"""Map old /media/ path -> new /media/ path. Same-named files from different folders that land in one
	folder keep one copy when identical, otherwise the later one is prefixed with its old folder name."""
	moves, taken = {}, {}
	for ref in sorted(users):
		if not users[ref]:
			continue  # Only in a partial nobody imports; leave it where it is.
		name = ref.rsplit('/', 1)[1]
		folder = f'/media/{owner(users[ref])}'
		new = f'{folder}/{name}'
		if new in taken and taken[new] != ref and not filecmp.cmp(PUBLIC + taken[new], PUBLIC + ref, shallow=False):
			new = f'{folder}/{ref.rsplit("/", 2)[1]}-{name}'
		taken.setdefault(new, ref)
		if new != ref:
			moves[ref] = new
	return moves


def main():
	dry_run = '--dry-run' in sys.argv
	users = media_users()
	missing = sorted(ref for ref in users if not os.path.isfile(PUBLIC + ref))
	present = {ref: pages for ref, pages in users.items() if ref not in missing}
	moves = plan_moves(present)

	if dry_run:
		for old, new in sorted(moves.items()):
			print(f'{old} -> {new}   ({", ".join(sorted(present[old]))})')
	else:
		for old, new in moves.items():
			src, dst = PUBLIC + old, PUBLIC + new
			os.makedirs(os.path.dirname(dst), exist_ok=True)
			if os.path.exists(dst):
				os.remove(src)
			else:
				os.replace(src, dst)
		for file in list(walk(DOCS, ('.md', '.mdx'))) + list(walk(PARTIALS, ('.md',))):
			text = read(file)
			new_text = REF.sub(lambda m: moves.get(m.group(0), m.group(0)), text)
			if new_text != text:
				write(file, new_text)
		for root, dirs, files in os.walk(MEDIA, topdown=False):
			if not dirs and not files and root != MEDIA:
				os.rmdir(root)
			elif not os.listdir(root) and root != MEDIA:
				os.rmdir(root)

	referenced = set(present) if dry_run else {moves.get(ref, ref) for ref in present}
	unused = sorted(f[len(PUBLIC):] for f in walk(MEDIA, ('',)) if f[len(PUBLIC):] not in referenced)
	print(f'moved: {len(moves)}, missing: {len(missing)}, unused: {len(unused)}')
	for ref in missing:
		print('  missing', ref)
	for ref in unused:
		print('  unused', ref)


if __name__ == '__main__':
	main()
