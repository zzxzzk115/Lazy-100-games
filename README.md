# LAZY-100 Games

The cartridge catalog for the [LAZY-100 fantasy console](https://github.com/zzxzzk115/Lazy-100) — play it on the web, browse it in-console with the `explore` command, or grab carts straight from this repo.

Every game lives in `games/<id>/` as a **`.lz100.png` PNG cartridge** — a playable cart whose visible cover art doubles as its preview image — and is listed in the machine-readable [`games.json`](games.json) index (validated by [`schema/games.schema.json`](schema/games.schema.json)). A plain-text `.lz100` may be included alongside for human code review.

## Playing

- **On the web**: open the [LAZY-100 site](https://zzxzzk115.github.io/Lazy-100/) and click a cartridge — it plays in place.
- **In the console**: type `explore` at the LAZY-100 shell — browse with the arrow keys, press Enter to download & play, `F` to favorite.
- **Manually**: download `games/<id>/<id>.lz100.png` into your local `carts/` folder, then `load <id>` and `run` (or just drag it onto the console window).

## Catalog format

`games.json`:

```json
{
  "schemaVersion": 1,
  "kind": "lazy100.gamesCatalog",
  "games": [
    {
      "id": "breakout",
      "name": "Breakout",
      "author": "Lazy_V",
      "description": "Classic brick-breaking arcade game.",
      "version": "1.0.0",
      "category": "arcade",
      "tags": ["classic", "arcade"],
      "license": "MIT",
      "repository": "https://github.com/zzxzzk115/Lazy-100",
      "featured": true,
      "cart": "games/breakout/breakout.lz100.png",
      "source": "games/breakout/breakout.lz100"
    }
  ]
}
```

| Field | Required | Notes |
|---|---|---|
| `id` | yes | `[a-z0-9_-]`, max 32 chars; doubles as the local cart filename |
| `name` | yes | Display name |
| `author` | yes | Author / maintainer |
| `description` | no | One-liner shown in the browser |
| `version` | yes | Semantic version (`1.0.0`) |
| `category` | yes | One of: arcade, action, puzzle, platformer, shooter, rpg, racing, sports, strategy, demo, tool, other |
| `tags` | no | Free-form short tags |
| `license` | no | SPDX id of the game itself |
| `repository` | no | The game's own source repo, if it has one |
| `featured` | no | `true` to feature it on the site's home page |
| `cart` | yes | `games/<id>/<id>.lz100.png` — the PNG cartridge (cover doubles as the preview) |
| `source` | no | `games/<id>/<id>.lz100` — plain-text cart, for code review |
| `preview` | no | A distinct preview PNG; omit to use the cart's own cover |

## Submitting a game

1. Fork, then add `games/<id>/` containing:
   - **`<id>.lz100.png`** — the PNG cartridge, exported from the console. Insert/author your cart, then export it as a cart image:
     ```
     save <id>.lz100.png
     ```
     or headlessly with the `cartshot` tool (output ending in `.lz100.png` packs the cart, any other name renders a plain preview):
     ```
     xmake build cartshot && xmake run cartshot carts/<id>.lz100 <id>.lz100.png
     ```
   - **`<id>.lz100`** *(optional)* — the plain-text cart, so reviewers can read the code.
2. Append your entry to `games.json` (see the schema above — `id` must match the folder and filename).
3. Open a pull request. Keep one game per PR.

Only LAZY-100 (`.lz100.png`) cartridges are catalogued.

## License

The catalog infrastructure is MIT. Each game keeps its own license (see its `license` field and source repository).
