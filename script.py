import shutil
import os
import re

source = 'C:/Users/66802/Desktop/Arbiter reboot/replays/'
dest = 'C:/Users/66802/REPO/MinesweeperScores/'

for filename in os.listdir(source):
    filepath = os.path.join(source, filename)
    if os.path.isfile(filepath):
        
        """Intermediate"""
        if re.search("Int_([0-999])", filepath):
            dest_int = os.path.join(dest, "int/untyped/")
            if re.search("Int_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "0-9/"))
            elif re.search("Int_(1[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "10-19/"))
            elif re.search("Int_(2[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "20-29/"))
            elif re.search("Int_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "30-39/"))
            elif re.search("Int_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "40-49/"))     
            elif re.search("Int_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int, "50+/"))
                
        elif re.search("Int_NF", filepath):
            dest_int_nf = os.path.join(dest, "int/NF/")
            if re.search("Int_NF_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "0-9/"))
            elif re.search("Int_NF_(1[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "10-19/"))
            elif re.search("Int_NF_(2[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "20-29/"))
            elif re.search("Int_NF_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "30-39/"))
            elif re.search("Int_NF_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "40-49/"))     
            elif re.search("Int_NF_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_nf, "50+/"))
        
        elif re.search("Int_FL", filepath):
            dest_int_fl = os.path.join(dest, "int/FL/")
            if re.search("Int_FL_([0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "0-9/"))
            elif re.search("Int_FL_(1[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "10-19/"))
            elif re.search("Int_FL_(2[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "20-29/"))
            elif re.search("Int_FL_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "30-39/"))
            elif re.search("Int_FL_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "40-49/"))     
            elif re.search("Int_FL_([5-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_int_fl, "50+/"))
                
        
        """Expert"""
        if re.search("Exp_([0-999])", filepath):
            dest_exp = os.path.join(dest, "exp/untyped/")
            if re.search("Exp_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "30-39/"))
            elif re.search("Exp_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "40-49/"))
            elif re.search("Exp_(5[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "50-59/"))
            elif re.search("Exp_(6[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "60-69/"))
            elif re.search("Exp_(7[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "70-79/"))
            elif re.search("Exp_(8[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "80-89/"))
            elif re.search("Exp_(9[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "90-99/"))       
            elif re.search("Exp_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp, "100+/"))
                
        elif re.search("Exp_NF", filepath):
            dest_exp_nf = os.path.join(dest, "exp/NF/")
            if re.search("Exp_NF_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "30-39/"))
            elif re.search("Exp_NF_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "40-49/"))
            elif re.search("Exp_NF_(5[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "50-59/"))
            elif re.search("Exp_NF_(6[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "60-69/"))
            elif re.search("Exp_NF_(7[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "70-79/"))
            elif re.search("Exp_NF_(8[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "80-89/"))
            elif re.search("Exp_NF_(9[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "90-99/"))       
            elif re.search("Exp_NF_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_nf, "100+/"))  
        
        elif re.search("Exp_FL", filepath):
            dest_exp_fl = os.path.join(dest, "exp/FL/")
            if re.search("Exp_FL_(3[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "30-39/"))
            elif re.search("Exp_FL_(4[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "40-49/"))
            elif re.search("Exp_FL_(5[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "50-59/"))
            elif re.search("Exp_FL_(6[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "60-69/"))
            elif re.search("Exp_FL_(7[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "70-79/"))
            elif re.search("Exp_FL_(8[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "80-89/"))
            elif re.search("Exp_FL_(9[0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "90-99/"))       
            elif re.search("Exp_FL_([10-99][0-9][.])", filepath):
                shutil.copy(filepath, os.path.join(dest_exp_fl, "100+/"))
                
                    