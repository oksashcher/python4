#checked_nums_list = []
#for i in num_list3:
#    if num_list3.count(i) > 1 and i not in checked_nums_list:
#        checked_nums_list.append(i)
#        print(i)




n = int( input( 'n = ' ) )
lis = [ int(x) for x in input( '-> ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max( ma, lis[i] + lis[i+1] + lis[i+2] )
print(ma)
