from mpmath import *
mp.dps=30
# 18B 3b roots
g=lambda z: exp(z)+sin(z)
rts=[findroot(g,z0) for z0 in [-3.1,-6.3,-9.4,-12.5,-15.7,-18.8,-0.0+(-4.7)]]
print('18B3b roots',[nstr(r,8) for r in rts], 'g(0)=',g(0),'g(-pi/2)=',g(-pi/2))
for k in range(4):
    a,b=-pi/2-2*pi*k,-2*pi*k; print(k,g(a)<0,g(b)>0)
print('x>=0 min',min(g(mpf(i)/100) for i in range(0,3000)))
# 18B 4a
for d in [1e-1,1e-2,1e-3]:
    x=pi/2-d; print('4a',(sin(x))**tan(x))
# 18B 4b
V=pi*quad(lambda x:x**2*atan(x),[0,1]); print('4b',V, pi**2/12-pi/6+pi*log(2)/6, quad(lambda x:x**3/(1+x**2),[0,1]), quad(lambda x:x**2*atan(x),[0,1]))
print('4b direct',pi*quad(lambda x:(x*sqrt(atan(x)))**2,[0,1]))
# 18B 6a arc
print('6a',quad(lambda x:sqrt(1+diff(lambda t:sqrt(1-t**2),x)**2),[0,0.5]),pi/6)
print('6b',[log(x)*log(1-x) for x in [mpf('0.9'),mpf('0.999'),1-mpf('1e-9')]])
# 18B 3a signs
f1=lambda x: 3*x**17*(x**3+1)
print('3a',f1(-2)>0,f1(-.5)<0,f1(.5)>0)
# 19A
f=lambda x: exp(-x)/(1-x)
fp=lambda x: x*exp(-x)/(x-1)**2
fpp=lambda x: -(x**2+1)*exp(-x)/(x-1)**3
for x0 in [mpf(-2),mpf('0.3'),mpf(3)]:
    print('19A1',diff(f,x0)-fp(x0),diff(f,x0,2)-fpp(x0))
print('19A2a',[(3**n+49**n+mpf(n)/(n+1))**(mpf(1)/(2*n)) for n in [10,100,1000]])
print('19A3a',[(4/(1+sqrt(9+x)))**(1/sin(x)) for x in [mpf('1e-4'),mpf('-1e-4')]],exp(-mpf(1)/24))
F=lambda x:-exp(-2*tan(x))*(2*tan(x)+1)/4
print('19A3b',diff(F,0.3)-tan(0.3)/(cos(0.3)**2*exp(2*tan(0.3))))
h=lambda x:x*cbrt(x**2-1) if x**2>=1 else -x*cbrt(1-x**2)
print('19A4a',[h(mpf(x)/1000) for x in [0,500,774,775,776,900,1000,3000]], -sqrt(15)/5*cbrt(mpf(2)/5), -(540**(mpf(1)/6))/5)
ff=lambda x:(x-3)**sqrt(x); print('19A4b',ff(4),diff(ff,4))
print('19A5a',[1/(sqrt(2*x-1)-sqrt(2*x-3))/sqrt(x+1) for x in [mpf(10)**4,mpf(10)**8]])
print('19A5b',diff(lambda x:log(x-1)+log(x**2+1)/2,3)-(2*9-3+1)/((3-1)*(10)))
print('19A6a',pi*quad(lambda y:log(1+y)**2,[0,1]),2*pi*(1-log(2))**2, 2*pi*quad(lambda x:x*(2-exp(x)),[0,log(2)]), quad(lambda x:x*exp(x),[0,log(2)]))
print('19A6b',quad(lambda x:x/2,[0,1])+quad(lambda x:1/x-x/2,[1,sqrt(2)]),log(2)/2)
# 17A
print('17A2b',diff(lambda x:tan(x)-4/sqrt(5)*atan(tan(x)/sqrt(5)),0.4)-1/(cos(0.4)**2+4*cos(0.4)**4))
print('17A3a',[cos(x)**(1/(x*sin(x))) for x in [mpf('1e-4')]],exp(-0.5))
print('17A3b',cos(pi*exp(mpf('0.1'))/6), sqrt(3)/2-pi/120)
print('17A4a',[((sqrt(2*x-a)-sqrt(x))/(x**2-a**2)) for a in [mpf(1)/2] for x in [a+mpf('1e-6')]],sqrt(0.5))
print('17A4b',quad(lambda x:exp(x)*sin(pi*x),[0,1]),pi*(e+1)/(1+pi**2))
g5=lambda x:x*cbrt((3*x-12)**2)
print('17A5a',[g5(mpf(v)) for v in [0,2.4,4,6]],[g5(mpf(x)/10) for x in range(0,61)].__len__(), min(g5(mpf(x)/100) for x in range(0,601)),max(g5(mpf(x)/100) for x in range(0,601)))
print('17A5b',diff(lambda x:x+log(x)-3.5*atan((x+1)/2),2)-(8+12+5)/(2*(4+4+5)))
print('17A6a',sqrt(mpf('1.05')),1.0246875, abs(sqrt(mpf('1.05'))-mpf('1.0246875')), mpf('0.05')**3/16, 1/mpf(128000))
print('17A6b',quad(lambda x:sqrt(32*x)-x**3,[0,2]),mpf(20)/3)
# 17B
print('17B 3b',2*pi*quad(lambda x:x*(8-x**3),[1,2]),58*pi/5)
print('17B 3b alt (washers y in [2,9])', pi*quad(lambda y: (cbrt(y-1))**2-1,[2,9]),)
print('17B 6b',diff(lambda x:2*sqrt(x+1)*log(x+1)-4*sqrt(x+1),2)-log(3)/sqrt(3))
print('17B 4b',quad(lambda x:(x/4+1)-sqrt(x) if x>0 else x/4+1,[-4,0,4]))
print('17B 6a',[ (exp(a*x)-1)**2/x**2 for a in [mpf(2)] for x in [-mpf('1e-6')]], 4+exp(-4/mpf('1e-3')))
# 21B / 24A
print('21B4a',[log(cos(x))/log(cos(4*x)) for x in [mpf('1e-3')]])
print('21B4b',2*pi*(quad(lambda x:(4-x)*x**2,[0,2])+quad(lambda x:(4-x)*(8-2*x),[2,4])),24*pi)
print('21B3a',2*sin(3)**2-4, 2*sin(-3)**2+5*cbrt(0)+4)
print('21B3b',diff(lambda t:log(abs((t-3)/(t-1)))/2,4)-1/((4-1)*(4-3)))
fx=lambda x:exp(x)/x**2
print('24A1',fx(2),[diff(fx,v,2)>0 for v in [-3,-.1,.1,1,2,5]],diff(fx,2),[fx(v) for v in [-50,-100]])
print('24AB 6b',[x**4/quad(lambda t:t*cos(t**2),[0,x**2]) for x in [mpf('0.1'),mpf('0.01')]])
