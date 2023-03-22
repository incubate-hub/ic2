  
# Extract least frequency element 
res = defaultdict(int) 
for ele in test_list: 
   res[ele] += 1 
min_occ = 9999
for ele in res: 
    if min_occ > res[ele]: 
        min_occ = res[ele] 
        tar_ele = ele 
