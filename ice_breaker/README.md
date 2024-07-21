# Ice Breaker

### Introduction

```python
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == "__main__":
    load_dotenv()

    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $178 billion.[4]

A member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.

In 2004, Musk became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.). He became the company's chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, Musk founded xAI, an artificial intelligence company.

Musk has expressed views that have made him a polarizing figure.[5] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and antisemitic conspiracy theories.[5][6][7][8] His ownership of Twitter has been similarly controversial, being marked by layoffs of large numbers of employees, an increase in hate speech and misinformation and disinformation on the website, and changes to Twitter Blue verification.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": information})

    print(res)

"""
{
'information': "\n    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $178 billion.[4]\n\nA member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.\n\nIn 2004, Musk became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.). He became the company's chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, Musk founded xAI, an artificial intelligence company.\n\nMusk has expressed views that have made him a polarizing figure.[5] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and antisemitic conspiracy theories.[5][6][7][8] His ownership of Twitter has been similarly controversial, being marked by layoffs of large numbers of employees, an increase in hate speech and misinformation and disinformation on the website, and changes to Twitter Blue verification.\n    ", 
'text': '1. Elon Musk is a highly successful businessman and investor known for his involvement in various companies such as SpaceX, Tesla, and Twitter. He is one of the wealthiest individuals in the world, with a net worth estimated at $178 billion.\n\n2. Two interesting facts about Elon Musk:\n- He dropped out of Stanford University after just two days to pursue his entrepreneurial ventures.\n- Musk has been involved in the creation of several innovative companies, including SpaceX, Tesla, SolarCity, Neuralink, and the Boring Company.'
}
"""
```

### Ollama & str output

```python
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

from third_parties import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": scrape_linkedin_profile("asd", mock=True)})

    print(res)
"""
Based on the LinkedIn information, here are:

**Summary**: Eden Marco is a former Captain in the Israel Defense Forces (IDF) with a Bachelor's Degree in Computer Science from Technion - Israel Institute of Technology.

**Two Interesting Facts**:

1. **Military Background**: Eden was a Captain in the IDF, serving from 2010 to 2014. This suggests that they have strong leadership and problem-solving skills, developed through their military experience.
2. **Computer Science Education**: After leaving the IDF, Eden pursued higher education in Computer Science at Technion - Israel Institute of Technology. This indicates that they are interested in technology and have a strong foundation in computer science principles.

Please let me know if you'd like me to highlight anything else!
"""
```

### ReAct with search

```python
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

from tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                                  Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    linkedin_url = lookup("Eden Marco")
    print(linkedin_url)

"""
> Entering new AgentExecutor chain...
I need to find the Linkedin profile page for Eden Marco.
Action: Crawl Google 4 linkedin profile page
Action Input: Eden Marcohttps://www.linkedin.com/in/eden-marcoI have found the Linkedin profile page for Eden Marco.
Final Answer: https://www.linkedin.com/in/eden-marco

> Finished chain.
https://www.linkedin.com/in/eden-marco
"""
```

### Working with frontend - OutputParser

```python
from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")


summary_parser = JsonOutputParser(pydantic_object=Summary)

"""-----------------------------------------------------------"""

summary_template = """
given the Linkedin information {information} about a person I want you to create:
1. A short summary
2. two interesting facts about them
\n{format_instructions}
"""
summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template,
    partial_variables={"format_instructions": summary_parser.get_format_instructions()},
)

# llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
llm = ChatOllama(model="llama3")
chain = summary_prompt_template | llm | summary_parser
res = chain.invoke(input={"information": scrape_linkedin_profile("asd", mock=True)})

print(res)

"""
{'summary': "Captain at Israel Defense Forces with a Bachelor's Degree in Computer Science from Technion - Israel Institute of Technology.", 
'facts': ['Serves as Captain at Israel Defense Forces, showcasing leadership skills and dedication to national service.', "Graduated with a Bachelor's Degree in Computer Science from Technion - Israel Institute of Technology, highlighting academic achievement."]}
"""
```
