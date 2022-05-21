#mg is mg/dl, mk is mkmol/l, mm is mmol/l
def CKD_EPI (crea, age, sex, unit="mg", black_race=False):
    if black_race:
        race_koef = 1.159
    else:
        race_koef = 1

    if unit == "mk":
        crea = 0.0113*crea
    elif unit == "mm":
        crea = 1.13*crea

    if sex == 'm':
        sex_koef = 1
        alpha = -0.411
        kappa = 0.9
        
        d = 0.9
        k = 141
        if (crea<=0.9):
            degree = -0.411
        else:
            degree = -1.209
    else:
        sex_koef = 1.018
        alpha = -0.329
        kappa = 0.7
        
        d = 0.7
        k = 144
        if (crea<=0.7):
            degree = -0.329
        else:
            degree = -1.209
    GFR = round((141*(min(crea/kappa,1)**alpha)*(max(crea/kappa,1)**-1.209)*(0.993**age)*sex_koef*race_koef),1)
    GFR_sempler = round((k*(crea/d)**degree*0.993**age),1)

    return [GFR,GFR_sempler]