# CovidTracker - Teslacoil

### Project Overview

---

##### Problem

Covid19 a real issue, a massive pandemic, how can we increase public awareness and help users to visualise their condtions and have a fair idea of the upcoming future.

##### Solution

- We gather data from the sources and create all sorts of data visualisation depicting the reach of the virus.
- We use graphs and plots to show the spread of the virus over time throughout the world, the deaths over time, the recovered over time.
- Main focus is on India, we have visuals on Indian spread and have shown every detail of the spread, death, recovery in India.
- We have included an prediction using fbprophet which is the most advanced tool for this, to show the prediction of spread and deaths in the upcoming 100 days.
- We have included symptoms of corona virus infected and have explained visually in form of graphs which symptom stands out the most.
- We even have included a few preventive measures to explain the audience what can be done to avoid this.
- There is also a dedicated application which can track and predict the chances of a person being infected in term of probability.
- We have made sure that users have complete satisfaction using this website and have the complete knowledge and awareness needed.

### Solution Description

---

#### Technical Description

##### Technologies and libraries used

Following are some important technologies and libraries used. See a complete list in the [requirements file](Application Code/requirements.txt).

| Technology     | Version    |
| -------------- | ---------- |
| python         | 3.6.5      |
| Django         | 3.0.4      |
| nltk           | 3.4.5      |
| numpy          | 1.17.4     |
| pandas         | 0.25.3     |
| virtualenv     | 16.7.8     |
| beautifulsoup4 | 4.8.2      |
| lxml           | 4.5.0      |
| numpy          | 1.18.0     |
| opencv-python  | 4.1.2.30   |
| pandas         | 1.0.1      |
| pipenv         | 2018.11.26 |
| scipy          | 1.4.1      |
| seaborn        | 0.10.0     |
| plotly         | 4.6.0      |
| requests       | 2.23.0     |
| bs4            | 0.0.1      |
| psycopg2       | 2.8.4      |

##### Setup/Installations required to run the solution for testing

1. You are inside **Application Code** and run the following commands

   - install virtualenv `pip install virtualenv`
   - create virtualenv `virtualenv env`
   - activate the env `/env/Scripts/activate`
   - `pip install -r requirements.txt`

2. change directory to **hack2hire**

   - `python manage.py migrate`
   - `python manage.py collectstatic` if prompted please type `yes` and press enter.

3. in the terminal `python manage.py runserver` please wait until it shows running, this takes a bit of time.

4. **In Any Browser open link localhost:8000 or 127.0.0.1:8000**
