import json,math
from tw import width as tw, lines as tl
SQ="M0 0H64V64H0z"; CIRC="M32 0A32 32 0 1 0 32 64A32 32 0 1 0 32 0Z"
BLUE="#23a6df"; LBLUE="#aae0fa"; PALE="#d9f0fb"; DARK="#2f4048"
COLS={"L":(76.69,307.32),"R":(399.58,315.21),"F":(76.69,638.11)}
class Page:
    def __init__(s,pid,roles,fs=12):
        s.pid=pid; s.ops=[]; s.front=[]; s.fs=fs
        s.pool=list(roles["pool"])+list(roles["spares"])
        s.used=[]; s.added=0; s.notes=[]
    # ---- primitives
    def shape(s,t,l,w,h,fill=None,stroke=None,sw=1,r=0,path=SQ):
        o={"type":"insert_shape","page_id":s.pid,"top":round(t,2),"left":round(l,2),"width":round(max(w,1),2),"height":round(max(h,1),2),"path":path,"view_box_width":64,"view_box_height":64}
        if fill: o["color"]=fill
        if stroke: o["stroke_color"]=stroke; o["stroke_weight"]=sw
        if r: o["corner_rounding"]=r
        s.ops.append(o)
    def line(s,y,x0,x1): s.shape(y,x0,x1-x0,1,fill=BLUE)
    def cb(s,t,l,sz=12): s.shape(t,l,sz,sz,fill="#ffffff",stroke=DARK,sw=1,r=3)
    def frame(s,t,l,w,h): s.shape(t,l,w,h,stroke=LBLUE,sw=1,r=8)
    def text(s,txt,t,l,w,fs=None,lh=1.2,align="start",color="#000000",weight="bold",loc=None,front=False):
        fs=fs or s.fs
        if not str(txt).strip() and loc is None: return
        if loc is None:
            if s.pool: loc=s.pool.pop(0)
            else:
                s.ops.append({"type":"add_text","page_id":s.pid,"text":txt,"top":round(t,2),"left":round(l,2),"width":round(w,2)})
                s.added+=1; return
        s.used.append(loc)
        s.ops.append({"type":"replace_text","locator_id":loc,"text":txt})
        s.ops.append({"type":"format_text","locator_id":loc,"formatting":{"font_size":int(fs),"font_weight":weight,"color":color,"text_align":align,"line_height":lh,"list_level":0}})
        s.ops.append({"type":"resize_element","locator_id":loc,"width":round(w,2)})
        s.ops.append({"type":"position_element","locator_id":loc,"top":round(t,2),"left":round(l,2)})
        if front or getattr(s,"force_front",False): s.front.append(loc)
    def nlines(s,txt,w,fs=None): return tl(txt,w,fs or s.fs)
    def finish(s,deletes):
        for d in deletes: s.ops.append({"type":"delete_element","locator_id":d})
        for loc in s.pool: s.ops.append({"type":"delete_element","locator_id":loc})
        for loc in s.front: s.ops.append({"type":"layer_element","locator_id":loc,"position":"front"})
        return s.ops
# ---------------- items: each returns (height, render(y,x0,x1))
def H(pg,items,W):
    return sum(item_h(pg,it,W) for it in items)
def item_h(pg,it,W):
    k=it[0]; fs=pg.fs; o=it[-1] if isinstance(it[-1],dict) else {}
    if k=="T": return pg.nlines(it[1],W-o.get("indent",0))*fs*o.get("lh",1.2)+o.get("after",5)
    if k=="FILL": return fill_layout(pg,it[1],W,o)[0]+o.get("after",4)
    if k=="OPTS": return opts_layout(pg,it[1],W,o)[0]+o.get("after",4)
    if k=="FRAMES":
        n,cols,h=it[1],it[2],it[3]; rows=math.ceil(n/cols)
        return rows*(h+frames_extra(pg,it,W))+(rows-1)*o.get("gap",6)+o.get("after",6)
    if k=="COLS":
        ws=split(W,o); return max(H(pg,sub,w) for sub,w in zip(it[1],ws))
    if k=="BOX":
        return pg.nlines(it[1],W-16)*fs*1.3+10+o.get("after",6)
    if k=="TABLE":
        rh=o.get("rowh",19); return rh*(len(it[2])+1)+o.get("after",6)
    if k=="MATCH": return match_layout(pg,it[1],it[2],W,o)[0]+o.get("after",4)
    if k=="GAP": return it[1]
    if k=="LINES": return it[1]*o.get("pitch",20)+o.get("after",4)
    if k=="FOUR": return it[1]*30+o.get("after",4)
    if k=="CARD":
        return H(pg,it[1],W-12)+8+o.get("after",5)
    raise Exception(k)
def frames_extra(pg,it,W):
    n,cols,h=it[1],it[2],it[3]; o=it[-1] if isinstance(it[-1],dict) else {}
    fw=(W-(cols-1)*7)/cols; e=0
    if o.get("line") or o.get("num"): e+=20
    if o.get("sq"): e+=22
    if o.get("labels"): e+=max(pg.nlines(l,fw) for l in o["labels"])*pg.fs*1.2+4
    return e
def split(W,o):
    fr=o.get("frac",[0.5,0.5]); g=o.get("gap",10)
    tot=W-g*(len(fr)-1); return [tot*f for f in fr]
def fill_layout(pg,rows,W,o):
    fs=pg.fs; lh=o.get("lh",1.6); p=fs*lh; txt=[]; blanks=[]; i=0
    minblank=o.get("minblank",45)
    for r in rows:
        if isinstance(r,tuple): label,tail=r
        else: label,tail=r,""
        lw=tw(label,fs); tailw=tw(tail,fs) if tail else 0
        if label and pg.nlines(label,W)>1 or lw+minblank+tailw>W:
            # label on its own line(s), blank on next line
            n=pg.nlines(label,W); txt.append(label+"\n"+(" "*1)); 
            # blank line full width on line i+n
            blanks.append((i+n,0,W-tailw-2,tail)); i+=n+1
        else:
            txt.append(label+(" " if label else "")); blanks.append((i,lw+(5 if label else 0),W-tailw-2,tail)); i+=1
    return i*p,txt,blanks,p
def opts_layout(pg,opts,W,o):
    fs=pg.fs; lh=o.get("lh",1.3); p=fs*lh; cols=o.get("cols",1)
    ws=split(W,{"frac":[1/cols]*cols,"gap":10}); per=math.ceil(len(opts)/cols)
    colsd=[];mx=0
    for c in range(cols):
        part=opts[c*per:(c+1)*per]; li=0; starts=[]
        for op in part:
            starts.append(li); li+=pg.nlines(op,ws[c]-18)
        colsd.append((part,starts,li)); mx=max(mx,li)
    return mx*p,colsd,ws,p
def match_layout(pg,L,R,W,o):
    fs=pg.fs; wl=o.get("wl",W*0.46); wr=W-wl-o.get("mid",34); p=fs*1.2
    rows=[];y=0
    n=max(len(L),len(R))
    pitch=o.get("pitch")
    hs=[]
    for i in range(n):
        a=L[i] if i<len(L) else ""; b=R[i] if i<len(R) else ""
        h=max(pg.nlines(a,wl-10),pg.nlines(b,wr-10))*p+10
        hs.append(h)
    if pitch: hs=[max(h,pitch) for h in hs]
    return sum(hs)+(n-1)*4,wl,wr,hs
def render(pg,items,y,x0,x1):
    W=x1-x0
    for it in items:
        k=it[0]; fs=pg.fs; o=it[-1] if isinstance(it[-1],dict) else {}
        h=item_h(pg,it,W)
        if k=="T":
            ind=o.get("indent",0)
            pg.text(it[1],y,x0+ind,W-ind,lh=o.get("lh",1.2),align=o.get("align","start"))
        elif k=="FILL":
            tot,txt,blanks,p=fill_layout(pg,it[1],W,o)
            pg.text("\n".join(txt) if any(t.strip() for t in txt) else " ",y,x0,W,lh=o.get("lh",1.6))
            for (li,bx0,bx1,tail) in blanks:
                ly=y+li*p+p/2+fs*0.45
                pg.line(ly,x0+bx0,x0+bx1)
            tails=[b for b in blanks if b[3]]
            # tails (e.g. "baris") rendered as one extra text aligned right
            if tails:
                ttxt="\n".join((b[3] if b in tails else " ") for b in blanks)
                pg.text(ttxt,y,x0+W-max(tw(b[3],fs) for b in tails)-1,max(tw(b[3],fs) for b in tails)+4,lh=o.get("lh",1.6))
        elif k=="OPTS":
            tot,colsd,ws,p=opts_layout(pg,it[1],W,o); cx=x0
            for (part,starts,li),w in zip(colsd,ws):
                if part:
                    pg.text("\n".join(part),y,cx+18,w-18,lh=o.get("lh",1.3))
                    for st in starts: pg.cb(y+st*p+(p-12)/2,cx+1)
                cx+=w+10
        elif k=="FRAMES":
            n,cols,fh=it[1],it[2],it[3]; g=o.get("gap",6); fw=(W-(cols-1)*7)/cols
            extra=frames_extra(pg,it,W)
            for i in range(n):
                r,c=divmod(i,cols); fx=x0+c*(fw+7); fy=y+r*(fh+extra+g)
                pg.frame(fy,fx,fw,fh)
                if o.get("cb"): pg.cb(fy+fh-17,fx+fw-17,13)
                if o.get("inum"): pg.text(str(i+1),fy+3,fx+5,20)
                ly=fy+fh
                if o.get("labels"):
                    lh_=max(pg.nlines(l,fw) for l in o["labels"])*fs*1.2+4
                    pg.text(o["labels"][i],ly+2,fx,fw,align="center"); ly+=lh_
                if o.get("sq"): pg.shape(ly+4,fx+fw/2-8,16,16,stroke=DARK,sw=1,r=3)
                if o.get("num"):
                    pg.text(f"{i+1}.",ly+4,fx,18); pg.line(ly+16,fx+16,fx+fw-3)
                elif o.get("line"): pg.line(ly+16,fx+3,fx+fw-3)
        elif k=="COLS":
            ws=split(W,o); cx=x0
            for sub,w in zip(it[1],ws):
                render(pg,sub,y,cx,cx+w); cx+=w+o.get("gap",10)
        elif k=="BOX":
            bh=pg.nlines(it[1],W-16)*fs*1.3+10
            pg.shape(y,x0,W,bh,fill=PALE,r=8)
            pg.text(it[1],y+5,x0+8,W-16,lh=1.3,align="center",front=True)
        elif k=="TABLE":
            heads,rows=it[1],it[2]; rh=o.get("rowh",19); fr=o.get("frac"); 
            fr=fr or [1/len(heads)]*len(heads); ws=[W*f for f in fr]
            th=rh*(len(rows)+1)
            if not o.get("plain"): pg.shape(y,x0,W,rh,fill=PALE,r=0)
            pg.frame(y,x0,W,th)
            for ri in range(1,len(rows)+1): pg.shape(y+ri*rh,x0,W,1,fill=LBLUE)
            cx=x0
            for ci,w in enumerate(ws):
                if ci>0: pg.shape(y,cx,1,th,fill=LBLUE)
                cells=[heads[ci]]+[r[ci] for r in rows]
                al="center" if (o.get("center",True) and ci>0) or o.get("center_all") else "start"
                tcells=[]
                for ri,cval in enumerate(cells):
                    ty=y+ri*rh
                    if cval=="☐": pg.cb(ty+(rh-12)/2,cx+w/2-6); tcells.append(" ")
                    elif cval=="___": pg.line(ty+rh-5,cx+6,cx+w-6); tcells.append(" ")
                    elif cval.endswith("___"):
                        lab=cval[:-3]; tcells.append(lab); pg.line(ty+rh-5,cx+6+tw(lab,fs)+4,cx+w-6)
                    else: tcells.append(cval)
                if any(c.strip() for c in tcells):
                    pg.text("\n".join(tcells),y+(rh-fs*min(2.5,rh/fs))/2,cx+4,w-8,lh=min(2.5,rh/fs),align=al,front=not o.get("plain"))
                cx+=w
        elif k=="MATCH":
            tot,wl,wr,hs=match_layout(pg,it[1],it[2],W,o); yy=y
            L,R=it[1],it[2]
            for i,hh in enumerate(hs):
                if i<len(L):
                    pg.frame(yy,x0,wl,hh-2); pg.text(L[i],yy+5,x0+5,wl-10)
                    pg.shape(yy+(hh-2)/2-3.5,x0+wl+5,7,7,fill=DARK,path=CIRC)
                if i<len(R):
                    rx=x0+W-wr
                    pg.frame(yy,rx,wr,hh-2); pg.text(R[i],yy+5,rx+5,wr-10)
                    pg.shape(yy+(hh-2)/2-3.5,rx-12,7,7,fill=DARK,path=CIRC)
                yy+=hh+4
        elif k=="LINES":
            pt=o.get("pitch",20)
            for i in range(it[1]): pg.line(y+(i+1)*pt-3,x0,x1)
        elif k=="FOUR":
            for i in range(it[1]):
                by=y+i*30
                for j,c in enumerate([LBLUE,"#f7b7b7",LBLUE,LBLUE]): pg.shape(by+2+j*7,x0,W,1,fill=c)
        elif k=="CARD":
            ch=H(pg,it[1],W-12)+8
            pg.frame(y,x0,W,ch); render(pg,it[1],y+5,x0+6,x1-6)
        elif k=="GAP": pass
        y+=h
    return y
# --------------- page layout
def build_page(roles,spec,deletes_extra=(),fs=12):
    pg=Page(roles["pid"],roles,fs)
    secs=spec["secs"]; rows=spec.get("rows")
    if not rows:
        nums=[s["n"] for s in secs]; rows=[]
        i=0
        while i<len(nums):
            if i+1<len(nums) and not secs[i].get("full") and not secs[i+1].get("full"): rows.append((nums[i],nums[i+1])); i+=2
            else: rows.append((nums[i],)); i+=1
    S={s["n"]:s for s in secs}
    # refleksi geometry
    refl=spec.get("refl")
    rW=707-234-24
    rh=H(pg,refl["items"],rW)+14 if refl else 0
    strip_h=max(79.36,rh+10) if refl else 0
    strip_top=1068.3-strip_h if refl else 1068
    bottom=strip_top-14 if refl else 1060
    # compute box heights
    def boxh(n,col):
        s=S[n]; x,w=COLS[col]; W=w-17.75
        ih=pg.nlines(s["instr"],W)*fs*1.2 if s.get("instr") else 0
        return 28.5+ih+7+H(pg,s["items"],W)+6
    def cell_h(c,col):
        if isinstance(c,tuple): return sum(boxh(n,col) for n in c)+30*(len(c)-1)
        return boxh(c,col)
    rowh=[]
    for r in rows:
        if len(r)==2: rowh.append(max(cell_h(r[0],"L"),cell_h(r[1],"R")))
        else: rowh.append(cell_h(r[0],"F"))
    gap=30; top0=201.22
    total=sum(rowh)+gap*(len(rows)-1)
    avail=bottom-top0
    info=dict(total=round(total),avail=round(avail),rowh=[round(h) for h in rowh],fs=fs)
    if total>avail:
        gap=max(27,gap-(total-avail)/max(1,len(rows)-1)); total=sum(rowh)+gap*(len(rows)-1)
    info["gap"]=round(gap,1); info["over"]=round(total-avail)
    T=top0
    tmpl={b["numtxt"]:b for b in roles["boxes"] if b["numtxt"]}
    used_tmpl=set()
    def draw(n,col,T,h):
        x,w=COLS[col]; s=S[n]
        tb=tmpl.get(str(n)) if spec.get("reuse",True) else None
        title=s["title"]; tfs=16
        tw_=tw(title,tfs)*1.04
        maxpill=w-5; pill=min(maxpill,41+tw_+14)
        if 41+tw_+6>maxpill: tfs=14; tw_=tw(title,14)*1.04; pill=min(maxpill,41+tw_+14)
        if tb:
            used_tmpl.add(str(n))
            if tb["box"]: pg.ops.extend([{"type":"resize_element","locator_id":tb["box"],"width":round(w,2),"height":round(h,2)},
                      {"type":"position_element","locator_id":tb["box"],"top":round(T,2),"left":round(x,2)}])
            else:
                pg.shape(T,x,w,h,stroke=LBLUE,sw=1,r=10)
                pg.front+=[tb[k] for k in ("pill","circ","num","title") if tb[k]]
            pg.ops.extend([{"type":"resize_element","locator_id":tb["pill"],"width":round(pill,2),"height":39.4},
                      {"type":"position_element","locator_id":tb["pill"],"top":round(T-19.5,2),"left":round(x+7.18,2)},
                      {"type":"position_element","locator_id":tb["circ"],"top":round(T-24.9,2),"left":round(x-12.23,2)}])
        else:
            pg.shape(T,x,w,h,stroke=LBLUE,sw=1,r=10)
            pg.shape(T-19.5,x+7.18,pill,39.4,fill="#feefbc",r=20)
            pg.shape(T-24.9,x-12.23,49.84,49.84,fill="#f8c357",path=CIRC)
        lab=s.get("label",str(n)); nw=26 if len(lab)>1 else 15.24
        pg.text(lab,T-11.5,x+12.69-nw/2,nw,fs=20,lh=1.4,align="center",color="#ffffff",loc=tb["num"] if tb else None,front=not tb)
        pg.text(title,T-9.4+(1.2 if tfs==14 else 0),x+47.96,max(pill-41-4,tw_+2),fs=tfs,lh=1.4,color=DARK,loc=tb["title"] if tb else None,front=not tb)
        W=w-17.75; x0=x+8.95; y=T+28.5
        if s.get("instr"):
            pg.text(s["instr"],y,x0,W,lh=1.2,loc=tb["instr"] if tb else None)
            y+=pg.nlines(s["instr"],W)*fs*1.2
        elif tb and tb["instr"]: pg.pool.append(tb["instr"])
        y+=7
        render(pg,s["items"],y,x0,x0+W)
    for r,h in zip(rows,rowh):
        for idx,c in enumerate(r):
            col="F" if len(r)==1 else ("L" if idx==0 else "R")
            if isinstance(c,tuple):
                hs=[boxh(n,col) for n in c]; extra=h-(sum(hs)+30*(len(c)-1)); yy=T
                for j,n in enumerate(c):
                    hh=hs[j]+(extra if j==len(c)-1 else 0)
                    draw(n,col,yy,hh); yy+=hh+30
            else: draw(c,col,T,h)
        T+=h+gap
    for ab in spec.get("abs",[]):
        t,l,w,items=ab; render(pg,items,t,l,l+w)
    dels=list(deletes_extra)
    for k,b in tmpl.items():
        if k not in used_tmpl:
            for role in ("box","pill","circ"): 
                if b[role]: dels.append(b[role])
            for role in ("num","title","instr"):
                if b[role]: pg.pool.append(b[role])
    # refleksi
    if refl:
        R=roles["refl"]; els=R.get("els",[])
        strip=[e for e in els if e["type"]=="shape" and e["w"]>600]
        star=[e for e in els if e["type"]=="rect"]
        lab=[e for e in els if e["type"]=="text" and "REFLEKSI" in (e["txt"] or "")]
        white=[e for e in els if e["type"]=="shape" and e["txt"]=="#ffffff"]
        ins=[e for e in els if e["type"]=="text" and e["left"]<200 and "REFLEKSI" not in (e["txt"] or "")]
        keep={x["loc"] for x in strip+star+lab+white[:1]+ins[:1]}
        for e in els:
            if e["loc"] in keep: continue
            if e["type"]=="text": pg.pool.append(e["loc"])
            else: dels.append(e["loc"])
        st=strip_top
        if strip: pg.ops+=[{"type":"resize_element","locator_id":strip[0]["loc"],"width":638.11,"height":round(strip_h,2)},{"type":"position_element","locator_id":strip[0]["loc"],"top":round(st,2),"left":76.69}]
        if star: pg.ops.append({"type":"position_element","locator_id":star[0]["loc"],"top":round(st+(strip_h-53.45)/2,2),"left":50.79})
        if lab: pg.ops.append({"type":"position_element","locator_id":lab[0]["loc"],"top":round(st+7,2),"left":114.05})
        # white box
        if white: pg.ops+=[{"type":"resize_element","locator_id":white[0]["loc"],"width":473.46,"height":round(strip_h-10,2)},{"type":"position_element","locator_id":white[0]["loc"],"top":round(st+5,2),"left":234.05}]
        else: pg.shape(st+5,234.05,473.46,strip_h-10,fill="#ffffff",r=20)
        it=refl.get("instr","Lengkapi kalimat berikut.")
        pg.text(it,st+27,114.05,112,lh=1.2,loc=ins[0]["loc"] if ins else None,front=True)
        pg.force_front=True
        render(pg,refl["items"],st+12,245.3,245.3+rW)
        pg.force_front=False
    ops=pg.finish(dels)
    info.update(texts_used=len(pg.used),added=pg.added,pool_left=len(pg.pool),ops=len(ops))
    return ops,info
