import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

#import data

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confired=pd.read_csv(url_confirmed)
deaths=pd.read_csv(url_deaths)
recovered=pd.read_csv(url_recovered)


date1=confired.columns[4:]
total_confirmed=confired.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_vars=date1,var_name='date',value_name='confired')
date2=deaths.columns[4:]
total_death=deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_vars=date2,var_name='date',value_name='deaths')
date3=recovered.columns[4:]
total_recovered=recovered.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_vars=date3,var_name='date',value_name='recovered')

#merging data frames
covid_data=total_confirmed.merge(right=total_death,how='left',on=['Province/State', 'Country/Region','date','Lat','Long'])
covid_data=covid_data.merge(right=total_recovered,how='left',on=['Province/State','Country/Region','date','Lat','Long'])

#converting date column froms tring
covid_data['date']=pd.to_datetime(covid_data['date'])
covid_data.isna().sum()

#replace nan with 0
covid_data['recovered']=covid_data['recovered'].fillna(0)

#calculated new colom
covid_data['active']=covid_data['confirmed']-covid_data
['death']-covid_data['recovered']
covid_data_1= covid_data.groupby(['date'])[['confirmed','death','recovered','active']].sum().reset_index()

covid_data_2=covid_data.groupby(['date','Country/Region'])[['confirmed','death','recovered','active']].sum().reset_index()

#membuat list dictionary
covid_data_dict=covid_data[['Country/Region','Lat','Long']]
list_locations=covid_data_dict.set_index('Country/Region')[['Lat','Long']].T.to_dict('dict')

app=dash.Dash(__name__,meta_tags=[{'name':'viewport','content':'width=device-width'}])
app.layout=html.Div(
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={
                         'height':'60px',
                         'width':'auto',
                         'margin-bottom':'25px',
                     },
                     )
        ],
        className='one-third column',
        ),
        html.Div([
            html.Div([
                html.H3('Covid -19', style={'margin-botton':'0px','color':'white'}),
                html.H5('Track Covid -19 Cases',style={'margin-top':'0px','color':'white'}),
            ])
        ],className='one-half column',id='title'
        ),
        html.Div([
            html.H6('Last Updated: ' + str(covid_data_1['date'].iloc[-1].strftime('%B %d,%Y')) + ' 00:01 (UTC)',
                                           style={'color':'orange'}
                                           ),
        ],className='one-third column',id='title1'),
    ],id)
)