from plotly.offline import plot, iplot, init_notebook_mode
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.request import urlopen
from datetime import timedelta
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from plotly.offline import plot
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# statistics start
plots = []

data = pd.read_csv(
    "datasets/covid19GlobalForecastingweek1/train.csv", parse_dates=['Date'])
cleaned_data = pd.read_csv(
    "datasets/covid19cleancompletedataset/covid_19_clean_complete.csv", parse_dates=['Date'])
cases = ['Confirmed', 'Deaths', 'Recovered', 'Active']
cleaned_data['Active'] = cleaned_data['Confirmed'] - \
    cleaned_data['Deaths'] - cleaned_data['Recovered']
cleaned_data['Country/Region'] = cleaned_data['Country/Region'].replace(
    'Mainland China', 'China')
cleaned_data[['Province/State']
             ] = cleaned_data[['Province/State']].fillna('')
cleaned_data[cases] = cleaned_data[cases].fillna(0)
cleaned_data.rename(columns={'Date': 'date'}, inplace=True)
data = cleaned_data

grouped = data.groupby(
    'date')['date', 'Confirmed', 'Deaths', 'Active'].sum().reset_index()
grouped = data.groupby(
    'date')['date', 'Confirmed', 'Deaths', 'Active'].sum().reset_index()

fig1 = px.line(grouped, x="date", y="Deaths",
               title="Worldwide Death Cases Over Time")

grouped_india = data[data['Country/Region'] == "India"].reset_index()
grouped_india_date = grouped_india.groupby(
    'date')['date', 'Confirmed', 'Deaths'].sum().reset_index()
plot_titles = ['India']

fig2 = px.line(grouped_india_date, x="date", y="Confirmed",
               title=f"Confirmed Cases in {plot_titles[0].upper()} Over Time", color_discrete_sequence=['#F61067'], height=500)

data['Province/State'] = data['Province/State'].fillna('')
temp = data[[col for col in data.columns if col != 'Province/State']]
latest = temp[temp['date'] == max(temp['date'])].reset_index()
latest_grouped = latest.groupby(
    'Country/Region')['Confirmed', 'Deaths'].sum().reset_index()

fig3 = px.bar(latest_grouped.sort_values('Confirmed', ascending=False)[
    :40][::-1], x='Confirmed', y='Country/Region', title='Confirmed Cases Worldwide', text='Confirmed', height=1000, orientation='h')

fig4 = px.bar(latest_grouped.sort_values('Deaths', ascending=False)[:30][::-1], x='Deaths', y='Country/Region', color_discrete_sequence=[
    '#84DCC6'], title='Deaths Cases Worldwide', text='Deaths', height=1000, orientation='h')

temp = cleaned_data.groupby(
    'date')['Recovered', 'Deaths', 'Active'].sum().reset_index()
temp = temp.melt(id_vars="date", value_vars=[
    'Recovered', 'Deaths', 'Active'], var_name='case', value_name='count')
temp['case'].value_counts()
pio.templates.default = "plotly_dark"

fig5 = px.line(temp, x="date", y="count", color='case',
               title='Cases over time: Line Plot', color_discrete_sequence=['cyan', 'red', 'orange'])

fig6 = px.area(temp, x="date", y="count", color='case',
               title='Cases over time: Area Plot', color_discrete_sequence=['cyan', 'red', 'orange'])

formated_gdf = data.groupby(
    ['date', 'Country/Region'])['Confirmed', 'Deaths'].max()

formated_gdf = data.groupby(
    ['date', 'Country/Region'])['Confirmed', 'Deaths'].max()
formated_gdf = formated_gdf.reset_index()
formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
formated_gdf['size'] = formated_gdf['Confirmed'].pow(0.3)

fig8 = px.scatter_geo(formated_gdf, locations="Country/Region", locationmode='country names',
                      color="Confirmed", size='size', hover_name="Country/Region",
                      range_color=[0, 1500],
                      projection="natural earth", animation_frame="date",
                      title='COVID-19: Spread Over Time', color_continuous_scale="portland")

formated_gdf = formated_gdf.reset_index()
formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
formated_gdf['size'] = formated_gdf['Confirmed'].pow(0.3)
pio.templates.default = "plotly_dark"
fig7 = px.scatter_geo(formated_gdf, locations="Country/Region", locationmode='country names', color="Deaths", size='size', hover_name="Country/Region",
                      range_color=[0, 100],  projection="natural earth", animation_frame="date",  title='COVID-19: Deaths Over Time', color_continuous_scale="peach")

# statistics end


# symptoms start

symptoms = {'symptom': ['Fever',
                        'Dry cough',
                        'Fatigue',
                        'Sputum production',
                        'Shortness of breath',
                        'Muscle pain',
                        'Sore throat',
                        'Headache',
                        'Chills',
                        'Nausea or vomiting',
                        'Nasal congestion',
                        'Diarrhoea',
                        'Haemoptysis',
                        'Conjunctival congestion'], 'percentage': [87.9, 67.7, 38.1, 33.4, 18.6, 14.8, 13.9, 13.6, 11.4, 5.0, 4.8, 3.7, 0.9, 0.8]}

symptoms = pd.DataFrame(data=symptoms, index=range(14))

symptom_graph = px.bar(symptoms[['symptom', 'percentage']].sort_values('percentage', ascending=False),
                       y="percentage", x="symptom", color='symptom',
                       log_y=True, template='ggplot2', title='Symptom of  Coronavirus')
symptom_div = plot(symptom_graph, output_type='div', include_plotlyjs=False, show_link=False,
                   link_text="", image_width=500, config={"displaylogo": False})
plots.append(symptom_div)

# symptoms end

# india starts


cnf = '#393e46'  # confirmed - grey
dth = '#ff2e63'  # death - red
rec = '#21bf73'  # recovered - cyan
act = '#fe9801'  # active case - yellow

register_matplotlib_converters()
pio.templates.default = "plotly"

# importing datasets
df = pd.read_csv('datasets/complete.csv', parse_dates=['Date'])
df['Name of State / UT'] = df['Name of State / UT'].str.replace(
    'Union Territory of ', '')
df = df[['Date', 'Name of State / UT', 'Latitude', 'Longitude',
         'Total Confirmed cases', 'Death', 'Cured/Discharged/Migrated']]
df.columns = ['Date', 'State/UT', 'Latitude',
              'Longitude', 'Confirmed', 'Deaths', 'Cured']

for i in ['Confirmed', 'Deaths', 'Cured']:
    df[i] = df[i].astype('int')

df['Active'] = df['Confirmed'] - df['Deaths'] - df['Cured']
df['Mortality rate'] = df['Deaths']/df['Confirmed']
df['Recovery rate'] = df['Cured']/df['Confirmed']

df = df[['Date', 'State/UT', 'Latitude', 'Longitude', 'Confirmed',
         'Active', 'Deaths', 'Mortality rate', 'Cured', 'Recovery rate']]
latest = df[df['Date'] == max(df['Date'])]

# days
latest_day = max(df['Date'])
day_before = latest_day - timedelta(days=1)

# state and total cases
latest_day_df = df[df['Date'] == latest_day].set_index('State/UT')
day_before_df = df[df['Date'] == day_before].set_index('State/UT')

temp = pd.merge(left=latest_day_df, right=day_before_df,
                on='State/UT', suffixes=('_lat', '_bfr'), how='outer')
latest_day_df['New cases'] = temp['Confirmed_lat'] - temp['Confirmed_bfr']
latest = latest_day_df.reset_index()
latest.fillna(1, inplace=True)

temp = latest.sort_values('Confirmed', ascending=False)
states = temp['State/UT']

fig = go.Figure(data=[
    go.Bar(name='Confirmed', x=states, y=temp['Confirmed']),
    go.Bar(name='Recovered', x=states, y=temp['Cured']),
    go.Bar(name='Deaths', x=states, y=temp['Deaths'])
])
# Change the bar mode
fig9 = fig.update_layout(barmode='group')

fig10 = px.scatter(latest[latest['Confirmed'] > 10], x='Confirmed', y='Deaths', color='State/UT', size='Confirmed',
                   text='State/UT', log_x=True, title='Confirmed vs Death')

figs = [fig1, fig2, fig3, fig4, fig5, fig6,
        fig7, fig8, fig9, fig10]

for x in figs:
    plot_div = plot(x, output_type='div', include_plotlyjs=False, show_link=False,
                    link_text="", image_width=500, config={"displaylogo": False})
    plots.append(plot_div)


def coronaCount(url):
    counts = []
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    qs = soup.find_all('div', {'class': 'maincounter-number'})
    for x in qs:
        counts.append(int(x.text.replace(',', '')))
    qs1 = soup.find('div', {'class': 'number-table-main'})
    counts.append(int(qs1.text.replace(',', '')))
    return counts


def index(request):
    # world = coronaCount('https://www.worldometers.info/coronavirus/')
    # india = coronaCount('https://www.worldometers.info/coronavirus/country/india/')
    # india[3] = india[0] - (india[1]+india[2])
    # {'world_total': f"{world[0]:,d}", 'world_active': f"{world[1]:,d}", 'world_dead': f"{world[2]:,d}", 'world_recovered': f"{world[3]:,d}", 'india_total': f"{india[0]:,d}", 'india_active': f"{india[1]:,d}", 'india_dead': f"{india[2]:,d}", 'india_recovered': f"{india[3]:,d}"})
    return render(request, 'index.html')


def statistics(request):
    global plot
    return render(request, "statistics.html", context={'plot_div1': plots[1], 'plot_div2': plots[2], 'plot_div3': plots[3], 'plot_div4': plots[4], 'plot_div5': plots[5], 'plot_div6': plots[6], 'plot_div9': plots[9], 'plot_div10': plots[10]})


def prevention(request):
    return render(request, 'prevention.html')


def symptoms(request):
    global plots
    return render(request, 'symptoms.html', context={'symp': plots[0]})


def faq(request):
    return render(request, 'faq.html')


def map_stats(request):
    global plots
    return render(request, 'india_map.html', context={'plot_div7': plots[7], 'plot_div8': plots[8]})


def prediction(request):
    return render(request, 'prediction.html')
