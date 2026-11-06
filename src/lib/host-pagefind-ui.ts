// Pagefind's search UI, pre-filtered to the reader's host.

// @ts-expect-error: @pagefind/default-ui ships no types (Starlight suppresses this the same way).
import { PagefindUI as BasePagefindUI } from '@pagefind/default-ui/npm_dist/mjs/ui-core.mjs';
import { currentHost } from './hosts';

export class PagefindUI extends BasePagefindUI {
	constructor(opts: Record<string, unknown>) {
		super(opts);
		// triggerFilters() is undocumented but public on the 1.5.2 class (ui-core.js). It pre-ticks
		// the Host checkbox in the filter panel, so readers can untick it to search all hosts.
		// Starlight builds the search UI on every page load (when the browser is idle), so this
		// is also where the last visited host gets recorded.
		const host = currentHost();
		if (host) this.triggerFilters({ host });
	}
}
