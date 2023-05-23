from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


#get video summary

map_prompt = """
Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:
"""
map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])

combine_prompt = """
Write a concise summary of the following text in short bullet points that covers the key points of the text.
```{text}```
Bullet point summary:
"""
combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])

llm = OpenAI(temperature=0)

summary_chain = load_summarize_chain(llm=llm, chain_type='map_reduce', map_prompt=map_prompt_template, combine_prompt=combine_prompt_template)