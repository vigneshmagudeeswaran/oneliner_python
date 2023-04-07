#popular quick sort algorithm

q= lambda l : q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

print(q([3,1,42,32]))

employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'frank': 88123,
             'Eve': 93121}

top_earners =[]

for key, val in employees.items():
    if val >= 100000: 
        top_earners.append((key,val))
print(top_earners)