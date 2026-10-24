# Builds the letter-road outline of Italy for the "Siamo finalmente in Italia" film.
# Usage: python3 make_road.py italy-ne50m.json 880 road.json  (map height px, output)
# Mainland, Sicily and Sardinia from Natural Earth 1:50m (public domain), projected with cos(42 deg) like make_dots.py.
# The road starts at the Tarvisio corner in the north-east and runs clockwise on screen, so letters stand on the outside.
# At the toe it loops once round Sicily and comes back. Sardinia is its own closed ring.
import json, math, sys
g = json.load(open(sys.argv[1]))
H = float(sys.argv[2])
k = math.cos(math.radians(42))

def area(r):
    return sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r))) / 2

mainland, sicily, sardinia = [p[0][:-1] for p in sorted(g['coordinates'], key=lambda p: -abs(area(p[0])))[:3]]
pts = mainland + sicily + sardinia
lo0, lo1 = min(p[0] for p in pts), max(p[0] for p in pts)
la0, la1 = min(p[1] for p in pts), max(p[1] for p in pts)
s = H / (la1 - la0)
W = (lo1 - lo0) * k * s
def proj(lon, lat): return [(lon - lo0) * k * s, (la1 - lat) * s]

def rdp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1e-9
    d = [abs(dy * (x - x1) - dx * (y - y1)) / n for x, y in pts[1:-1]]
    i = max(range(len(d)), key=d.__getitem__)
    if d[i] < tol: return [pts[0], pts[-1]]
    return rdp(pts[:i + 2], tol)[:-1] + rdp(pts[i + 1:], tol)

def chaikin(ring, n):
    for _ in range(n):
        out = []
        for i in range(len(ring)):
            (x1, y1), (x2, y2) = ring[i], ring[(i + 1) % len(ring)]
            out += [[0.75 * x1 + 0.25 * x2, 0.75 * y1 + 0.25 * y2], [0.25 * x1 + 0.75 * x2, 0.25 * y1 + 0.75 * y2]]
        ring = out
    return ring

def resample(ring, step):
    out, carry = [], 0.0
    for i in range(len(ring)):
        (x1, y1), (x2, y2) = ring[i], ring[(i + 1) % len(ring)]
        d = math.dist((x1, y1), (x2, y2))
        t = carry
        while t < d:
            out.append([x1 + (x2 - x1) * t / d, y1 + (y2 - y1) * t / d]); t += step
        carry = t - d
    return out

def relax(ring, radius, iters):
    # Moving average round the closed ring: irons out hooks tighter than a letter, keeps the coastline's shape.
    n = len(ring)
    for _ in range(iters):
        ring = [[sum(ring[(i + j) % n][k] for j in range(-radius, radius + 1)) / (2 * radius + 1) for k in (0, 1)] for i in range(n)]
    return ring

def prep(ring, start, tol=5, smooth=3):
    r = [proj(*p) for p in ring]
    i = min(range(len(r)), key=lambda j: math.dist(r[j], start))
    r = r[i:] + r[:i]
    far = max(range(len(r)), key=lambda j: math.dist(r[j], r[0]))  # split the closed ring so RDP has two distinct ends
    r = rdp(r[:far + 1], tol)[:-1] + rdp(r[far:] + [r[0]], tol)[:-1]
    r = chaikin(r, smooth)
    r = relax(resample(r, 3), 5, 3)[::3]
    if area(r) > 0: r = r[:1] + r[1:][::-1]  # area() is negative for clockwise on screen (y down)
    i = min(range(len(r)), key=lambda j: math.dist(r[j], start))
    return r[i:] + r[:i]

north = proj(13.72, 46.52)  # Tarvisio corner, where the tail joins the Alps
main = prep(mainland, north)
toe = min(range(len(main)), key=lambda j: math.dist(main[j], proj(15.64, 37.95)))
sic = prep(sicily, proj(15.62, 38.27))
sar = prep(sardinia, proj(9.45, 41.25))
road = main[:toe + 1] + sic + [sic[0]] + main[toe:] + [main[0]]
marks = {'toe': toe, 'sicilyEnd': toe + len(sic) + 1}
r1 = lambda ring: [[round(x, 1), round(y, 1)] for x, y in ring]
out = {'W': round(W), 'H': round(H), 'road': r1(road), 'sardinia': r1(sar + [sar[0]]), 'marks': marks,
       'cities': {n: [round(v, 1) for v in proj(*c)] for n, c in {'Milano': (9.19, 45.46), 'Roma': (12.50, 41.90), 'Lecce': (18.17, 40.35)}.items()}}
json.dump(out, open(sys.argv[3], 'w'), separators=(',', ':'))
print(out['W'], out['H'], len(road), len(sar), marks)
