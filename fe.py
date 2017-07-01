import numpy as np
import pandas as pd
from datetime import date

def get_feature(data):

    all_feature=data[['orderid','uid','basicroomid','roomid']].drop_duplicates()
    user_feature=get_user_feature(data)
    basicroom_feature=get_basicroom_feature(data)
    all_feature=pd.merge(all_feature,user_feature,on='uid',how='left')
    all_feature=pd.merge(all_feature,basicroom_feature,on='basicroomid',how='left')
    return all_feature

## user related features
def get_user_feature(data):  

    t5=data[['uid','basicroomid']].drop_duplicates()[['uid']]
    t5['user_unique_basicroomid_cnt']=1
    t5=t5.groupby(['uid']).agg('sum').reset_index()

    t6=data[['uid','roomid']].drop_duplicates()[['uid']]
    t6['user_unique_roomid_cnt']=1
    t6=t6.groupby(['uid']).agg('sum').reset_index()

    t9=data[['orderid','uid','basicroomid']].drop_duplicates()[['uid']]
    t9['user_unique_orderid_basicroomid_cnt']=1
    t9=t9.groupby(['uid']).agg('sum').reset_index()

    t10=data[['orderid','uid','roomid']].drop_duplicates()[['uid']]
    t10['user_unique_orderid_roomid_cnt']=1
    t10=t10.groupby(['uid']).agg('sum').reset_index()

    t10_1=data[['orderid','uid','basicroomid','roomid']].drop_duplicates()[['uid']]
    t10_1['user_unique_orderid_basicroomid_roomid_cnt']=1
    t10_1=t10_1.groupby(['uid']).agg('sum').reset_index()

    #user avg star,    avg_rank(maybe not useful),  avg_returnvalue, avg_price_deduct, avg_basic_minarea,  avg_basic_maxarea, avg_area
    t11=data[['uid','star']]
    t11.star=t11.star.astype('str')
    t11=t11.groupby(['uid'])['star'].agg(lambda x:':'.join(x)).reset_index()
    t11['len']=t11.star.apply(lambda s:len(s.split(':')))
    t11['user_avg_star']=t11.star.apply(lambda s:sum(int(d) for d in s.split(':'))).astype('float')/t11.len
    t11=t11[['uid','user_avg_star']]
    
    t12=data[['uid','rank1']]
 #   t12.rename(columns={'rank':'room_rank'},inplace=True)
    t12.rank1=t12.rank1.astype('str')
    t12=t12.groupby(['uid'])['rank1'].agg(lambda x:':'.join(x)).reset_index()
    t12['len']=t12.rank1.apply(lambda s:len(s.split(':')))
    t12['user_avg_rank1']=t12.rank1.apply(lambda s:sum(int(d) for d in s.split(':'))).astype('float')/t12.len
    t12=t12[['uid','user_avg_rank1']]
    
    t13=data[['uid','returnvalue']]
    t13.returnvalue=t13.returnvalue.astype('str')
    t13=t13.groupby(['uid'])['returnvalue'].agg(lambda x:':'.join(x)).reset_index()
    t13['len']=t13.returnvalue.apply(lambda s:len(s.split(':')))
    t13['user_avg_returnvalue']=t13.returnvalue.apply(lambda s:sum(float(d) for d in s.split(':')))/t13.len
    t13=t13[['uid','user_avg_returnvalue']]

    t14=data[['uid','price_deduct']]
    t14.price_deduct=t14.price_deduct.astype('str')
    t14=t14.groupby(['uid'])['price_deduct'].agg(lambda x:':'.join(x)).reset_index()
    t14['len']=t14.price_deduct.apply(lambda s:len(s.split(':')))
    t14['user_avg_price_deduct']=t14.price_deduct.apply(lambda s:sum(float(d) for d in s.split(':')))/t14.len
    t14=t14[['uid','user_avg_price_deduct']]

    t15=data[['uid','basic_minarea']]
    t15.basic_minarea=t15.basic_minarea.astype('str')
    t15=t15.groupby(['uid'])['basic_minarea'].agg(lambda x:':'.join(x)).reset_index()
    t15['len']=t15.basic_minarea.apply(lambda s:len(s.split(':')))
    t15['user_avg_basic_minarea']=t15.basic_minarea.apply(lambda s:sum(float(d) for d in s.split(':')))/t15.len
    t15=t15[['uid','user_avg_basic_minarea']]

    t16=data[['uid','basic_maxarea']]
    t16.basic_maxarea=t16.basic_maxarea.astype('str')
    t16=t16.groupby(['uid'])['basic_maxarea'].agg(lambda x:':'.join(x)).reset_index()
    t16['len']=t16.basic_maxarea.apply(lambda s:len(s.split(':')))
    t16['user_avg_basic_maxarea']=t16.basic_maxarea.apply(lambda s:sum(float(d) for d in s.split(':')))/t16.len
    t16=t16[['uid','user_avg_basic_maxarea']]
    
    user_feature = pd.merge(t5,t6,on='uid')

    user_feature = pd.merge(user_feature,t9,on='uid')
    user_feature = pd.merge(user_feature,t10,on='uid')
    user_feature = pd.merge(user_feature,t10_1,on='uid')
    user_feature = pd.merge(user_feature,t11,on='uid')
    user_feature = pd.merge(user_feature,t12,on='uid')
    user_feature = pd.merge(user_feature,t13,on='uid')
    user_feature = pd.merge(user_feature,t14,on='uid')
    user_feature = pd.merge(user_feature,t15,on='uid')
    user_feature = pd.merge(user_feature,t16,on='uid')
    user_feature['user_basic_avearea']=(user_feature.user_avg_basic_minarea+user_feature.user_avg_basic_maxarea)/2
    return user_feature

#basic room related features
def get_basicroom_feature(data):
    
    t1=data[['orderid','basicroomid']].drop_duplicates()[['basicroomid']]
    t1['basicroomid_unique_order_cnt']=1
    t1=t1.groupby(['basicroomid']).agg('sum').reset_index()

    t2=data[['orderdate','basicroomid']].drop_duplicates()[['basicroomid']]
    t2['basicroomid_unique_orderdate_cnt']=1
    t2=t2.groupby(['basicroomid']).agg('sum').reset_index()

    t3=data[['uid','basicroomid']].drop_duplicates()[['basicroomid']]
    t3['basicroomid_unique_user_cnt']=1
    t3=t3.groupby(['basicroomid']).agg('sum').reset_index()

    t4=data[['basicroomid','roomid']].drop_duplicates()[['basicroomid']]
    t4['basicroomid_unique_roomid_cnt']=1
    t4=t4.groupby(['basicroomid']).agg('sum').reset_index()

#    basicroom_feature=pd.merge(t,t1,on='basicroomid')
    basicroom_feature=pd.merge(t1,t2,on='basicroomid')
    basicroom_feature=pd.merge(basicroom_feature,t3,on='basicroomid')
    basicroom_feature=pd.merge(basicroom_feature,t4,on='basicroomid')
    return basicroom_feature