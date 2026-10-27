import math
import pandas as pd
import plotly.express as px
import streamlit as st
from cm import cMatrix
#functions 



#Variables

#user Interface

st.title("Post-Test Probability Calculator")

with st.sidebar: 
    prevalence= st.number_input("Prevalence/pre-test probability", min_value = 0, max_value=100, value = 10)
    sensitivity= st.slider("Sensitivity (%):", min_value = 0, max_value = 100, value = 90)
    specificity = st.slider("Specificity (%):",min_value = 0, max_value = 100, value = 90)


#logical checks
if prevalence == 0:
    st.error ("Test is not useful in this population and values cannot be calculated")
    st.stop()
#Logic CM = confusionMatrix
CM = cMatrix(sensitivity/100, specificity/100, prevalence/100)

post_positive = (CM.ppv()) * 100
post_negative = (1-CM.npv()) * 100

if math.isnan(post_positive) or math.isnan(post_negative):
    st.warning("Post-test probability is undefined for these inputs")
    st.stop()
#create dataframe with pre and post-test probabilities
npvC = 1-float(CM.npv())


df = pd.DataFrame({
    "Scenario": ["Pre-test", "After positive test", "After negative test"],
    "Probability of disease (%)": [prevalence, post_positive , post_negative ],
})

#Display 
st.text(f"Probability of having the condition after a positive result {post_positive:.2f} %", width = "content")
st.text(f"Probability of having the condition after a negative result {post_negative:.2f} %", width = "content")

fig = px.bar(df, x="Scenario", y = "Probability of disease (%)", range_y = [0,100])

st.plotly_chart(fig)

