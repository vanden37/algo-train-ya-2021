mat  = list(map(int, input().split()))
            
raw_mat = mat[0]
one_preuse_mat = mat[1]
one_use_mat = mat[2]


num_preuse = 0
dets_all = 0
dets_weight = 0
not_used_raw = 0

if raw_mat > 0 and one_preuse_mat > 0 and one_use_mat >0:

    # колво деталей из одной заготовки
    dets_from_one_preuse = one_preuse_mat // one_use_mat
    
    # остатки от веса от одной заготовки 
    not_used_one_preuse_one_use = one_preuse_mat - dets_from_one_preuse * one_use_mat
    
    if one_preuse_mat > raw_mat or one_use_mat > one_preuse_mat:
        print(0)
    else:
    
        while raw_mat >= one_preuse_mat:
        
            # колво заготовок
            num_preuse = raw_mat // one_preuse_mat
        
            # остатки материала до заготовок
            not_used_raw = raw_mat - num_preuse * one_preuse_mat
        
            # колво деталей из всех заготовок
            dets_all += dets_from_one_preuse * num_preuse
        
            # остатки веса от готовых деталей
            not_used_for_det_raw = not_used_one_preuse_one_use * num_preuse
        
            raw_mat = not_used_raw + not_used_for_det_raw
        print(int(dets_all))  
else:
    print(0)