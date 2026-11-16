import json as j,os,urllib.request as u
U='PNBRQK';Y=39e3;L=18300;Z=(' '*9+'\n')*2
D=dict(zip(U,[(-10,-20,-11,-9),(-19,-8,12,21,19,8,-12,-21),B:=(-9,11,9,-11),R:=(-10,1,10,-1),R+B,R+B]))
A=dict(zip(U+'.',(100,320,330,500,900,3e4,100)))
T=b'KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLGIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJECCAECCAECCAECCAGEECIGGGOOKKOQMK'
P={p:[A[p]+T[z*32+x//10*4-9+min(x%10,9-x%10)]*5-375 if x//20*(x%10%9)else 0 for x in range(99)]for z,p in enumerate(U)}
P['.']=[0]*120;N=[0,0];O={};E={};K={};I={}
X=StopIteration
H={223:(73,52,''),409:(54,75,'')}
r=lambda p:(p[0][::-1].swapcase(),-p[1],*p[3:1:-1],*(x and 119-x for x in p[4:]))
def G(p):
 b=p[0];m=[]
 for i,x in enumerate(b):
  for d in D.get(x,()):
   j=i+d
   while(q:=b[j])in'.pnbrqk':
    if x=='P':
     if'.'<q or j==p[4]or abs(j-p[5])<2 if d%10 else q=='.'and(d+20 or i>80 and b[i-10]in'.'):
      m+=[(i,j,z)for z in'NBRQ'*(j<29)or['']]
     break
    m+=[(i,j,'')]
    if x in'NK'or'.'<q:break
    if i in(91,98)and p[2][i>91]and b[j+(u:=1-2*(i>91))]=='K':m+=[(j+u,j-u,'')]
    j+=d
 return m
def V(p,m):
 b=p[0];c=b.count;i,z,t=m;x,q=b[i],b[z]
 return P[x][z]-P[x][i]+P[q.upper()][119-z]+(abs(z-p[5])<2)*P['K'][119-z]+(x=='K'and abs(i-z)==2)*(P['R'][(i+z)//2]-P['R'][91+7*(z>i)])+P[t or'P'][z]-P['P'][z]+(x=='P'and z==p[4])*P['P'][109-z]+25*((t=='B'and c('B')==1)+(q=='b'and c('b')==2))
def M(p,m):
 b,s,w,c,e,k=p;i,z,q=m;x=b[i];b=list(b);b[z]=q or x;b[i]='.'
 if x=='P'and z==e:b[z+10]='.'
 e=(i-10)*(x=='P'and i-z>19);k=(i+z)//2*(x=='K'and abs(z-i)==2)
 if k:b[91+7*(z>i)]='.';b[k]='R'
 return r((''.join(b),s+V(p,m),tuple(w[t]*(x!='K')*(i!=91+7*t)for t in(0,1)),(c[0]*(z!=28),c[1]*(z!=21)),e,k))
C=lambda p:any(p[0][m[1]]=='k'for m in G(p))
k=lambda p:p[:1]+p[2:5]
def B(p,g,d,t,y,x,j):
 N[0]+=1
 if N[0]>55e3:raise X
 b,s=p[:2]
 if s<=-L:return-Y
 h=C(r(p))
 if h*d*(x<8):d+=1;x+=1
 u=N[1]
 if I.get(k(p),0)>2:N[1]+=1;return 25
 n=p,d,x
 if d>t and n in O:
  v,f=O[n]
  if(v>=g)==f:return v
 l=G(p);c=lambda m:'.'<b[m[1]]or m[1]==p[4]
 if h*t:l=[m for m in l if b[m[0]]!='K'or abs(m[0]-m[1])!=2]
 o=-Y;a=0
 if d+h<1:
  o=s+len(l)
  if j>31or s>=g:return o
  l=[m for m in l if c(m)or m[2]]
 q=K.get(y,());i=E.get(p)
 for m in sorted(l,key=lambda m:-1e9 if m==i else-5e4-10*A[b[m[1]].upper()]+A[b[m[0]]]if c(m)else-4e4-A[m[2]]if m[2]else-3e4+(m!=q[0])if m in q else-(V(p,m)//8)):
  z=M(p,m);f=k(z);I[f]=I.get(f,0)+1
  try:v=-B(z,1-g,d and d-1,0,y+1,x,(j+1)*(d<1))
  finally:I[f]-=1
  a|=v>-Y
  if v>o:
   o=v
   if t or d*(o>=g):E[p]=m
   if o>=g:
    if(c(m)or m[2]or m in q)==0:K[y]=m,*q[:1]
    break
 if(d+h)*(1-a):o=-(L+d)*h
 if d>t and N[1]==u:O[n]=o,o>=g
 return o
def R(p):
 bs=g=0;N[:]=0,0
 for d in O,E,K:d.clear()
 for d in range(99):
  try:
   l,h=1-Y,Y
   while l<h:s=B(p,g,d,1,0,0,0);l,h=((s,h),(l,s))[s<g];g=(l+h+1)//2
   if p in E:bs=E[p];g=l
  except X:break
 return bs or next((m for m in G(p)if C(M(p,m))==0),0)
q=lambda x:x>'-'and 4+ord(x[0])-10*int(x[1])
def F(f):
 u,v,c,e,*_=f.split();b=Z+' '+''.join('.'*int(c)if'0'<c<'9'else c for c in u.replace('/','\n '))+'\n'+Z
 d=b.count;s=sum(-P[x.upper()][119-i]if x>'a'else P.get(x,P['.'])[i]for i,x in enumerate(b))+25*((d('B')>1)-(d('b')>1))
 p=b,s,('Q'in c,'K'in c),('k'in c,'q'in c),q(e),0;return[r(p),p][v>'c']
Q=lambda p,b:j.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,j.dumps(b).encode()))
s='status'
while(g:=Q('/game',{}))[s]>'e':
 while g[s]>'x':
  p=F('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -');I={k(p):1};S=lambda x:abs(n%2*119-q(x))
  for n,x in enumerate(g['moves']):p=M(p,(S(x[:2]),S(x[2:4]),x[4:].upper()));I[k(p)]=I.get(k(p),0)+1
  a=g['game'];v=g['moves'];l=len(v);m=H.get(a*100+l);m=m if m in G(p)else R(p)
  g=Q('/move',{'game':a,'move':''.join(chr(96+x%10)+str(10-x//10)for x in(m[:2],(119-m[0],119-m[1]))[l%2])+m[2].lower()})
