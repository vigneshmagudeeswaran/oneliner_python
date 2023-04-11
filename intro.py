# popular quick sort algorithm

def q(l): return q([x for x in l[1:] if x <= l[0]]) + \
    [l[0]] + q([x for x in l if x > l[0]]) if l else []


print(q([3, 1, 42, 32]))

# list comprehension
employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'frank': 88123,
             'Eve': 93121}

top_earners = []

for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val))
print(top_earners)

top_earners1 = [(key, value)
                for key, value in employees.items() if value >= 10000]
print(top_earners)

# reading file and adding
filename = 'intro.py'
f = open(filename)
lines = []
for line in f:
    print(line.strip())
    lines.append(line.strip())

print(lines)

print([line.strip() for line in open('intro.py')])

txt = ['last month my manager',
       'removed my admin access  anonymous now I am doing some installation.',
       'for mach1ml project anonymous so i need admin access again.']

# map function and ternary operator
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
print(mark)


letters_amazon = '''
we spent several years building our own database engine, Amazon Aurora, 
a fully-managed MySQL and PostgreSQL-compatible service with the
same or better durability and availability as the commercial engines, 
but at one-tenth of the cost. We were not surprised when this worked.
'''

find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1

print(find(letters_amazon,'SQL'))