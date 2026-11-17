#!/usr/bin/env python3
"""Pull the sales records out of a sales-map HTML file (the `const D=[...]` array)
and write data/sales.json for our-sales.html.

Usage: python3 tools/extract_sales.py path/to/thapar_sales_map.html
No network access and no geocoding: the coordinates already in the file are used as they are.
"""
import json, re, sys, pathlib

src = pathlib.Path(sys.argv[1]).read_text(encoding="utf8")
m = re.search(r"const D\s*=\s*(\[.*?\]);\s*\n", src, re.S)
if not m:
    sys.exit("Could not find `const D=[...]` in that file.")
records = json.loads(m.group(1))
need = {"lat", "lng", "year", "side", "addr", "city", "type", "price", "date", "id"}
bad = [r.get("id") for r in records if not need <= set(r)]
if bad:
    sys.exit(f"{len(bad)} records are missing fields, e.g. id {bad[0]}")
out = pathlib.Path(__file__).resolve().parent.parent / "data" / "sales.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"count": len(records), "records": records}, separators=(",", ":")), encoding="utf8")
years = sorted({r["year"] for r in records})
print(f"Wrote {out} with {len(records)} records, {years[0]} to {years[-1]}.")
