// Pagefind's search UI, pre-filtered to the reader's host.

// @ts-expect-error: @pagefind/default-ui ships no types (Starlight suppresses this the same way).
import { PagefindUI as BasePagefindUI } from '@pagefind/default-ui/npm_dist/mjs/ui-core.mjs';
import { currentHost, HOST_CHANGE_EVENT } from './hosts';

export class PagefindUI extends BasePagefindUI {
	constructor(opts: Record<string, unknown>) {
		super(opts);
		// triggerFilters() is undocumented but public on the 1.5.2 class (ui-core.mjs). It replaces
		// the selected filters, and Pagefind re-runs any open search when they change.
		// The sidebar switcher is the only host control, so the filter follows it. With no host
		// selected (a shared page on a first visit), {} clears the filter and everything is searched.
		const applyHost = () => {
			const host = currentHost();
			this.triggerFilters(host ? { host } : {});
		};
		applyHost();
		document.addEventListener(HOST_CHANGE_EVENT, applyHost);
	}
}
