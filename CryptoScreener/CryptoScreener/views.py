from urllib import request
from django.shortcuts import render
import pandas as pd 
import os 

def MainScreener(request):
    print(os.listdir())
    df = pd.read_excel('CryptoScreener/final_output.xlsx',)
    xdf = {'TickerNomatches':[],
    'Chgpercent':[],
    "Chg":[],
    "Vol":[]
    }
    for i in range(len(df['TickerNomatches'])):
        xdf['TickerNomatches'].append(df['TickerNomatches'][i])
        xdf['Chg'].append(df['Chg'][i])
        xdf['Chgpercent'].append(df['Chgpercent'][i])
        xdf['Vol'].append(df['Vol'][i])

    print(xdf)

    xdf = zip(xdf['TickerNomatches'], xdf['Chg'],xdf['Chgpercent'],xdf['Vol'])
    return render(request, 'frontend.html',{'df':xdf,
    'range':range(4)
    }
    )