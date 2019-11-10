# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:44:09 2018

@author: Sagar Hossain
"""
"""
it takes a word then gives which parts of speech it is as a tuple as 
(word,nameOfpos)
"""

from xml.dom import minidom

nouns=[]
prons=[]
verbs=[]
adj=[]
adv=[]
conj=[]
def gettinNouns():
    xmldoc = minidom.parse('data/Noun.xml')
    itemlist = xmldoc.getElementsByTagName('noun')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinProns():
    xmldoc = minidom.parse('data/Pronoun.xml')
    itemlist = xmldoc.getElementsByTagName('pron')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinVerbs():
    xmldoc = minidom.parse('data/Verb.xml')
    itemlist = xmldoc.getElementsByTagName('verb')
    for s in itemlist:
        nouns.append(s.childNodes[0].nodeValue)
def gettinPosLen2():
    xmldoc = minidom.parse('data/L1_2.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen3():
    xmldoc = minidom.parse('data/L3.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen4():
    xmldoc = minidom.parse('data/L4.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen5():
    xmldoc = minidom.parse('data/L5.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen6():
    xmldoc = minidom.parse('data/L6.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen7():
    xmldoc = minidom.parse('data/L7.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen8():
    xmldoc = minidom.parse('data/L8.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen9():
    xmldoc = minidom.parse('data/L9.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen10():
    xmldoc = minidom.parse('data/L10.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen11():
    xmldoc = minidom.parse('data/L11.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen12():
    xmldoc = minidom.parse('data/L12.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen13():
    xmldoc = minidom.parse('data/L13.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen14():
    xmldoc = minidom.parse('data/L14.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen15():
    xmldoc = minidom.parse('data/L15.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen16():
    xmldoc = minidom.parse('data/L16.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen17():
    xmldoc = minidom.parse('data/L17.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen18():
    xmldoc = minidom.parse('data/L18.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen19():
    xmldoc = minidom.parse('data/L19.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
def gettinPosLen20():
    xmldoc = minidom.parse('data/L20.xml')
    itemlist1 = xmldoc.getElementsByTagName('noun')
    itemlist2 = xmldoc.getElementsByTagName('pron')
    itemlist3 = xmldoc.getElementsByTagName('adj')
    itemlist4 = xmldoc.getElementsByTagName('adv')
    itemlist5 = xmldoc.getElementsByTagName('verb')
    itemlist6 = xmldoc.getElementsByTagName('conj')
    for s in itemlist1:
        nouns.append(s.childNodes[0].nodeValue)
    for s in itemlist2:
        prons.append(s.childNodes[0].nodeValue)
    for s in itemlist3:
        adj.append(s.childNodes[0].nodeValue)
    for s in itemlist4:
        adv.append(s.childNodes[0].nodeValue)
    for s in itemlist5:
        verbs.append(s.childNodes[0].nodeValue)
    for s in itemlist6:
        conj.append(s.childNodes[0].nodeValue)
gettinNouns()
gettinPosLen2()
gettinPosLen3()
gettinPosLen4()
gettinPosLen5()
gettinPosLen6()
gettinPosLen7()
gettinPosLen8()
gettinPosLen9()
gettinPosLen10()
gettinPosLen11()
gettinPosLen12()
gettinPosLen13()
gettinPosLen14()
gettinPosLen15()
gettinPosLen16()
gettinPosLen17()
gettinPosLen18()
gettinPosLen19()
gettinPosLen20()
gettinProns()
gettinVerbs()
class pos:
    def posTagging(self, word):
        global prons,adj,adv,conj,verbs
        if word not in prons:
            if word not in adj:
                if word not in adv:
                    if word not in conj:
                        if word not in verbs:
                            return (word,"noun")
                        else:
                            return(word,"verb")
                    else:
                        return (word,"conj")
                else:
                    return (word,"adv")
            else:
                return (word,"adj")
        else:
            return (word,"pron")
        
a=pos()
print(a.posTagging('এবং'))
