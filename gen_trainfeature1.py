#coding=utf-8
import os
import pandas as pd
from datetime import date
from fe import *
import gc
def convert_day(x):
      try:
            y,m,d=x.split('-')
            return (date(int(y),int(m),int(d))-date(2013,4,14)).days 
      except:
            return -1
# the 'orderdate' of training data is between '2013-04-14(sunday)' to '2013-04-20(saturday)'
all_colname=['orderid','uid','orderdate','hotelid','basicroomid','roomid','star','rank','returnvalue','price_deduct','basic_minarea','basic_maxarea']

#nrows = 10000  #测试代码用
nrows = None
data=pd.read_csv('dataset/competition_train.txt',sep='\t',usecols=all_colname, nrows=nrows)
data.rename(columns={'rank':'rank1'},inplace=True)  # change name rank to rank1, to avoid key-name conflict

data.orderdate=data.orderdate.apply(convert_day)

#print data.shape
File_Name = "train_related_feature1.csv"

related_feature=get_feature(data)
related_feature=related_feature.drop(['uid','basicroomid'],axis=1)
#print related_feature.shape
#dataset=pd.merge(data,all_feature,on=['orderid','roomid'],how='left')
#del data,all_feature
#gc.collect()
related_feature.to_csv('data/'+File_Name,index=None)