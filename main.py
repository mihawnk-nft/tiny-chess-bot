import json as j,os,urllib.request as u
B=(-9,11,9,-11);R=(-10,1,10,-1);U='PNBRQK';Y=39e3;L=18300;Z='         \n'*2
D=dict(zip(U,[(-10,-20,-11,-9),(-19,-8,12,21,19,8,-12,-21),B,R,R+B,R+B]))
A=dict(zip(U+'.',(100,320,330,500,900,3e4,100)))
T='KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLGIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJECCAECCAECCAECCAGEECIGGGOOKKOQMK'
P={p:[A[p]+ord(T[z*32+x//10*4-9+min(x%10,9-x%10)])*5-375 if 19<x and x%10%9 else 0 for x in range(99)]for z,p in enumerate(U)}
P['.']=[0]*120;N=[0,0];O={};E={};K={};I={}
X=StopIteration
r=lambda p:(p[0][::-1].swapcase(),-p[1],*p[3:1:-1],*(x and 119-x for x in p[4:]))
def G(p):
 b=p[0];ms=[]
 for i,x in enumerate(b):
  for d in D.get(x,()):
   j=i+d
   while(q:=b[j])in'.pnbrqk':
    if x=='P':
     if('.'<q or j==p[4]or abs(j-p[5])<2)if d%10 else q=='.'and(d+20 or i>80 and b[i-10]in'.'):
      for z in'NBRQ'*(j<29)or['']:ms.append((i,j,z))
     break
    ms.append((i,j,''))
    if x in'NK'or'.'<q:break
    if i in(91,98)and p[2][i>91]and b[j+(u:=1-2*(i>91))]=='K':ms.append((j+u,j-u,''))
    j+=d
 return ms
def V(p,m):
 b=p[0];i,z,pr=m;x,q=b[i],b[z]
 return P[x][z]-P[x][i]+P[q.upper()][119-z]+(abs(z-p[5])<2)*P['K'][119-z]+(x=='K'and abs(i-z)==2)*(P['R'][(i+z)//2]-P['R'][91+7*(z>i)])+P[pr or 'P'][z]-P['P'][z]+(x=='P'and z==p[4])*P['P'][109-z]+25*((pr=='B'and b.count('B')==1)+(q=='b'and b.count('b')==2))
def M(p,m):
 b,s,w,c,e,k=p;i,z,pr=m;x=b[i];s+=V(p,m);b=list(b);b[z]=pr or x;b[i]='.'
 if x=='P'and z==e:b[z+10]='.'
 e=(i-10)*(x=='P'and i-z>19);k=(i+z)//2*(x=='K'and abs(z-i)==2)
 if k:b[91+7*(z>i)]='.';b[k]='R'
 return r((''.join(b),s,tuple(w[t]*(x!='K')*(i!=91+7*t)for t in(0,1)),(c[0]*(z!=28),c[1]*(z!=21)),e,k))
C=lambda p:any(p[0][m[1]]=='k'for m in G(p))
k=lambda p:p[:1]+p[2:5]
def B(p,g,d,rt,y,x,qd):
 N[0]+=1
 if N[0]>55e3:raise X
 b,s,w,c,e,_=p
 if s<=-L:return-Y
 ck=C(r(p))
 if ck*d*(x<8):d+=1;x+=1
 rh=N[1]
 if I.get(k(p),0)>2:N[1]+=1;return 0
 tk=(p,d,x)
 if d>rt and tk in O:
  v,f=O[tk]
  if v>=g if f else v<g:return v
 ms=G(p);c=lambda m:'.'<b[m[1]]or m[1]==e
 if ck*rt:ms=[m for m in ms if b[m[0]]!='K'or abs(m[0]-m[1])!=2]
 bs=-Y;lv=0
 if d+ck<1:
  if all(C(M(p,m))for m in ms):return 0
  if qd>31 or s>=g:return s
  bs=s;ms=[m for m in ms if c(m)or m[2]]
 ks=K.get(y,());tm=E.get(p)
 for m in sorted(ms,key=lambda m:-1e9 if m==tm else-5e4-10*A[b[m[1]].upper()]+A[b[m[0]]]if c(m)else-4e4-A[m[2]]if m[2]else-3e4+ks.index(m)if m in ks else-(V(p,m)//8)):
  ch=M(p,m);kk=k(ch);I[kk]=I.get(kk,0)+1
  try:sc=-B(ch,1-g,d and d-1,0,y+1,x,(qd+1)*(d<1))
  finally:I[kk]-=1
  lv|=sc>-Y
  if sc>bs:
   bs=sc
   if rt or d*(bs>=g):E[p]=m
   if bs>=g:
    if(c(m)or m[2]or m in ks)==0:K[y]=(m,*ks[:1])
    break
 if(d+ck)*(1-lv):bs=(-L-d)*ck
 if d>rt and N[1]==rh:O[tk]=(bs,bs>=g)
 return bs
def R(p):
 I[k(p)]=I.get(k(p),0)or 1;bs=gs=0;N[:]=[0,0]
 for d in O,E,K:d.clear()
 for d in range(99):
  try:
   l,h=1-Y,Y;g=gs
   while l<h:s=B(p,g,d,1,0,0,0);l,h=((s,h),(l,s))[s<g];g=(l+h+1)//2
   if p in E:bs=E[p];gs=l
  except X:break
 return bs or next((m for m in G(p)if C(M(p,m))==0),None)
q=lambda x:x>'-'and 4+ord(x[0])-10*int(x[1])
def F(f):
 u,v,c,e=f.split()[:4];b=Z+' '+''.join('.'*int(c)if'0'<c<'9'else c for c in u.replace('/','\n '))+'\n'+Z
 s=sum(-P[x.upper()][119-i]if x>'a'else P.get(x,P['.'])[i]for i,x in enumerate(b))+25*((b.count('B')>1)-(b.count('b')>1))
 p=b,s,('Q'in c,'K'in c),('k'in c,'q'in c),q(e),0;return r(p)if v<'c'else p
Q=lambda p,b:j.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL','')+p,j.dumps(b).encode()))
if __name__=='__main__':
 while(g:=Q('/game',{}))['status']!='done':
  while g['status']=='your_move':
   I.clear();p=F('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -');I[k(p)]=1;S=lambda x:119-q(x)if n%2 else q(x)
   for n,x in enumerate(g['moves']):p=M(p,(S(x[:2]),S(x[2:4]),x[4:].upper()));I[k(p)]=I.get(k(p),0)+1
   f=g['fen'];m=R(F(f))
   if' b 'in f:m=(119-m[0],119-m[1],m[2])
   g=Q('/move',{'game':g['game'],'move':''.join(chr(96+x%10)+str(10-x//10)for x in m[:2])+m[2].lower()})
