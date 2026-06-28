import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("Joseph.jpeg", width=180)
with col2:
    st.markdown("<h1 style='margin-bottom: 0;'>Joseph (Xingkai) Wu</h1>", unsafe_allow_html=True)
    st.markdown("**Senior Associate Data Analyst | Capital One**")
    st.markdown("Toronto, Ontario, Canada • Hybrid")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/xkjosephwu/) • [GitHub](https://github.com/xwu0223) • [Tableau](https://public.tableau.com/app/profile/xingkai.eu)")

st.markdown("---")

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################
st.markdown('## Summary')
st.markdown('''
- Senior analytics professional specializing in dbt pipeline architecture, Snowflake transformation workflows, and data quality automation.
- Delivered streamlined analytics that reduced processing latency by 30% and enabled executive-level credit strategy recommendations.
- Partnered with product, engineering, and AI/ML teams to convert complex datasets into reliable, business-ready insights.
''')

st.markdown('---')

#####################
st.markdown('## Work Experience')

txt('**Senior Associate Data Analyst**, *Capital One* | Toronto, ON • Hybrid',
'Oct 2025 - Present')
st.markdown('''
- Architected and maintained a modular dbt pipeline in Snowflake, reducing data processing latency by 30%.
- Analyzed Credit Limit Increase underwriting strategies using SQL and Python, optimizing risk mitigation.
- Implemented custom dbt validations and automated data quality checks to identify anomalies proactively.
- Collaborated with cross-functional stakeholders to translate analytics into executive credit strategy recommendations.
''')

txt('**Data Scientist II**, *TD* | Toronto, ON • Hybrid',
'Nov 2024 - Sep 2025')
st.markdown('''
- Served as analytics lead for the Private Wealth Management 4-Pillar Platform, optimizing client journey insights.
- Integrated third-party data sources with data engineering to improve data reliability and analytics coverage.
- Partnered with AI/ML teams on causal inference analysis, influencing advisor behavior and client engagement.
- Led product attrition analysis and delivered insights for targeted retention strategies across business units.
''')

txt('**Senior Business Intelligence Analyst**, *TD* | Toronto, ON • Hybrid',
'May 2022 - Nov 2024')
st.markdown('''
- Modernized ETL pipelines for enterprise datasets, improving efficiency for BI and analytics teams.
- Developed a KPI dashboard for Business Banking, enabling data-driven decision-making for executives.
- Migrated market share analytics from legacy systems to Python, SQL, and Tableau, improving reporting efficiency by 90%.
- Recognized as a 2023 Q4 Legendary Recipient for high-impact analytics delivery.
''')

txt('**Analytics Consultant** (Student Project), Client: Interac Corp. | Toronto, ON',
'2021 - 2022')
st.markdown('''
- Directed project planning, task assignment, and stakeholder communication for a data governance consulting engagement.
- Built a classification pipeline using SQL, Python, and Tableau to visualize customer behavior and segmentation opportunities.
- Applied XGBoost, HistGradientBoostingClassifier, and SHAP to deliver interpretable customer segment recommendations.
''')

txt('**Research Assistant**, Advanced Power Electronics Lab, *York University* | Toronto, ON',
'2016 - 2018')
st.markdown('''
- Built a Raspberry Pi and Python-based oscilloscope data logger to capture electrical measurements and waveforms.
- Developed an SQL/HTML/CSS inventory application to streamline component search and prototype development.
''')

st.markdown('---')

#####################
st.markdown('## Education')

txt('**Master of Business Analytics (MBAN)**, *Schulich School of Business*',
'2021 - 2022')
st.markdown('''
- GPA: `A-`
- Relevant coursework: Visual Analytics and Modelling, Data Science, Predictive Modelling, Data Management.
- 1st place, University of New Brunswick Data Sprint Competition; finalist, Data Visualization Competition.
''')

txt('**Bachelor of Engineering**, Electrical Engineering, *York University*',
'2014 - 2019')
st.markdown('''
- GPA: `B+`
''')

st.markdown('---')

#####################
st.markdown('## Skills')

txt3('Analytics engineering', '`dbt`, `Snowflake`, `ETL`, `data quality`')
txt3('Programming', '`Python`, `SQL`, `R`, `pandas`, `numpy`')
txt3('Visualization', '`Tableau`, `Power BI`, `plotly`, `matplotlib`, `seaborn`')
txt3('Modeling', '`scikit-learn`, `causal inference`, `statistics`')
txt3('Deployment & tools', '`streamlit`, `Azure`, `git`, `Jira`')

st.markdown('---')

#####################
st.markdown('## Social Media')
txt2('LinkedIn', 'https://www.linkedin.com/in/xkjosephwu/')
txt2('GitHub', 'https://github.com/xwu0223')
txt2('Tableau', 'https://public.tableau.com/app/profile/xingkai.eu')
