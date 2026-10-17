from mpmath import *
mp.dps=20
chk=lambda n,v,a,t=1e-3: print(('OK ' if abs(v-a)<=t else 'BAD'),n,nstr(v,8),a)
# 24B-A
chk('24B-A 5a',quad(lambda x:(x*x+2*x)*cos(2*x),[0,pi/4]),0.3438)
chk('24B-A 6a g1',e-4,-1.2817); chk('24B-A 6a g1.5',exp(1.5)-2/3-3,0.815)
chk('24B-A 1 fmax',(-2**(1/3.))-1/2**(2/3.),-1.8899)
# 24A-B
chk('24A-B 1 f(-2)',4*exp(-2),0.5413)
chk('24A-B 3b',quad(lambda x:(4-sqrt(x))**2-(x-2)**2,[2,4]),7.7516)
# shell check of official
chk('24A-B 3b shell',2*quad(lambda y:((4-y)**2-2)*y,[2,4-sqrt(2)])+2*quad(lambda y:y*y,[0,2]),7.7516)
chk('24A-B 4b',quad(lambda x:1.5-.5*x,[-1,3])-quad(lambda x:sqrt(2-2*x),[-1,1]),1.3333)
chk('24A-B 5a',quad(lambda x:log(x)/(x*(log(x)**2+1)),[1,e]),0.3466)
chk('24A-B 6a f16',2**4+atan(32)-5,12.5396)
chk('24A-B a2',sqrt(24),4.899)
# limit numerics
chk('24A-B 3a',(((1e6)**2+5e6-2)/((1e6)**2+3e6-2))**1e6,7.3891,1e-2)
# 24A-A
chk('24A-A 3b def',quad(lambda x:sin(2*x)/(3+cos(2*x)**2),[0,pi/4]),0.1511)
chk('24A-A 4a y(-3)',cbrt(9)*exp(3),41.7796,0.1)
chk('24A-A 4a y2/3',(2/3.)**(2/3.)*exp(-2/3.),0.3918)
chk('24A-A 4b',quad(atan,[0,1]),0.4388); chk('24A-A 4b V',pi*quad(atan,[0,1]),1.3786)
chk('24A-A 6b',quad(lambda x:x-2,[2,3])-quad(lambda x:sqrt(2*x-5),[2.5,3]),0.1667)
chk('24A-A a3',6/(5-6/(5-1.)),1.7143)
chk('24A-A 5a',quad(lambda x:sin(x*x),[0,sqrt(1e-4)])/(1e-4)**1.5,0.3333,1e-3)
# 23B-B
chk('23B-B 2a',quad(lambda x:1/(2+cos(x)),[0,pi/2]),0.6046)
chk('23B-B 2a coef',2/sqrt(3),1.1547)
chk('23B-B 5b',quad(lambda x:(exp(-x)-exp(x))/(exp(-x)+exp(x)),[0,1]),-0.4338)
chk('23B-B 6a',quad(lambda x:sqrt(1+cot(x)**2),[pi/3,pi/2]),0.5493)
chk('23B-B 4b shell',2*pi*quad(lambda x:x*(2*x-x*x),[0,2]),8.3776)
chk('23B-B 4a g1/2',.25/.75**1.5,0.3849); chk('23B-B 4a f3/5',1/sqrt(1-.36)-1,0.25)
chk('23B-B 3a',(1e-3)**4/quad(lambda t:log(1+3*t),[0,(1e-3)**2]),0.6667,1e-3)
chk('23B-B 5a',log(1+1/1e6)/sin(3/1e6),0.3333)
chk('23B-B f(1)',atan(1)+2-2,0.7854)
# 24A-A Q1 f'' sign: sample
f2=lambda x: exp(x)*(x*x-4*x+6)/x**4
print('24A-A Q1 f2 sample', [nstr(f2(v),4) for v in (-5,-1,-.1,.1,1,3,10)], 'diff check', nstr(diff(lambda x:exp(x)/x**2,-2,2)-f2(-2),5))
