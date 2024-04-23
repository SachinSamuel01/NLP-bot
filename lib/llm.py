from dotenv.main import load_dotenv
import os
import io
from langchain_openai.chat_models import ChatOpenAI
import warnings
from langchain_core.output_parsers import StrOutputParser
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


embeddings=OpenAIEmbeddings(openai_api_key='')
llm=ChatOpenAI(model_name='gpt-4',openai_api_key='')

# prompt='You are a AI bot'
# query=''
# print("Current Working Directory: ", os.getcwd())
# file_path = os.path.join('lib',"test", "test.txt")
# if os.path.exists(file_path):
#     print("File found!")
# else:
#     print("File not found at:", file_path)
# file=os.path.join('lib',"test", "test.txt")

def db(uploaded_file):
    if uploaded_file is None:
        return
    text_doc = uploaded_file.getvalue().decode("utf-8")
    file_path = os.path.join("lib", "tmp.txt")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())


    loader=TextLoader(file_path, encoding='utf8')
    text_doc=loader.load()
    
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=9000, chunk_overlap=100)
    docs=text_splitter.split_documents(text_doc)
    vectordb=Chroma.from_documents(documents=docs,
                                   embedding=embeddings,
                                   persist_directory='vector_database')
    vectordb.persist()
    vectordb=None
    vectordb=Chroma(persist_directory='vector_database',
                    embedding_function=embeddings)
    retriever=vectordb.as_retriever()
    return retriever

def bot(prompt,query,file,content=''):
    
    vectordb_retriever=db(file)
    docs=vectordb_retriever.get_relevant_documents(query)
    content=docs[0]
    
    template=''' Set of instructions is given to you in the prompt
    The content is just for reference until otherwise said so in the prompt, you can also find it empty

    prompt: {prompt} 
    content: {content}
    query: {query}
    '''
    promptss = ChatPromptTemplate.from_template(template)
    #promptss.format(context="Mary's sister is Susana", question="Who is Mary's sister?")
    
    parser=StrOutputParser()
    chain=promptss | llm | parser

    return chain.invoke({
        'prompt':prompt,
        'content':content,
        'query':query
    })

#response=bot(prompt,query,vectordb_retriever)




