"""
So this is a script for showing todays prime number. Started 21. September 2019. For some reason. Please know that this is a inside joke so dont expect understanding anything. 
"""

from datetime import date
f_date = date(2019, 9, 21)
l_date = date.today()
f = []
n_days = f_date - l_date
m_days = n_days.days
m_days = m_days - (m_days*2)

def primes(goal):
    global f
    global todayprime
    amount = 0
    D = {}
    q = 2  # first integer to test for primality.
    while amount < goal:
        if q not in D:
                # not marked composite, must be prime  
                #first multiple of q not already marked
            D[q * q] = [q]
            amount += 1
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
                  # no longer need D[q], free memory
            del D[q]
        q += 1
    todayprime = q -1

def prime():
  global todayprime
  primes(m_days)

