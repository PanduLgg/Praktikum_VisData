import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz


#Graphviz
st.title('Graphviz Chart')
#Creating Graph Object
st.graphviz_chart('''
    digraph {   
    "Training Data" -> "ML Algorithm" 
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"
    }
                  ''')

#Create Ghraphlib by Graph Object
st.title('Graphviz Object')
graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)