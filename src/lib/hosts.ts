// Which hosts a page belongs to, and which host the reader is in.

export const HOSTS = ['unreal', 'maya'] as const;
export type Host = (typeof HOSTS)[number];

const SHARED_SECTIONS = ['effects', 'tools'];
const STORAGE_KEY = 'flair:host';

/** Hosts a docs entry belongs to, from its top-level folder. */
export function hostsForEntry(id: string): Host[] {
	// The folder decides, so a page can't be published untagged by forgetting frontmatter.
	// Pages outside every section (the landing page) get no tags and drop out of filtered search.
	const section = id.split('/')[0];
	if (SHARED_SECTIONS.includes(section)) return [...HOSTS];
	return HOSTS.filter((host) => host === section);
}

/** The reader's host: from the URL, else the last host page they visited. */
export function currentHost(): Host | undefined {
	const section = location.pathname.split('/')[1];
	const fromUrl = HOSTS.find((host) => host === section);
	try {
		if (fromUrl) {
			localStorage.setItem(STORAGE_KEY, fromUrl);
			return fromUrl;
		}
		// Shared pages (/effects/, /tools/) keep whichever host the reader came from.
		const stored = localStorage.getItem(STORAGE_KEY);
		return HOSTS.find((host) => host === stored);
	} catch {
		// Storage can be blocked (private windows, strict privacy settings). Shared pages then
		// search unfiltered, which is the safe fallback.
		return fromUrl;
	}
}
