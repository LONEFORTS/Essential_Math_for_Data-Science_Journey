#Helloworld.12:07am
#date.22-July-2026_Wednesday 

#Helloworld it's 12.08am energetic and this program and information is about the euler's number in math and python. 

#WEll...Euler's Number can be defined as or it is a very special number much like 'pi', and it's valu is approximately 2.71828
#and it is rperesented as "e". 

#here's how i like to discover about THe eule'rs number ffor example say you loan 100$ to somebody with 20% interest anually, typically interest will be compunded monthly. so the interest each month would be i think .... .20/12= .01666...the 
#How much will be the loan balance after two years? to keep it simple, lets's assume the loan does ot require any payments  right now and not any  payment has done yet.

#there is formula also it is: 
# A = p*(1+r/n)^nt 

#here the p = inverstment, and a = balance, and n is showing the number of month in the year and t = time span. 


#here is the example for it: 

from math import exp 
p=100 
r=.20
n=12 
t=2.0 
a=p*(1+r/n)**n*t
print(a)