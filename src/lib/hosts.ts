// Which hosts a page belongs to, and which host the reader is in.

export const HOSTS = ['unreal', 'maya'] as const;
export type Host = (typeof HOSTS)[number];
export const HOST_LABELS: Record<Host, string> = { unreal: 'UE', maya: 'Maya' };

const SHARED_SECTIONS = ['effects', 'tools'];
export const STORAGE_KEY = 'flair:host';
export const HOST_CHANGE_EVENT = 'flair:host-change';

/** `<Tabs syncKey>` for per-host tabs, and the tab label that names each host. */
export const HOST_TABS_SYNC_KEY = 'host';
export const HOST_TAB_LABELS: Record<Host, string> = { unreal: 'Unreal Engine', maya: 'Maya' };
/** Where Starlight remembers the selected tab for HOST_TABS_SYNC_KEY. */
export const HOST_TABS_STORAGE_KEY = `starlight-synced-tabs__${HOST_TABS_SYNC_KEY}`;

/** Hosts a docs entry belongs to, from its top-level folder. */
export function hostsForEntry(id: string): Host[] {
	// The folder decides, so a page can't be published untagged by forgetting frontmatter.
	// Pages outside every section (the landing page) get no tags and drop out of filtered search.
	const section = id.split('/')[0];
	if (SHARED_SECTIONS.includes(section)) return [...HOSTS];
	return HOSTS.filter((host) => host === section);
}

/** The reader's selected host, if any. */
export function currentHost(): Host | undefined {
	// HostHead.astro sets this before first paint, from the URL or the remembered host.
	// If storage is blocked, shared pages have no host and search everything, which is the safe fallback.
	const host = document.documentElement.dataset.host;
	return HOSTS.find((h) => h === host);
}

/** Selects the reader's host for the sidebar, search and per-host tabs, and remembers it. */
export function setHost(host: Host) {
	document.documentElement.dataset.host = host;
	try {
		localStorage.setItem(STORAGE_KEY, host);
		localStorage.setItem(HOST_TABS_STORAGE_KEY, HOST_TAB_LABELS[host]);
	} catch {}
	showHostTabs(host);
	document.dispatchEvent(new CustomEvent(HOST_CHANGE_EVENT));
}

type StarlightTabs = HTMLElement & {
	tabs: HTMLAnchorElement[];
	switchTab(tab: HTMLAnchorElement, index: number, shouldSync?: boolean): void;
};

function showHostTabs(host: Host) {
	// switchTab() and tabs are public on Starlight's <starlight-tabs> element (user-components/Tabs.astro).
	// shouldSync = false skips Starlight's own syncing, which would focus the tab and scroll the page
	// towards it. Every host tab group on the page is switched here instead, and the choice is already
	// stored under Starlight's key above.
	const selector = `starlight-tabs[data-sync-key="${HOST_TABS_SYNC_KEY}"]`;
	for (const group of document.querySelectorAll<StarlightTabs>(selector)) {
		const index = group.tabs.findIndex((tab) => tab.textContent?.trim() === HOST_TAB_LABELS[host]);
		if (index !== -1) group.switchTab(group.tabs[index], index, false);
	}
}
