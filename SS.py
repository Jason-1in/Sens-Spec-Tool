import math
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from cm import cMatrix

#user Interface

st.set_page_config(page_title = "Post-Test Probability Calculator", layout = "wide")
st.title("Post-Test Probability Calculator")
st.caption ("Educational tool, not for clinical decisions")

with st.sidebar: 
    prevalence= st.number_input("Prevalence/pre-test probability (%)", min_value = 0.0, max_value=100.0, value = 10.0, step = 0.1)
    sensitivity= st.slider("Sensitivity (%):", min_value = 0.0, max_value = 100.0, value = 90.0, step = 0.5)
    specificity = st.slider("Specificity (%):",min_value = 0.0, max_value = 100.0, value = 90.0, step = 0.5)


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


df = pd.DataFrame({
    "Scenario": ["Pre-test", "After positive test", "After negative test"],
    "Probability of disease (%)": [prevalence, post_positive , post_negative ],
})

#Display 
st.write(f"Probability of having the condition after a positive result **{post_positive:.2f} %**")
st.write(f"Probability of having the condition after a negative result **{post_negative:.2f} %**")

fig = px.bar(df, x="Scenario", y = "Probability of disease (%)", range_y = [0,100], text_auto=".1f")

#Plot of PPV vs prevalence curve/NPV vs prevalence curve

sens,spec = sensitivity/100, specificity/100
prevs = np.linspace(0.01,0.99,99)

prevs_curve = pd.DataFrame({
    "Prevalence(%)": prevs*100,
    "After positive test": [cMatrix(sens,spec,p).ppv() * 100 for p in prevs],
    "After negative test": [(1- cMatrix(sens,spec,p).npv()) * 100 for p in prevs]
})

fig2 = px.line (prevs_curve, x= "Prevalence(%)",
                y = ["After positive test", "After negative test"], range_y = [0,100],
                labels = {"value": "Probability of disease (%)", "variable": "Test Result"})
fig2.add_vline(x=float(prevalence), line_dash="dash")
fig2.add_annotation(x = float(prevalence), y = 100, text = "Your pre-test probability", showarrow = False, yanchor = "bottom",xanchor = "left")

col1,col2 = st.columns (2)
with col1: 
    st.plotly_chart(fig, use_container_width = True)
with col2: 
    st.plotly_chart(fig2, use_container_width = True)



#Natural frequencies table , calculated with population = 1000 default 

st.subheader (f"Natural Frequencies table for population of {CM.population}")
tp, fp = CM.truePositive, CM.falsePositive
fn, tn = CM.falseNegative, CM.trueNegative

nf_table = pd.DataFrame(
    {
        "Disease present": [ tp,fn,tp+fn], 
        "Disease absent": [fp,tn, fp+tn],
        "Total": [tp+fp, fn+tn, CM.population],
    },
    index = ["Test positive", "Test negative", "Total"],

)
st.table(nf_table.style.format("{:.0f}"))
st.write(f"Out of {CM.population}, people with this pre-test probability:")


st.write(
    f"- About **{tp + fp:.0f}** would test positive.\n"
    f"- About **{tp:.0f}** of them would actually have the disease."
)
#Formatting time 

