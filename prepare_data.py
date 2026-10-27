"""Run once with the coursework CSVs to create small dashboard-ready datasets."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source_data'
OUT = ROOT / 'data'
OUT.mkdir(exist_ok=True)
crime_path = SOURCE / 'cw1-street-outcome.csv'
pop_path = SOURCE / 'LSOA_data.csv'

pop = pd.read_csv(pop_path, usecols=['LSOACode','PartOfName','Total'])
pop = pop.drop_duplicates('LSOACode')
# Keep London boroughs only, identified from the crime data rather than assumed list.
crime_chunks = pd.read_csv(crime_path, usecols=['Month','LSOACode','CrimeType'], chunksize=200_000)
monthly_parts=[]; type_parts=[]; area_parts=[]
for chunk in crime_chunks:
    chunk=chunk.dropna(subset=['LSOACode','Month','CrimeType'])
    chunk=chunk.merge(pop[['LSOACode','PartOfName']],on='LSOACode',how='inner')
    monthly_parts.append(chunk.groupby(['PartOfName','Month']).size().rename('Crimes').reset_index())
    type_parts.append(chunk.groupby(['PartOfName','CrimeType']).size().rename('Crimes').reset_index())
    area_parts.append(chunk.groupby('LSOACode').size().rename('Crimes').reset_index())

def combine(parts,keys):
    return pd.concat(parts).groupby(keys,as_index=False)['Crimes'].sum()
monthly=combine(monthly_parts,['PartOfName','Month'])
monthly.to_csv(OUT/'monthly_by_borough.csv',index=False)
combine(type_parts,['PartOfName','CrimeType']).to_csv(OUT/'types_by_borough.csv',index=False)
area=combine(area_parts,['LSOACode']).merge(pop,on='LSOACode',how='left')
area=area[area['Total']>0].copy()
area['CrimesPer1000']=area['Crimes']/area['Total']*1000
area.to_csv(OUT/'lsoa_rates.csv',index=False)
print('Created three dashboard-ready files in data/.')
