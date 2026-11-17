# Home Buyer Guide – The Thapar Team

Static site for GitHub Pages. No build step.

| File | What it is |
|---|---|
| `index.html` | The guide: an intake questionnaire (part 1) and ten parts with calculators. Part 6 embeds the two tools below as tabs ("Nearby places" and "School boundaries"), with an "Open full screen" link to each. |
| `neighbourhood-map.html` | Restaurants, schools and parks near an address (Google Maps). Needs an API key. Accepts `?embed=1&address=...` when loaded inside the guide. |
| `school-boundaries.html` | TDSB / TCDSB boundary viewer (Leaflet + OpenStreetMap, data embedded, no key). About 7 MB, so the guide only loads it when someone opens the School boundaries tab. |
| `config.js` | Where the Google Maps API key goes. |
| `our-sales.html` | Map of homes we have sold and bought (Leaflet + OpenStreetMap, no key). Reads `data/sales.json`. Shown in part 12. |
| `tools/build-sales.html` | Private, unlinked tool that turns MLS exports into `data/sales.json`. |
| `vendor/` | Self-hosted Leaflet, marker clustering and SheetJS (no CDN). |

## Add the Google Maps API key
1. In Google Cloud, create a key and enable **Maps JavaScript API**, **Places API (New)**, **Geocoding API** and **Maps Static API** (billing must be on).
2. Under *Application restrictions* choose **Websites** and add your Pages address, e.g. `https://<user>.github.io/home-buyer-guide/*` (and your custom domain if you add one).
3. Under *API restrictions* limit the key to those four APIs. Set a daily quota cap as a safety net.
4. Paste the key into `config.js`, commit, push. The key is visible in the page source by design; the referrer restriction is what protects it.

If `config.js` is left blank, the map page asks the visitor for a key and stores it in their browser only.

## Updating the sales map
1. Open `https://<user>.github.io/home-buyer-guide/tools/build-sales.html` (it has to be opened from the site so the Google key's website restriction allows it).
2. Choose the MLS exports (`.xlsx`), press **Read files**, then **Look up locations**, then **Download sales.json**.
3. Put the file at `data/sales.json` and push. Leave "Add to the map data already on the site" ticked to add new years without redoing old ones.

Privacy: the exports are read in the browser and never uploaded. `sales.json` keeps only a pin rounded to about 100 m, the year, property type, city and type of transaction (sold for seller, bought for buyer, or both sides). No street addresses, prices, MLS numbers or agent names. Do not commit the raw exports (`.gitignore` blocks `.xlsx` and `.csv`). Lookups that Google can only place approximately are listed in the tool and left off the map.

## Publish
Repo **Settings → Pages → Deploy from a branch**, pick the branch and `/ (root)`.

## Keeping figures current
These are hard-coded in `index.html` and go stale. Check them monthly:
- Market data: the `AREAS` / `GTA` constants and `SRC_TRREB` (TRREB Market Watch).
- Mortgage rate: the `rate:4.34` default and the Ratehub note beside the rate input.
- Program dates and limits in part 3 (HST/GST rebates, Home Renovation Savings Program end date, municipal down payment programs).

## How the calculators treat first-time buyers
Question 1 asks the federal four-year test. A "yes" opens a follow-up asking whether the buyer has ever owned a home anywhere, because the Ontario and Toronto land transfer tax refunds use a lifetime test. The refunds are only applied in parts 4 and 10 when the buyer answers "No, never" (`lttRefundOK` in `index.html`).

## Notes
- `school-boundaries.html` uses OpenStreetMap's public tile server, which is fine for light use; switch to a tile provider if traffic grows.
- Board boundary data is a snapshot (TCDSB 2025/26). Refresh it by regenerating the `DATA` / `TDSB` constants in that file.
