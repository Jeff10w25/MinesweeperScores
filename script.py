import shutil
import os
import re
import settings

source = os.path.join(settings.SOURCE, "replays/")      # ~/Arbiter/replays/
source2 = settings.SOURCE                               # ~/Arbiter/
dest = settings.DEST

def beg_sorter(filepath, destination, dir1, board_type):    
    # beg_sorter(dest, "beg/untyped/", "Beg") beg_untyped
    dest_beg = os.path.join(destination, dir1)
            
    if re.search("%s_([10-99][0-9][.])" % (board_type), filepath):
        shutil.copy(filepath, os.path.join(dest_beg, "10+/"))
    else: 
        for t in range(10):
            if re.search("%s_(%s[.])" % (board_type, t), filepath):
                shutil.copy(filepath, os.path.join(dest_beg, "%s/" % (t)))
                
def int_sorter(filepath, destination, dir1, board_type):    
    # int_sorter(dest, "int/FL/", "Int_FL") int_fl
    dest_int = os.path.join(destination, dir1)
            
    if re.search("Int_([0-9][.])", filepath):
        shutil.copy(filepath, os.path.join(dest_int, "0-9/"))
    elif re.search("Int_([5-99][0-9][.])", filepath):
        shutil.copy(filepath, os.path.join(dest_int, "50+/"))
    else: 
        for t in range(1,5):
            if re.search("%s_(%s[0-9][.])" % (board_type, t), filepath):
                shutil.copy(filepath, os.path.join(dest_int, "%s0-%s9/" % (t, t)))
                
def exp_sorter(filepath, destination, dir1, board_type):    
    # exp_sorter(dest, "exp/NF/", "Exp_NF") exp_nf
    dest_exp = os.path.join(destination, dir1)    
            
    if re.search("Exp_([1-9][0-9][0-9][.])", filepath):
        shutil.copy(filepath, os.path.join(dest_exp, "100+/"))
    else: 
        for t in range(3,10):
            if re.search("%s_(%s[0-9][.])" % (board_type, t), filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "%s0-%s9/" % (t, t)))
                                    
# CSV
# for filename in os.listdir(source2):
#     filepath = os.path.join(source2, filename)
#     if os.path.isfile(filepath):
#         if re.search("stats_csv.csv", filepath):
#             shutil.copy(filepath, dest)

# Replays
for filename in os.listdir(source):
    filepath = os.path.join(source, filename)
    if os.path.isfile(filepath):
        
        # Beginner
        if re.search("Beg_([0-999])", filepath):
            beg_sorter(filepath, dest, "beg/untyped/", "Beg")
                
        elif re.search("Beg_NF", filepath):
            beg_sorter(filepath, dest, "beg/NF/", "Beg_NF")

        elif re.search("Beg_FL", filepath):
            beg_sorter(filepath, dest, "beg/FL/", "Beg_FL")
        
        # Intermediate
        elif re.search("Int_([0-999])", filepath):
            int_sorter(filepath, dest, "int/untyped/", "Int")    
                
        elif re.search("Int_NF", filepath):
            int_sorter(filepath, dest, "int/NF/", "Int_NF") 
        
        elif re.search("Int_FL", filepath):
            int_sorter(filepath, dest, "int/FL/", "Int_FL") 
                
        # Expert
        elif re.search("Exp_([0-999])", filepath):
            exp_sorter(filepath, dest, "exp/untyped/", "Exp")
                
        elif re.search("Exp_NF", filepath):
            exp_sorter(filepath, dest, "exp/NF/", "Exp_NF")  
        
        elif re.search("Exp_FL", filepath):
            exp_sorter(filepath, dest, "exp/FL/", "Exp_FL") 
                