#                                                                                                                                                             #
# Tudor44                                                                                                                                                     #
# An example for extract in Json format a review sentiment from italian text/reviews composing a prompt in natural language using a Supervised Learning task. #                                                     #
#                                                                                                                                                             #   
from api import Api
import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#external class for api integrations, 
api = Api()

#llm default OpenAPI
llm = api.llm

#streamlit view component
st.title('Sentiment Analysis')
text_review = st.text_area('Write me a review in Italian') 

#1 prompt template
template = """
Please act as a machine learning model trained for perform a supervised learning task, 
for extract the sentiment of a review in Italian Language.

Give your answer writing a Json evaluating the sentiment field between the dollar sign, the value must be printed without dollar sign.
The value of sentiment must be "positive"  or "negative", otherwise if the text is not valuable write "null".

Example:

field 1 named :
text_review with value: {text_review}
field 2 named :
sentiment with value: $sentiment$

Review text: '''{text_review}'''

"""
prompt = PromptTemplate(template=template, input_variables=["text_review"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = text_review

if prompt:
    response = llm_chain.run(question)
    #json printed
    print(response)
    st.text(response) 
