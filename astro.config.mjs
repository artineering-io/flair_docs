// @ts-check
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	site: 'https://docs.flair.graphics',
	integrations: [
		starlight({
			title: 'Flair',
			sidebar: [
				{ label: 'Unreal Engine', items: [{ autogenerate: { directory: 'unreal' } }] },
				{ label: 'Maya', items: [{ autogenerate: { directory: 'maya' } }] },
				{ label: 'Effects', items: [{ autogenerate: { directory: 'effects' } }] },
				{ label: 'Tools', items: [{ autogenerate: { directory: 'tools' } }] },
			],
			components: {
				PageTitle: './src/components/HostPageTitle.astro',
			},
		}),
	],
	vite: {
		resolve: {
			alias: [
				{
					// Starlight's Search.astro creates the Pagefind UI internally and never exposes it,
					// so we can't call triggerFilters() from outside. Redirecting this exact import name
					// swaps in a host-aware subclass without copying Starlight's search component.
					// Only the bare name matches: the subclass's deep import and the CSS import pass through.
					find: /^@pagefind\/default-ui$/,
					replacement: fileURLToPath(new URL('./src/lib/host-pagefind-ui.ts', import.meta.url)),
				},
			],
		},
	},
});
