import shutil
import os
import re
import settings

source = settings.SOURCE
dest = settings.DEST

for filename in os.listdir(source):
    filepath = os.path.join(source, filename)
    if os.path.isfile(filepath):
        
        # Beginner
        if re.search("Beg_([0-999])", filepath):
            dest_beg = os.path.join(dest, "beg/untyped/")
            
            if re.search("Beg_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_beg, "10+/"))
            else: 
                for t in range(10):
                    if re.search("Beg_(%s[.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_beg, "%s/" % (t)))
                
        elif re.search("Beg_NF", filepath):
            dest_beg_nf = os.path.join(dest, "beg/NF/")
            
            if re.search("Beg_NF_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_beg_nf, "10+/"))
            else: 
                for t in range(10):
                    if re.search("Beg_NF_(%s[.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_beg_nf, "%s/" % (t)))
        
        elif re.search("Beg_FL", filepath):
            dest_beg_fl = os.path.join(dest, "beg/FL/")
            
            if re.search("Beg_FL_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_beg_fl, "10+/"))
            else: 
                for t in range(10):
                    if re.search("Beg_FL_(%s[.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_beg_fl, "%s/" % (t)))
        
        # Intermediate
        elif re.search("Int_([0-999])", filepath):
            dest_int = os.path.join(dest, "int/untyped/")
            
            if re.search("Int_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "0-9/"))
            elif re.search("Int_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "50+/"))
            else: 
                for t in range(1,5):
                    if re.search("Int_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_int, "%s0-%s9/" % (t, t)))     
                
        elif re.search("Int_NF", filepath):
            dest_int_nf = os.path.join(dest, "int/NF/")
            
            if re.search("Int_NF_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "0-9/"))     
            elif re.search("Int_NF_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "50+/"))
            else: 
                for t in range(1,5):
                    if re.search("Int_NF_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_int_nf, "%s0-%s9/" % (t, t)))
        
        elif re.search("Int_FL", filepath):
            dest_int_fl = os.path.join(dest, "int/FL/")
            
            if re.search("Int_FL_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "0-9/"))     
            elif re.search("Int_FL_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "50+/"))
            else: 
                for t in range(1,5):
                    if re.search("Int_FL_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_int_fl, "%s0-%s9/" % (t, t)))
                
        
        # Expert
        elif re.search("Exp_([0-999])", filepath):
            dest_exp = os.path.join(dest, "exp/untyped/")    
            
            if re.search("Exp_([1-9][0-9][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "100+/"))
            else: 
                for t in range(3,10):
                    if re.search("Exp_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_exp, "%s0-%s9/" % (t, t)))
                
        elif re.search("Exp_NF", filepath):
            dest_exp_nf = os.path.join(dest, "exp/NF/")       
            if re.search("Exp_NF_([1-9][0-9][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "100+/"))
            else: 
                for t in range(3,10):
                    if re.search("Exp_NF_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_exp_nf, "%s0-%s9/" % (t, t)))  
        
        elif re.search("Exp_FL", filepath):
            dest_exp_fl = os.path.join(dest, "exp/FL/")      
            if re.search("Exp_FL_([1-9][0-9][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "100+/"))
            else: 
                for t in range(3,10):
                    if re.search("Exp_FL_(%s[0-9][.])" % (t), filepath):
                        shutil.copy(filepath, os.path.join(dest_exp_fl, "%s0-%s9/" % (t, t))) 
                