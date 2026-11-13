import json as j,os,urllib.request as u
W=os.environ['MAKEFUN_ENV_URL']
def P(p,b):
 q=u.Request(W+p,data=j.dumps(b).encode(),headers={'content-type':'application/json'})
 try:
  with u.urlopen(q)as r:return j.load(r)
 except:raise
V=[100,320,330,500,900,9999]
T="AAAAKKKKCCEGBBCFAAAEB@?ABCC=AAAA79;;9=AA;ACD;BDE;ADE;BCD9=AB79;;=????AAA?ABC?BBC?ACC?CCC?BAA=???AAAABCCC@AAA@AAA@AAA@AAA@AAAAAAB=??@?AAA?ABB@ABBAABB?BBB?ABA=??@;997;997;997;997=;;9?===EEAAEGCA"
KN=(-33,-31,-18,-14,14,18,31,33)
BD=(-17,-15,15,17)
RD=(-16,-1,1,16)
KI=BD+RD
B=[0]*128;K=[0,0];C=0;E=-1;N=0;BUD=16e3
class AB(Exception):pass
def F(f):
 global C,E;B[:]=[0]*128
 p=f.split();r=c=0
 for ch in p[0]:
  if ch=='/':r+=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   v='PNBRQK'.index(ch.upper())+1
   if ch.islower():v=-v
   B[r*16+c]=v
   if abs(v)==6:K[v>0]=r*16+c
   c+=1
 C=sum(1<<'KQkq'.find(ch)for ch in p[2]if ch in'KQkq')
 q=p[3];E=(8-int(q[1]))*16+ord(q[0])-97 if q!='-' else -1
def A(s,c):
 for O,v in(((15*c,17*c),1),(KN,2),(KI,6)):
  for o in O:
   x=s+o
   if not x&0x88 and B[x]==v*c:return 1
 for d in BD+RD:
  w=3 if d in BD else 4;x=s+d
  while not x&0x88 and not B[x]:x+=d
  if not x&0x88 and B[x] in(5*c,w*c):return 1
 return 0
def G(c):
 ms=[]
 for s in range(128):
  if s&0x88 or (p:=B[s])*c<=0:continue
  v=abs(p);r=s>>4
  if v==1:
   d=-16*c;t=s+d;pr=5 if r==(1,6)[c<0] else 0
   if not t&0x88 and not B[t]:
    ms.append((s,t,pr))
    if r==(6,1)[c<0] and not B[s+2*d]:ms.append((s,s+2*d,0))
   for df in(-1,1):
    t=s+d+df
    if not t&0x88 and (B[t]*c<0 or t==E):ms.append((s,t,pr))
  elif v==2 or v==6:
   for o in KN if v==2 else KI:
    t=s+o
    if not t&0x88 and B[t]*c<=0:ms.append((s,t,0))
  else:
   for d in BD if v==3 else RD if v==4 else BD+RD:
    t=s+d
    while not t&0x88:
     if not B[t]:ms.append((s,t,0))
     elif B[t]*c<0:ms.append((s,t,0));break
     else:break
     t+=d
 b0=(1,4)[c<0];kk=(116,4)[c<0]
 for k,sg in((b0,1),(b0*2,-1)):
  rk=kk+3 if sg>0 else kk-4;a=kk+sg;b=kk+2*sg
  if C&k and B[rk]==4*c and not B[a] and not A(a,-c) and not B[b] and not A(b,-c) and not A(kk,-c) and (sg>0 or not B[kk-3]):ms.append((kk,b,0))
 o=[]
 for m in ms:
  u=M(m)
  if not A(K[c>0],-c):o.append(m)
  U(m,u)
 return o
def M(m):
 global C,E
 f,t,pr=m;p=B[f];cap=B[t];ec=rf=rt=0;oc,oe=C,E
 if abs(p)==1 and t==E and not cap:
  e=(f>>4)*16+(t&7);ec=B[e];B[e]=0
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1) if t>f else (f-4,f-1);B[rt]=B[rf];B[rf]=0
 B[t]=pr*p if pr else p;B[f]=0
 if abs(p)==6:K[p>0]=t;C&=~(3 if p>0 else 12)
 for q,n in((112,2),(119,1),(0,8),(7,4)):
  if (f==q or t==q) and (abs(p)==4 or abs(cap)==4):C&=~n
 E=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
 return f,t,pr,cap,ec,rf,rt,oc,oe
def U(m,u):
 global C,E
 f,t,pr,cap,ec,rf,rt,oc,oe=u;p=B[t]
 B[f]=p//5 if pr else p;B[t]=cap
 if ec:B[(f>>4)*16+(t&7)]=ec
 if rt:B[rf]=B[rt];B[rt]=0
 if not pr and abs(p)==6:K[p>0]=f
 C,E=oc,oe
def E_():
 s=0
 for i,p in enumerate(B):
  if p:
   a=abs(p);r=i>>4;f=i&7;f=f if f<4 else 7-f;x=(r if p>0 else 7-r)*4+f;s+=(V[a-1]+5*(ord(T[(a-1)*32+x])-65))*p//a
 return s
def S(d,a,be,c,pl):
 global N;N+=1
 if N>BUD:raise AB
 if d<=0:
  a=max(a,c*E_())
  if a>=be:return a
  ms=[m for m in G(c) if B[m[1]] or (abs(B[m[0]])==1 and m[1]==E)]
 else:
  ms=G(c)
  if not ms:return -99999+pl if A(K[c>0],-c) else 0
 ms.sort(key=lambda m:-((abs(B[m[1]])+1)*10-abs(B[m[0]])))
 for m in ms:
  u=M(m)
  try:s=-S(d-1,-be,-a,-c,pl+1)
  except AB:U(m,u);raise
  U(m,u)
  if s>=be:return s
  if s>a:a=s
 return a
def R(c):
 global N
 ms=G(c)
 if len(ms)==1:return ms[0]
 bm=ms[0]
 for d in range(9):
  N=0
  try:
   ms.sort(key=lambda m:m!=bm);a=-99999;cur=bm
   for m in ms:
    u=M(m)
    try:s=-S(d-1,-99999,-a,-c,1)
    except AB:U(m,u);raise
    U(m,u)
    if s>a:a=s;cur=m
   bm=cur
  except AB:break
 return bm
def Y(m):return ''.join(chr(97+(x&7))+str(8-(x>>4))for x in m[:2])+('q' if m[2] else '')
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  F(g['fen']);g=P('/move',{'game':g['game'],'move':Y(R((-1,1)[g['colour']=='white']))})
