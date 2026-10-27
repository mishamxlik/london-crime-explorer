"""Interactive dashboard based on MSc statistics coursework."""
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='London Crime Explorer',page_icon='📊',layout='wide')
BASE=Path(__file__).resolve().parent

@st.cache_data
def load_data():
    monthly=pd.read_csv(BASE/'data/monthly_by_borough.csv')
    types=pd.read_csv(BASE/'data/types_by_borough.csv')
    areas=pd.read_csv(BASE/'data/lsoa_rates.csv')
    return monthly,types,areas

monthly,types,areas=load_data()
boroughs=sorted(set(monthly['PartOfName']).intersection(types['PartOfName']))
st.title('London Crime Explorer')
st.caption('Street crime records: July 2024 – June 2025 | Population denominator: 2021 Census')
selected=st.sidebar.selectbox('Choose a London borough',boroughs)
m=monthly[monthly.PartOfName==selected].copy()
m['Month']=pd.to_datetime(m['Month'])
m=m.sort_values('Month')
t=types[types.PartOfName==selected].sort_values('Crimes',ascending=False)
a=areas[areas.PartOfName==selected]
col1,col2,col3=st.columns(3)
col1.metric('Recorded crimes',f'{int(m.Crimes.sum()):,}')
col2.metric('Crime categories',f'{len(t):,}')
col3.metric('LSOAs with data',f'{len(a):,}')
st.plotly_chart(px.line(m,x='Month',y='Crimes',markers=True,title=f'Monthly recorded crime — {selected}'),use_container_width=True)
st.plotly_chart(px.bar(t.head(12),x='Crimes',y='CrimeType',orientation='h',title='Most recorded crime categories').update_layout(yaxis={'categoryorder':'total ascending'}),use_container_width=True)
st.subheader('Crime rates across small areas')
st.caption('Crimes per 1,000 residents. Interpret with caution: city centres, commuters and visitors can inflate resident-based rates.')
st.plotly_chart(px.histogram(a,x='CrimesPer1000',nbins=35,title=f'Distribution of LSOA crime rates — {selected}'),use_container_width=True)
st.subheader('Geographical map')
geo_path = BASE / 'source_data' / 'LSOA_England_geom.gpkg'
if geo_path.exists():
    try:
        import geopandas as gpd
        geo=gpd.read_file(geo_path)
        code_col=next((c for c in ['LSOA21CD','LSOACode'] if c in geo.columns),None)
        if code_col:
            geo=geo.merge(a,left_on=code_col,right_on='LSOACode',how='inner')
            geo=geo.to_crs(4326)
            # Plotly choropleth uses geometry in WGS84.
            # Stable index property for Plotly matching.
            geo=geo.reset_index(drop=True)
            geo['map_id']=geo.index.astype(str)
            fig=px.choropleth(geo,geojson=geo.__geo_interface__,locations='map_id',
                              featureidkey='properties.map_id',color='CrimesPer1000',
                              title=f'Crime rate by LSOA — {selected}')
            fig.update_geos(fitbounds='locations',visible=False)
            st.plotly_chart(fig,use_container_width=True)
        else: st.warning('No compatible LSOA code column found in the GeoPackage.')
    except Exception as exc:
        st.warning(f'Map could not load: {exc}')
st.markdown('---')
st.caption('Source: modified police street-crime records and 2021 Census population data supplied for coursework. Observational patterns do not establish causation. Counts may reflect reporting practices and data limitations.')
