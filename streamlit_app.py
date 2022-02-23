import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Joseph(Xingkai) Wu
''')

image = Image.open('Joseph.jpeg')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Data Analyst/ Scientist with 3 of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as presenter at multiple business data competitions and prject deliveries.
- Strong programming and analytical skills as demonstrated by prior professional and project experience
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Business Analytics** (MBAN), *Schulich School of Business*, Canada',
'20021-2022')
st.markdown('''
- GPA: `A-`
- Relevant Courses Visual Analytics and Modelling, Data Science, Predictive Modelling, Data Management.
- Received the 1st place in University New Brunswick Data Sprint Competition, and the Finalist in Data Visualization Competition.
- Lead group of 4 students in Analytics Consulting Project(Client- Interac Corp.) in data governance and classification modelling.
''')

txt('**Bachelors of Egnineering** (Electrical Engineering), *York University*, Canada',
'2014-2019')
st.markdown('''
- GPA: `B+`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Analytics Consultant** (Student Project), Client- Interac Corp., Toronto, Canada',
'2021-2022')
st.markdown('''
- Designed project roadmap by understanding project scope, deliverable, and assigning task responsibilities, to keep Client and team members updated on the project objective, progress, and roadblocks. 
- Developed case study to understand customer segmentation by using Tableau to create a dashboard which visualize customer payment diary data, which helped target products to a particular customer group.
- Utilized XGBoost, HistGradientBoost, and stacked Ensemble models to in Python, to create a model that classifies customers into interpretable segments using SHAP, and make actionable recommendations.
''')

txt('**Data Analyst** (Contract), Toronto Transit Commission, Toronto, Canada',
'2019-2020')
st.markdown('''
- Merged customer satisfaction survey data via python and SQL, and conducted explanatory data analysis, to impute missing data and uncover a parsimonious model with most influential variables.
- Visualized data and reported key findings and actionable insights via PowerBI report, to help management with future operation plan.
- Built multiple linear regression model using Python Scikit Learn package, to forecast customer satisfaction with a given budget, personnel management, and assisted TTC subway segment to identify key variables to improve customer satisfaction in different parts of the City of Toronto.
''')

txt('**Research Assistant**, Advanced Power Electronics Lab, York University, Toronto',
'2016-2018')
st.markdown('''
- Designed and implemented oscilloscope data logging tool using Raspberry with Python, which collects circuits’ electrical measurements and waveforms. The logging tool saves hours of data entry and validation, improves experiments efficiency and enables researchers designing more configurations.
- Designed and implemented components searching and inventory web application using SQL, HTML, and CSS, to improve research prototype efficiency and workflow, saving hours of components searching time and weeks of restocking time.
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SAS`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `Tableau`, `PowerBI`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Azure`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/xkjosephwu/')
txt2('GitHub', 'https://github.com/xwu0223')
txt2('Tableau', 'https://public.tableau.com/app/profile/xingkai.eu')