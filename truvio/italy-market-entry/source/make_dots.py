# Builds the dotted Italy grid used by the mocks and build_italy_variants.jsx.
# Usage: python3 make_dots.py italy-ne50m.json 880 18 dots.json  (map height px, dot spacing px, output)
# Input: Italy from Natural Earth 1:50m admin 0 countries (public domain), lon/lat, projected with cos(42 deg).
import json, math, sys
g = json.load(open(sys.argv[1]))
H = float(sys.argv[2]); SP = float(sys.argv[3])
k = math.cos(math.radians(42))
polys = g['coordinates']
lons = [p[0] for poly in polys for ring in poly for p in ring]
lats = [p[1] for poly in polys for ring in poly for p in ring]
lo0, lo1, la0, la1 = min(lons), max(lons), min(lats), max(lats)
s = H / (la1 - la0)
W = (lo1 - lo0) * k * s
def inside(x, y, ring):
    c = False
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]; x2, y2 = ring[i - 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c
def land(lon, lat):
    for poly in polys:
        if inside(lon, lat, poly[0]) and not any(inside(lon, lat, h) for h in poly[1:]):
            return True
    return False
pts = []
y = SP / 2
while y < H:
    x = SP / 2
    while x < W:
        lon = lo0 + x / (k * s); lat = la1 - y / s
        if land(lon, lat): pts.append([round(x), round(y)])
        x += SP
    y += SP
def proj(lon, lat): return [round((lon - lo0) * k * s), round((la1 - lat) * s)]
cities = {n: proj(*c) for n, c in {'Milano': (9.19, 45.46), 'Torino': (7.69, 45.07), 'Bologna': (11.34, 44.49), 'Roma': (12.50, 41.90), 'Napoli': (14.27, 40.85), 'Bari': (16.87, 41.12), 'Palermo': (13.36, 38.12), 'Venezia': (12.33, 45.44), 'Firenze': (11.25, 43.77), 'Cagliari': (9.11, 39.22)}.items()}
print(json.dumps({'W': round(W), 'H': round(H), 'n': len(pts), 'cities': cities}))
json.dump({'W': round(W), 'H': round(H), 'pts': pts, 'cities': cities}, open(sys.argv[4], 'w'), separators=(',', ':'))
