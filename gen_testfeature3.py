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
# roomtag_6, roomtag6_lastord are invalid features
# delete  'orderbehavior_4_ratio_1month','orderbehavior_5_ratio_1month','orderbehavior_3_ratio_1month', all of them are null
# the 'orderdate' of training data is between '2013-04-14(sunday)' to '2013-04-20(saturday)'
all_colname=['returnvalue','price_deduct','basic_week_ordernum_ratio',	'basic_recent3_ordernum_ratio',\
            'basic_comment_ratio',	'basic_30days_ordnumratio',	'basic_30days_realratio',	'room_30days_ordnumratio',	'room_30days_realratio']

#nrows = 10000  #测试代码用
nrows = None
data1=pd.read_csv('dataset/competition_test.txt',sep='\t',usecols=all_colname, nrows=nrows)

data1['true_value']=data1.returnvalue+data1.price_deduct
#print data1.shape

data2=pd.read_csv('data/features6-18/test_newFeatures43.csv',nrows=nrows)


#print data2.shape

data1['minus_price_deduct_price_median']=data1.price_deduct- data2.price_deduct_basic_median
data1['minus_returnvalue_basic_median']=data1.returnvalue-data2.returnvalue_basic_median
data1['minus_true_value_basic_median']=data1.true_value-data2.true_value_basic_median

data1['minus_price_deduct_basic_std']=data1.price_deduct-data2.price_deduct_basic_std
data1['minus_returnvalue_basic_std']=data1.returnvalue-data2.returnvalue_basic_std
data1['minus_true_value_basic_std']=data1.true_value-data2.true_value_basic_std

data1['rate_price_deduct_basic_sum']=data1.price_deduct/data2.price_deduct_basic_sum
data1['rate_returnvalue_basic_sum']=data1.returnvalue/data2.returnvalue_basic_sum
data1['rate_true_value_basic_sum']=data1.true_value/data2.true_value_basic_sum

data1['minus_price_deduct_basic_min']=data1.price_deduct-data2.price_deduct_basic_min
data1['minus_returnvalue_basic_min']=data1.returnvalue-data2.returnvalue_basic_min
data1['minus_true_value_basic_min']=data1.true_value-data2.true_value_basic_min

data1['minus_price_deduct_basic_max']=data1.price_deduct-data2.price_deduct_basic_max
data1['minus_returnvalue_basic_max']=data1.returnvalue-data2.returnvalue_basic_max
data1['minus_true_value_basic_max']=data1.true_value-data2.true_value_basic_max

data1['minus_basic_week_ordernum_ratio_mean']=data1.basic_week_ordernum_ratio-data2.basic_week_ordernum_ratio_mean
data1['minus_basic_recent3_ordernum_ratio_mean']=data1.basic_recent3_ordernum_ratio-data2.basic_recent3_ordernum_ratio_mean
data1['minus_basic_comment_ratio_mean']=data1.basic_comment_ratio-data2.basic_comment_ratio_mean
data1['minus_basic_30days_ordnumratio_mean']=data1.basic_30days_ordnumratio-data2.basic_30days_ordnumratio_mean
data1['minus_basic_30days_realratio_mean']=data1.basic_30days_realratio-data2.basic_30days_realratio_mean

data1['minus_basic_week_ordernum_ratio_min']=data1.basic_week_ordernum_ratio-data2.basic_week_ordernum_ratio_min
data1['minus_basic_recent3_ordernum_ratio_min']=data1.basic_recent3_ordernum_ratio-data2.basic_recent3_ordernum_ratio_min
data1['minus_basic_comment_ratio_min']=data1.basic_comment_ratio-data2.basic_comment_ratio_min
data1['minus_basic_30days_ordnumratio_min']=data1.basic_30days_ordnumratio-data2.basic_30days_ordnumratio_min
data1['minus_basic_30days_realratio_min']=data1.basic_30days_realratio-data2.basic_30days_realratio_min

data1['minus_basic_week_ordernum_ratio_max']=data1.basic_week_ordernum_ratio-data2.basic_week_ordernum_ratio_max
data1['minus_basic_recent3_ordernum_ratio_max']=data1.basic_recent3_ordernum_ratio-data2.basic_recent3_ordernum_ratio_max
data1['minus_basic_comment_ratio_max']=data1.basic_comment_ratio-data2.basic_comment_ratio_max
data1['minus_basic_30days_ordnumratio_max']=data1.basic_30days_ordnumratio-data2.basic_30days_ordnumratio_max
data1['minus_basic_30days_realratio_max']=data1.basic_30days_realratio-data2.basic_30days_realratio_max

data1['minus_basic_week_ordernum_ratio_std']=data1.basic_week_ordernum_ratio-data2.basic_week_ordernum_ratio_std
data1['minus_basic_recent3_ordernum_ratio_std']=data1.basic_recent3_ordernum_ratio-data2.basic_recent3_ordernum_ratio_std
data1['minus_basic_comment_ratio_std']=data1.basic_comment_ratio-data2.basic_comment_ratio_std
data1['minus_basic_30days_ordnumratio_std']=data1.basic_30days_ordnumratio-data2.basic_30days_ordnumratio_std
data1['minus_basic_30days_realratio_std']=data1.basic_30days_realratio-data2.basic_30days_realratio_std

data1['minus_room_30days_ordnumratio_mean']=data1.room_30days_ordnumratio-data2.room_30days_ordnumratio_mean
data1['minus_room_30days_realratio_mean']=data1.room_30days_realratio-data2.room_30days_realratio_mean

data1['minus_room_30days_ordnumratio_min']=data1.room_30days_ordnumratio-data2.room_30days_ordnumratio_min
data1['minus_room_30days_realratio_min']=data1.room_30days_realratio-data2.room_30days_realratio_min

data1['minus_room_30days_ordnumratio_max']=data1.room_30days_ordnumratio-data2.room_30days_ordnumratio_max
data1['minus_room_30days_realratio_max']=data1.room_30days_realratio-data2.room_30days_realratio_max

data1['minus_room_30days_ordnumratio_std']=data1.room_30days_ordnumratio-data2.room_30days_ordnumratio_std
data1['minus_room_30days_realratio_std']=data1.room_30days_realratio-data2.room_30days_realratio_std

data1=data1.drop(all_colname,axis=1)
data1=data1.drop(['true_value'],axis=1)
#print data1.shape

File_Name = "test_feature_add3.csv"
data1.to_csv('data/'+File_Name,index=None)  