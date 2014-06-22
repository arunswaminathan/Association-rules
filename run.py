'''
Created on Apr 26, 2014
@author: AjaySivaSantoshReddy/ArunSwaminathan
'''

from __future__ import division
import csv
import sys
from collections import defaultdict
from itertools import  chain,combinations
import operator

global sup
sup=sys.argv[2]
con=sys.argv[3]
print "**********************************"
print "Support value received: " + sup
print "Confidence value received: "+ con
print "**********************************"
print " "


def read_csv():
    tran_list=[]
    item_list=set()
    cr = csv.reader(open("result.csv","r"))
    for r in cr:
        tran_list.append(frozenset(r))
        for item in r:
            item_list.add(frozenset([item]))
            
    return item_list,tran_list

def min_sup(itemlist,transet,freq_itemset):  
    
    
    freq_list=defaultdict(int)
    freq_set=set()
    
    for i in itemlist:
        for tran in transet:
            if (i.issubset(tran)):
                freq_list[i] += 1
                freq_itemset[i] += 1
    for i in itemlist:
        count=(freq_list[i]/len(transet))
        if(count>float(sup)):
            freq_set.add(i)
    return freq_set

def get_subset(sub_list,k):
    llist=(map(frozenset,combinations(sub_list, k)))
    return llist

def apriori():
    itemlist=[]
    transet=set()
    new_itemlist=set()
    freq_itemset=defaultdict(int)
    final_itemset=dict()
    itemlist,transet=read_csv()
    new_itemlist=min_sup(itemlist,transet,freq_itemset)  
    returneditemlist=new_itemlist
    itr=2
    while(returneditemlist != set([])):
        f_list=[]
        final_itemset[itr-1]=new_itemlist
        for i in new_itemlist:
            for j in i:
                if j not in f_list:
                    f_list.append(j)
        itrlist=get_subset(f_list,itr)
        new_itemlist=min_sup(itrlist,transet,freq_itemset)
        returneditemlist=new_itemlist
        itr=itr+1
    print_results(final_itemset,freq_itemset,len(transet))
    

def print_results(final_itemset,freq_itemset,tran_len):
    print_conf=dict()
    print_conf_supp=dict()
    print_dic=dict()
    for key, value in final_itemset.items():
        for i in value:
            supp=int((freq_itemset[i]/tran_len)*100)
            print_dic[i]=supp
    sorted_x = sorted(print_dic.iteritems(), key=operator.itemgetter(1), reverse=True)
    #print print_dic ['']
    for key,value in sorted_x:
        print"["+",".join( str(x) for x in key)+"], "+str(value)+"%" #write to file
        
    print " "
    print "*******High Confidence Association Rules******"
    print " "
    for key,value in final_itemset.items()[1:]:
        for i in value:
            sub = chain.from_iterable((combinations(i, r) for r in range(len(i)+1)))
            print_supp = print_dic[i]
            for x in sub:
                if(x!=()):
                    balance=i.difference(x)
                else:
                    continue           
                if(len(balance)>0 and len(balance)<2):
                    conf=int((freq_itemset[i]/freq_itemset[frozenset(x)])*100)
                    if(conf>int(float(con)*100)):
                        print_conf["[" + str(x[0])+"] -->["+"".join(str(k) + "," for k in balance)+"]"]= int(conf)
                        print_conf_supp["[" + str(x[0])+"] -->["+"".join(str(k) + "," for k in balance)+"]"]= int(print_supp)
                        
                        #print "[" + str(x[0])+"] -->["+"".join(str(k) + "," for k in balance)+"] (Conf: "+str(conf) +"%, Supp: " +str(print_supp) +"%)"

    sorted_print_conf = sorted(print_conf.iteritems(), key=operator.itemgetter(1), reverse=True)

    for key, value in sorted_print_conf:
        print key + "(Conf: " + str(value) + "%, Supp: " + str(print_conf_supp[key]) + "%)";


apriori()
    