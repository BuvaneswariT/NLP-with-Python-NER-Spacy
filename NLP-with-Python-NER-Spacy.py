#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
pprint(...)


# In[8]:


doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])


# In[9]:


pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])


# In[52]:


from bs4 import BeautifulSoup
import requests
import re
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://techjobs.sulekha.com/qa-automation-testing-training')
article = nlp(ny_bb)
len(article.ents)


# In[53]:


labels = [x.label_ for x in article.ents]
Counter(labels)


# In[54]:


items = [x.text for x in article.ents]
Counter(items).most_common(3)


# In[55]:


sentences = [x for x in article.sents]
print(sentences[22])


# In[56]:


displacy.render(nlp(str(sentences[22])), jupyter=True, style='ent')


# In[57]:


displacy.render(nlp(str(sentences[23])), style='dep', jupyter = True, options = {'distance': 120})


# In[58]:


[(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(str(sentences[23])) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]


# In[59]:


dict([(str(x), x.label_) for x in nlp(str(sentences[27])).ents])


# In[60]:


print([(x, x.ent_iob_, x.ent_type_) for x in sentences[25]])


# In[61]:


displacy.render(article, jupyter=True, style='ent')


# In[ ]:




