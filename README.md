# Home Buyer Guide – The Thapar Team

Static site for GitHub Pages. No build step.

| File | What it is |
|---|---|
| `index.html` | The guide. Part 11 links to the two tools below. |
| `neighbourhood-map.html` | Restaurants, schools and parks near an address (Google Maps). Needs an API key. |
| `school-boundaries.html` | TDSB / TCDSB boundary viewer (Leaflet + OpenStreetMap, data embedded, no key). About 7 MB. |
| `config.js` | Where the Google Maps API key goes. |

## Add the Google Maps API key
1. In Google Cloud, create a key and enable **Maps JavaScript API**, **Places API (New)**, **Geocoding API** and **Maps Static API** (billing must be on).
2. Under *Application restrictions* choose **Websites** and add your Pages address, e.g. `https://<user>.github.io/home-buyer-guide/*` (and your custom domain if you add one).
3. Under *API restrictions* limit the key to those four APIs. Set a daily quota cap as a safety net.
4. Paste the key into `config.js`, commit, push. The key is visible in the page source by design; the referrer restriction is what protects it.

If `config.js` is left blank, the map page asks the visitor for a key and stores it in their browser only.

## Publish
Repo **Settings → Pages → Deploy from a branch**, pick the branch and `/ (root)`.

## Notes
- `school-boundaries.html` uses OpenStreetMap's public tile server, which is fine for light use; switch to a tile provider if traffic grows.
- Board boundary data is a snapshot (TCDSB 2025/26). Refresh it by regenerating the `DATA` / `TDSB` constants in that file.
