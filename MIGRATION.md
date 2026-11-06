# Content migration: redirects and open gaps

What's left of moving docs.artineering.io (Jekyll, frozen; `C:\DEV\flair-docs`) and the public Notion
docs (Public / Documentation) into this site. This repo is now the only source for both hosts; the Maya
converter that generated the first version lives in git history (`scripts/convert_maya.py`, removed in
the commit after the design pass). Delete this file once the redirects are live and the gaps are closed.

## Still to migrate

- Notion "Troubleshooting Dependencies" (Maya) → `/maya/troubleshooting-dependencies/`. Its zip and
  video are Notion uploads and need a new home (YouTube, GitHub release assets, or `public/`).
- The UE setup video on the Notion landing page, same question.

## Known gaps

- Unreal tabs on `/effects/` pages only name the effect layer(s); Notion has no per-effect parameter docs.
- For shared effects, the Maya tab uses the watercolor variant; the old Warp page's demo clips of Edge
  Darkening and Pigment were dropped (originals in the old repo's `media/styles/warp/`).
- Anchors already broken on the old site: `#lightmap` (flair-shader), `#line-light-response` and
  `#sketch-light-response`, `#function-getmayaattrs` and `#function-customimport` (API import-export).
- Maya pages still use the old site's HTML figures and classes, styled by `src/styles/content.css`.
  Converting them to Markdown images (and `src/assets/` optimization) is a later pass.

## Media

`/media/<page path>/<file>`, e.g. `/media/maya/styles/library/watercolor/` or `/media/effects/pigment/`,
stored in Git LFS. After moving pages, `python scripts/organize_media.py` re-files media and rewrites
links: a file used by several pages goes to the shared `/effects/` or `/tools/` page using it, else to
the deepest section those pages share (`/media/shared/` only across hosts).

## Redirects: Maya (docs.artineering.io → /maya/)

Every old `/flair/<path>/` maps to `/maya/<path>/`, except:

| Old page | New URL |
| --- | --- |
| `/` (home) | `/` |
| `/flair/art-direction/noisefx/` | `/tools/noisefx/` (shared, Maya tab) |
| `/flair/styles/presets/` | `/tools/style-presets/` (shared, Maya tab) |

## Redirects: Unreal (Notion → /unreal/)

| Notion page | New URL |
| --- | --- |
| Flair for Unreal Engine (landing) | `/unreal/` |
| Installation | `/unreal/installation/` |
| Artist Guide | `/unreal/artist-guide/` |
| ├ Getting Started with Flair for Unreal | `/unreal/artist-guide/getting-started/` |
| ├ Breakdown - Artist's Perspective | `/unreal/artist-guide/breakdown/` |
| ├ Create a Flair Style Actor | `/unreal/artist-guide/create-style-actor/` |
| ├ Using Presets to save/load styles | `/tools/style-presets/` (shared) |
| ├ Breaking down the Flair Style Actor | `/unreal/artist-guide/style-actor/` |
| ├ NoiseFX | `/tools/noisefx/` (shared) |
| ├ Animating in Sequencer | `/unreal/artist-guide/sequencer/` |
| └ Tips and Best Practices | `/unreal/artist-guide/tips/` |
| Technical Artist Guide | `/unreal/technical-artist-guide/` |
| ├ Breakdown - Technical Artist's Perspective | `/unreal/technical-artist-guide/breakdown/` |
| ├ Mix-and-Match Flair Effect Layers | `/unreal/technical-artist-guide/mix-and-match/` |
| ├ Create / Breaking down / Parameters / Control Definitions / Custom Render Passes / Iterative / Seamless Textures | `/unreal/technical-artist-guide/effect-layers/<page>/` |
| └ Create a Flair PPM / Authoring Flair PPMs | `/unreal/technical-artist-guide/ppms/<page>/` |
