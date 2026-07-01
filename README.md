# LAZY-100 Games

The cartridge catalog for the [LAZY-100 fantasy console](https://github.com/zzxzzk115/Lazy-100) — browse it in-console with the `explore` command, or grab carts straight from this repo.

Every game lives in `games/<id>/` as a **`.lz100` cart plus a 320x240 `preview.png`**, and is listed in the machine-readable [`games.json`](games.json) index (validated by [`schema/games.schema.json`](schema/games.schema.json)).

## Playing

- **In the console**: type `explore` at the LAZY-100 shell — browse with the arrow keys, press Enter to download & play, `F` to favorite.
- **Manually**: download `games/<id>/<id>.lz100` into your local `carts/` folder, then `load <id>` and `run`.

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
      "cart": "games/breakout/breakout.lz100",
      "preview": "games/breakout/preview.png"
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
| `cart` | yes | `games/<id>/<id>.lz100` |
| `preview` | yes | `games/<id>/preview.png`, 320x240 |

## Submitting a game

1. Fork, then add `games/<id>/` containing:
   - **`<id>.lz100`** — the cart in the plain-text `.lz100` format. **PNG carts are not accepted** (export the `.lz100` from the console instead); previews are separate images, not carriers.
   - **`preview.png`** — a 320x240 first-frame screenshot. Generate it with the console's `cartshot` tool so the colors match the LAZY-100 palette exactly:
     ```
     xmake build cartshot && xmake run cartshot carts/<id>.lz100 preview.png
     ```
2. Append your entry to `games.json` (see the schema above — `id` must match the folder and filename).
3. Open a pull request. Keep one game per PR.

## License

The catalog infrastructure is MIT. Each game keeps its own license (see its `license` field and source repository).
