# approximate text width for Proxima Nova Bold (em units)
NARROW=set("iljtfrI.,:;'!|()[]")
WIDE=set("mwMW")
def cw(c):
    if c==" ": return 0.26
    if c in NARROW: return 0.33
    if c in WIDE: return 0.86
    if c in "✓×☐": return 0.7
    if c=="_": return 0.52
    if c=="—" or c=="–": return 0.8
    if c.isupper() or c.isdigit(): return 0.64 if c.isupper() else 0.58
    return 0.565
def width(s,fs): return sum(cw(c) for c in s)*fs
def lines(s,w,fs):
    n=0
    for par in s.split("\n"):
        words=par.split(" ")
        cur=0; n+=1
        for wd in words:
            ww=width(wd,fs); sp=width(" ",fs)
            if cur==0: cur=ww
            elif cur+sp+ww<=w: cur+=sp+ww
            else: n+=1; cur=ww
    return n
if __name__=="__main__":
    tests=[("Lengkapi kalimat berikut dengan kata atau tindakan yang tepat.",352,1),
           ("Lihat gambar berikut. Tulislah nama tempat atau benda di bawah gambar.",283,2),
           ("1. Ada bungkus makanan di lantai kelas.",142,2),
           ("Membiarkannya.\nMemungut dan membuangnya ke tempat sampah.",124,4),
           ("Bacalah setiap situasi. Pilih tindakan yang sebaiknya dilakukan, lalu tulis alasanmu.",294,2),
           ("Perhatikan kedua gambar. Berilah tanda ✓ pada gambar lingkungan yang lebih terawat. Jelaskan alasanmu.",290,3),
           ("Berilah tanda ✓ pada perilaku yang peduli lingkungan dan tanda × pada perilaku yang tidak peduli lingkungan.",294,3),
           ("1. Ada bungkus makanan di lantai kelas.",122,3),("2. Tanaman di halaman terlihat kering.",122,3),
           ("Amati kedua gambar. Tulislah tiga hal yang kamu lihat di setiap gambar.",294,2),
           ("Hari ini saya sudah bisa menjaga lingkungan dengan cara",449,1)]
    for s,w,exp in tests: print(lines(s,w,12),exp, round(width(s,12)), s[:30])
    for s in ["Lingkungan Rumah dan Sekolah","Mendengarkan Percakapan","Menghubungkan dengan Garis","Amati Gambar"]:
        print(s, round(width(s,16)))
