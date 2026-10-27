
First Project Specification 

Version 1
Pre and post-test probability viewer given a particular test
Inputs: prevalence or pre-test probability, specificity, sensitivity 
Features: Can enter sensitivity and specificity as a number or a slider
Outputs: post-test probability after positive and negative result (PPV or NPV), interpretation guide (this will just be a text prompt 
telling the user how to interpret the results); this can be a natural frequency sentence e.g. out of 1000 people 
A chart showing pre vs post test probability (bar graph)

Unit tests:
Will work through one examples, FOBT for colon cancer and 

Data for FOBT test (iFOBT from Japanese study)
# Focus on this one
Pre-cancerous adenomas
Sensitivity: 33.9%
Specificity 90.6% 

Early stage cancer
sensitivity = 84.6
Specificity 91.9%
Advanced cancer
Sensitivity 43.7%
Specificity 91.9% 

10% prevalence, 90% sensitivity 80% specificity



Sensitivty and Specificity

Test result
positive
negative 


FOrmulas

Test.  DIsease Healthy
+ve    TP.      FP
-ve.  FN       TN

Sensivity = TP/Disease 
Specificity = TN/Healthy 
PPV = TP/FP+FP 
NPV = TN/TN+FN

Complete when: 
* deployed
* tests pass
* README with limitations -> prevalence can drastically change results and sensitivity and specificity vary with patient mix 
* Inputs able to be enter on webapp via streamlit
* Logic works for worked example and can be trialled on other examples 
* Outputs are PPV and NPV + graph to show change between pre-test and post-test proability after positive and negative result
