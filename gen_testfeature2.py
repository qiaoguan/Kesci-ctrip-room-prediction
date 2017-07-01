#coding=utf-8
import os
import pandas as pd
from datetime import date
from fe import *
import gc
def convert_day(x):
      try:
            y,m,d=x.split('-')
            return (date(int(y),int(m),int(d))-date(2013,4,21)).days 
      except:
            return -1
# the 'orderdate' of testing data is between '2013-04-21(sunday)' to '2013-04-27(saturday)'
# delete  'orderbehavior_4_ratio_1month','orderbehavior_5_ratio_1month','orderbehavior_3_ratio_1month', all of them are null

all_colname=['orderid','uid','orderdate','hotelid','basicroomid','roomid','star','rank','returnvalue','price_deduct','basic_minarea','basic_maxarea',\
            'roomservice_1','roomservice_2','roomservice_3','roomservice_4','roomservice_5','roomservice_6','roomservice_7','roomservice_8',\
            'roomtag_1','roomtag_2','roomtag_3','roomtag_4','roomtag_5','user_confirmtime','user_avgadvanceddate','user_avgstar','user_avggoldstar','user_avgrecommendlevel',\
            'user_avgroomnum','ordertype_1_ratio','ordertype_2_ratio','ordertype_3_ratio','ordertype_4_ratio','ordertype_5_ratio','ordertype_6_ratio','ordertype_7_ratio',\
            'ordertype_8_ratio','ordertype_9_ratio','ordertype_10_ratio','ordertype_11_ratio',\
            'user_avgdealpriceholiday','user_avgdealpriceworkday','user_avgdealprice','user_avgpromotion','user_avgprice_star',\
            'orderbehavior_1_ratio','orderbehavior_2_ratio','orderbehavior_3_ratio_1week','orderbehavior_4_ratio_1week','orderbehavior_5_ratio_1week',\
            'orderbehavior_3_ratio_3month','orderbehavior_4_ratio_3month',\
            'orderbehavior_5_ratio_3month','orderbehavior_6_ratio','orderbehavior_7_ratio','orderbehavior_8','orderbehavior_9',\
            'user_ordernum','user_activation','user_avgprice','user_maxprice','user_minprice','user_stdprice','user_cvprice','user_citynum','user_avgroomarea',\
            'user_roomservice_4_0ratio',	'user_roomservice_4_2ratio',	'user_roomservice_4_3ratio',	'user_roomservice_4_4ratio',	'user_roomservice_4_1ratio',\
            'user_roomservice_4_5ratio',  'user_roomservice_3_123ratio',	'user_roomservice_6_2ratio',	'user_roomservice_6_1ratio',	'user_roomservice_6_0ratio',\
            'user_roomservice_5_1ratio',	'user_roomservice_7_0ratio',	'user_roomservice_2_1ratio',	'user_roomservice_8_1ratio',	'user_rank_ratio',\
            'user_roomservice_5_345ratio',	'user_ordnum_1week',	'user_avgprice_1week',	'user_medprice_1week',	'user_minprice_1week',	'user_maxprice_1week',\
            'user_roomservice_3_123ratio_1week',	'user_roomservice_7_1ratio_1week',	'user_roomservice_7_0ratio_1week',	'user_roomservice_4_5ratio_1week',\
            'user_roomservice_4_4ratio_1week', 'user_roomservice_4_2ratio_1week',	'user_roomservice_4_3ratio_1week',	'user_roomservice_4_0ratio_1week',	'user_ordnum_1month',\
            'user_avgprice_1month',	'user_medprice_1month',	'user_minprice_1month',	'user_maxprice_1month',	'user_roomservice_3_123ratio_1month',\
            'user_roomservice_7_1ratio_1month',	'user_roomservice_7_0ratio_1month',	'user_roomservice_4_5ratio_1month',	'user_roomservice_4_4ratio_1month',\
            'user_roomservice_4_2ratio_1month',	'user_roomservice_4_3ratio_1month',	'user_roomservice_4_0ratio_1month',	'user_ordnum_3month',	'user_avgprice_3month',\
            'user_medprice_3month',	'user_minprice_3month',	'user_maxprice_3month',	'user_roomservice_3_123ratio_3month',	'user_roomservice_7_1ratio_3month',\
            'user_roomservice_7_0ratio_3month',	'user_roomservice_4_5ratio_3month',	'user_roomservice_4_4ratio_3month',	'user_roomservice_4_2ratio_3month',\
            'user_roomservice_4_3ratio_3month',	'user_roomservice_4_0ratio_3month',	'basic_week_ordernum_ratio',	'basic_recent3_ordernum_ratio',\
            'basic_comment_ratio',	'basic_30days_ordnumratio',	'basic_30days_realratio',	'room_30days_ordnumratio',	'room_30days_realratio',\
            'orderid_lastord',	'orderdate_lastord',	'hotelid_lastord',	'roomid_lastord',	'basicroomid_lastord',	'rank_lastord',	'return_lastord',	\
            'price_last_lastord',	'roomservice_2_lastord',	'roomservice_3_lastord',	'roomservice_4_lastord',	'roomservice_5_lastord',	'roomservice_6_lastord',\
            'roomservice_8_lastord',	'roomtag_2_lastord',	'roomtag_3_lastord',	'roomtag_4_lastord',	'roomtag_5_lastord',	'star_lastord',\
            'hotel_minprice_lastord',	'basic_minprice_lastord']

#nrows = 10000  #测试代码用
nrows = None
data=pd.read_csv('dataset/competition_test.txt',sep='\t',usecols=all_colname, nrows = nrows)
data.rename(columns={'rank':'rank1'},inplace=True)  # change name rank to rank1, to avoid key-name conflict

data.orderdate=data.orderdate.apply(convert_day)
data.orderdate_lastord=data.orderdate_lastord.apply(convert_day)

################ 2017/6/21 added               one roomservice may have several types
data['user_roomservice_4_1ratio_3month']=1-data.user_roomservice_4_0ratio_3month-data.user_roomservice_4_2ratio_3month-data.user_roomservice_4_3ratio_3month-\
                                          data.user_roomservice_4_4ratio_3month-data.user_roomservice_4_5ratio_3month

data['user_roomservice_4_1ratio_1month']=1-data.user_roomservice_4_0ratio_1month-data.user_roomservice_4_2ratio_1month-data.user_roomservice_4_3ratio_1month-\
                                          data.user_roomservice_4_4ratio_1month-data.user_roomservice_4_5ratio_1month

data['user_roomservice_4_1ratio_1week']=1-data.user_roomservice_4_0ratio_1week-data.user_roomservice_4_2ratio_1week-data.user_roomservice_4_3ratio_1week-\
                                         data.user_roomservice_4_4ratio_1week-data.user_roomservice_4_5ratio_1week
data['user_roomservice_3_other_ratio']=1-data.user_roomservice_3_123ratio
data['user_roomservice_6_other_ratio']=1-data.user_roomservice_6_0ratio-data.user_roomservice_6_1ratio-data.user_roomservice_6_2ratio
data['user_roomservice_5_other_ratio']=1-data.user_roomservice_5_1ratio
data['user_roomservice_7_other_ratio']=1-data.user_roomservice_7_0ratio
data['user_roomservice_2_other_ratio']=1-data.user_roomservice_2_1ratio
data['user_roomservice_8_2ratio']=1-data.user_roomservice_8_1ratio-data.user_roomservice_5_345ratio

data['user_price_deduct_user_maxprice_1week']=data.price_deduct-data.user_maxprice_1week
data['user_price_deduct_user_minprice_1week']=data.price_deduct-data.user_minprice_1week
data['user_price_deduct_user_maxprice_1month']=data.price_deduct-data.user_maxprice_1month
data['user_price_deduct_user_minprice_1month']=data.price_deduct-data.user_minprice_1month
data['user_price_deduct_user_maxprice_3month']=data.price_deduct-data.user_maxprice_3month
data['user_price_deduct_user_minprice_3month']=data.price_deduct-data.user_minprice_3month
data['price_deduct_diff_up2std']=data.price_deduct-data.user_avgprice+2*data.user_stdprice
data['price_deduct_diff_down2std']=data.price_deduct-data.user_avgprice-2*data.user_stdprice
#############



t=data[['orderid','basicroomid','roomid']].drop_duplicates()[['orderid','basicroomid']]     ##how many roomid in each (orderid,basicroomid)
t['basicroomid_roomid_cnt']=1
t=t.groupby(['orderid','basicroomid']).agg('sum').reset_index()
data=pd.merge(data,t,on=['orderid','basicroomid'],how='left')


#leak_order=pd.read_csv('data/leak_order.csv')
#data=data[~data.orderid.isin(leak_order.orderid)]   # fiter some leak order

data.user_avgadvanceddate=data.user_avgadvanceddate.apply(round).astype('int')#convert user_avgadvanceddata to int,so we can get real data(orderdate+adv_data)
data['is_holiday']=(((data.orderdate+data.user_avgadvanceddate)%7==0)|((data.orderdate+data.user_avgadvanceddate)%7==6))

data['order_hotel_is_same']=data.hotelid==data.hotelid_lastord    # added features

data.orderdate_lastord.replace(-1,np.nan,inplace=True)                    # calculate gap between orderdate and orderdate_lastord
data['orderdate_after_before_gap']=data.orderdate-data.orderdate_lastord
data.orderdate_lastord.replace(np.nan,-1,inplace=True)
data.orderdate_after_before_gap.replace(np.nan,-1,inplace=True)

# calculate gap between rank and rank_lastord
data['rank_this_last_gap']=data.rank1-data.rank_lastord

# calculate gap between returnvalue and return_lastord
data['returnvalue_this_last_gap']=data.returnvalue-data.return_lastord

#data.returnvalue_this_last_gap.replace(np.nan,-1,inplace=True)

# calculate gap between price_deduct and price_last_lastord
data['price_this_last_gap']=data.price_deduct-data.price_last_lastord

# calculate gap between price_deduct and user_avgprice      ,user_maxprice, user_minprice
data['this_price_last_avgprice_gap']=data.price_deduct-data.user_avgprice
data['this_price_last_maxprice_gap']=data.price_deduct-data.user_maxprice
data['this_price_last_minprice_gap']=data.price_deduct-data.user_minprice

data['basicroomid_roomid_price_rank']=data.groupby(['orderid','basicroomid'])['returnvalue'].rank(method='max')
data['basicroomid_roomid_price_ismin']=data['basicroomid_roomid_price_rank']==1

data['orderid_roomid_price_rank']=data.groupby(['orderid'])['returnvalue'].rank(method='max')
data['orderid_roomid_price_ismin']=data['orderid_roomid_price_rank']==1

data['basicroomid_roomid_rank1']=data.groupby(['orderid','basicroomid'])['rank1'].rank(method='max')
data['basicroomid_roomid_rank1_ismin']=data['basicroomid_roomid_price_rank']==1
data['basicroomid_roomid_rank1_rate']=data.basicroomid_roomid_rank1.astype('float')/data.basicroomid_roomid_cnt

########################## 2017/6/11 added
data['order_basicroomid_is_same']=data.basicroomid==data.basicroomid_lastord 
data['order_rank_is_same']=data.rank1==data.rank_lastord

data['order_roomservice_8_is_same']=data.roomservice_8==data.roomservice_8_lastord  # only user some roomservices which are more important
data['order_roomservice_4_is_same']=data.roomservice_4==data.roomservice_4_lastord
data['order_roomservice_3_is_same']=data.roomservice_3==data.roomservice_3_lastord
data['order_roomservice_6_is_same']=data.roomservice_6==data.roomservice_6_lastord

data['order_roomtag_3_is_same']=data.roomtag_3==data.roomtag_3_lastord  # only user some roomtags which are more important
#data['order_roomtag_1_is_same']=data.roomtag_1==data.roomtag_1_lastord  

data['order_star_is_same']=data.star==data.star_lastord

data['this_last_roomservice_2_gap']=data.roomservice_2-data.roomservice_2_lastord
data['this_last_roomservice_3_gap']=data.roomservice_3-data.roomservice_3_lastord
data['this_last_roomservice_4_gap']=data.roomservice_4-data.roomservice_4_lastord
data['this_last_roomservice_5_gap']=data.roomservice_5-data.roomservice_5_lastord
data['this_last_roomservice_6_gap']=data.roomservice_6-data.roomservice_6_lastord
data['this_last_roomservice_8_gap']=data.roomservice_8-data.roomservice_8_lastord
data['this_last_roomtag_4_gap']=data.roomtag_4-data.roomtag_4_lastord
data['this_last_roomtag_5_gap']=data.roomtag_5-data.roomtag_5_lastord

# calculate gap between user price and hotel price
data['user_maxprice_hotel_minprice_lastord_gap']=data.user_maxprice-data.hotel_minprice_lastord
data['user_maxprice_basic_minprice_lastord_gap']=data.user_maxprice-data.basic_minprice_lastord
data['user_minprice_hotel_minprice_lastord_gap']=data.user_minprice-data.hotel_minprice_lastord
data['user_minprice_basic_minprice_lastord_gap']=data.user_minprice-data.basic_minprice_lastord
data['user_stdprice_hotel_minprice_lastord_gap']=data.user_stdprice-data.hotel_minprice_lastord
data['user_stdprice_basic_minprice_lastord_gap']=data.user_stdprice-data.basic_minprice_lastord

#########################  2017/6/12 added
data['user_price_deduct_user_avgdealpriceholiday']=data.price_deduct-data.user_avgdealpriceholiday
data['user_price_deduct_user_avgdealpriceworkday']=data.price_deduct-data.user_avgdealpriceworkday
data['user_price_deduct_user_avgdealprice']=data.price_deduct-data.user_avgdealprice
data['user_price_deduct_user_avgprice_1week']=data.price_deduct-data.user_avgprice_1week
data['user_price_deduct_user_avgprice_1month']=data.price_deduct-data.user_avgprice_1month
data['user_price_deduct_user_avgprice_3month']=data.price_deduct-data.user_avgprice_3month

# 2017/6/14
data['per_area_value']=data.price_deduct*2/(data.basic_minarea+data.basic_maxarea)
data['per_area_returnvalue']=data.returnvalue*2/(data.basic_minarea+data.basic_maxarea)

#----------------------------------------------
data['star_diff']=data.star-data.user_avgstar
data['rank_diff']=data.rank1-data.user_rank_ratio
data['returnvalue_diff']=data.returnvalue-data.user_avgpromotion
#data['ismain_type_rs2']=data.
data['true_value']=data.returnvalue+data.price_deduct
data['day_of_week']=data.orderdate%7
data['dif_star']=data.star-data.user_avggoldstar
data['dif_recommendstar']=data.star-data.user_avgrecommendlevel
data['dif_price_deduct']=data.price_deduct-data.user_avgprice_star
data['dif_true_value']=data.true_value-data.user_avgdealprice
data['dif_basic_minarea']=data.basic_minarea-data.user_avgroomarea
data['dif_basic_maxarea']=data.basic_maxarea-data.user_avgroomarea
data['different_star']=data.star-data.star_lastord
data['diffferent_hotel_minprice']=data.price_deduct-data.hotel_minprice_lastord
data['different_basic_minprice']=data.price_deduct-data.basic_minprice_lastord

data['true_value_rank']=data.groupby(['orderid'])['true_value'].rank(method='max')
data['price_deduct_rank']=data.groupby(['orderid'])['price_deduct'].rank(method='max')
data['basic_minarea_rank']=data.groupby(['orderid'])['basic_minarea'].rank(method='max')
data['basic_maxarea_rank']=data.groupby(['orderid'])['basic_maxarea'].rank(method='max')


tt=data[(data.price_deduct_rank==1)][['orderid','price_deduct']]
tt.rename(columns={'price_deduct':'order_min_price'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')
data['price_over_min']=data.price_deduct-data.order_min_price
data=data.drop(['order_min_price'],axis=1)

data['true_value_basic_rank']=data.groupby(['orderid','basicroomid'])['true_value'].rank(method='max')
data['price_deduct_basic_rank']=data.groupby(['orderid','basicroomid'])['price_deduct'].rank(method='max')

tt=data.groupby('orderid')['price_deduct'].agg('median').reset_index()
tt.rename(columns={'price_deduct':'price_deduct_median'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['returnvalue'].agg('median').reset_index()
tt.rename(columns={'returnvalue':'returnvalue_median'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['true_value'].agg('median').reset_index()
tt.rename(columns={'true_value':'true_value_median'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['basic_minarea'].agg('median').reset_index()
tt.rename(columns={'basic_minarea':'basic_minarea_median'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['basic_maxarea'].agg('median').reset_index()
tt.rename(columns={'basic_maxarea':'basic_maxarea_median'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['price_deduct'].agg('std').reset_index()
tt.rename(columns={'price_deduct':'price_deduct_std'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['returnvalue'].agg('std').reset_index()
tt.rename(columns={'returnvalue':'returnvalue_std'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['true_value'].agg('std').reset_index()
tt.rename(columns={'true_value':'true_value_std'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['basic_minarea'].agg('std').reset_index()
tt.rename(columns={'basic_minarea':'basic_minarea_std'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

tt=data.groupby('orderid')['basic_maxarea'].agg('std').reset_index()
tt.rename(columns={'basic_maxarea':'basic_maxarea_std'},inplace=True)
data=pd.merge(data,tt,on='orderid',how='left')

data['price_deduct_std_rate']=data.price_deduct_std/data.price_deduct_median
data['returnvalue_std_rate']=data.returnvalue_std/data.returnvalue_median
data['true_value_std_rate']=data.true_value_std/data.true_value_median
data['basic_minarea_std_rate']=data.basic_minarea_std/data.basic_minarea_median
data['basic_maxarea_std_rate']=data.basic_maxarea_std/data.basic_maxarea_median

File_Name = "test_feature1.csv"

#print data.shape
data.to_csv('data/'+File_Name,index=None)