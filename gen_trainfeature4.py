#coding=utf-8
import pandas as pd

all_colname=['orderid','basicroomid','returnvalue','price_deduct','basic_week_ordernum_ratio',	'basic_recent3_ordernum_ratio',\
            'basic_comment_ratio',	'basic_30days_ordnumratio',	'basic_30days_realratio',	'room_30days_ordnumratio',	'room_30days_realratio',\
            'user_roomservice_4_0ratio', 'user_roomservice_4_1ratio', 'user_roomservice_4_2ratio','user_roomservice_4_3ratio', 'user_roomservice_4_4ratio',\
            'user_roomservice_4_5ratio','user_roomservice_4_0ratio_1week', 'user_roomservice_4_2ratio_1week',\
            'user_roomservice_4_3ratio_1week', 'user_roomservice_4_4ratio_1week',  'user_roomservice_4_5ratio_1week',\
            'user_roomservice_4_0ratio_1month', 'user_roomservice_4_2ratio_1month',\
            'user_roomservice_4_3ratio_1month', 'user_roomservice_4_4ratio_1month',  'user_roomservice_4_5ratio_1month',\
            'user_roomservice_4_0ratio_3month',  'user_roomservice_4_2ratio_3month',\
            'user_roomservice_4_3ratio_3month', 'user_roomservice_4_4ratio_3month',  'user_roomservice_4_5ratio_3month',\
            'user_avgprice_1week',	'user_medprice_1week',	'user_minprice_1week',	'user_maxprice_1week',\
            'user_avgprice_1month',	'user_medprice_1month',	'user_minprice_1month',	'user_maxprice_1month',\
            'user_avgprice_3month','user_medprice_3month',	'user_minprice_3month',	'user_maxprice_3month','user_avgprice','user_stdprice']

#nrows = 10000  #测试代码用
nrows = None
train=pd.read_csv('dataset/competition_train.txt',sep='\t',usecols=all_colname, nrows=nrows)

train['discount_ratio'] = 1.0 * train['returnvalue'] / train['price_deduct']
train['discount_ratio_rank'] = train.groupby('orderid')['discount_ratio'].rank(method='max') 

train['user_roomservice_4_1ratio_3month']=1 - train.user_roomservice_4_0ratio_3month - train.user_roomservice_4_2ratio_3month \
                - train.user_roomservice_4_3ratio_3month - train.user_roomservice_4_4ratio_3month - train.user_roomservice_4_5ratio_3month

train['user_roomservice_4_1ratio_1month']=1-train.user_roomservice_4_0ratio_1month-train.user_roomservice_4_2ratio_1month\
                -train.user_roomservice_4_3ratio_1month-train.user_roomservice_4_4ratio_1month-train.user_roomservice_4_5ratio_1month

train['user_roomservice_4_1ratio_1week'] =1-train.user_roomservice_4_0ratio_1week -train.user_roomservice_4_2ratio_1week\
                -train.user_roomservice_4_3ratio_1week -train.user_roomservice_4_4ratio_1week -train.user_roomservice_4_5ratio_1week

train['user_roomservice_4_max'] = train[["user_roomservice_4_0ratio", "user_roomservice_4_1ratio", "user_roomservice_4_2ratio",\
                                    "user_roomservice_4_3ratio", "user_roomservice_4_4ratio",  "user_roomservice_4_5ratio"]].max(axis=1)

train['user_roomservice_4_max_1week'] = train[["user_roomservice_4_0ratio_1week", "user_roomservice_4_1ratio_1week", "user_roomservice_4_2ratio_1week",\
                        "user_roomservice_4_3ratio_1week", "user_roomservice_4_4ratio_1week",  "user_roomservice_4_5ratio_1week"]].max(axis=1)

train['user_roomservice_4_max_1month'] = train[["user_roomservice_4_0ratio_1month", "user_roomservice_4_1ratio_1month", "user_roomservice_4_2ratio_1month",\
                         "user_roomservice_4_3ratio_1month", "user_roomservice_4_4ratio_1month",  "user_roomservice_4_5ratio_1month"]].max(axis=1)

train['user_roomservice_4_max_3month'] = train[["user_roomservice_4_0ratio_3month", "user_roomservice_4_1ratio_3month", "user_roomservice_4_2ratio_3month",\
                        "user_roomservice_4_3ratio_3month", "user_roomservice_4_4ratio_3month",  "user_roomservice_4_5ratio_3month"]].max(axis=1)



group = train[['orderid','price_deduct','returnvalue','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio','basic_comment_ratio',
               'basic_30days_ordnumratio','basic_30days_realratio']].groupby('orderid')

group_min = group.min().reset_index()
group_min.columns = group_min.columns.map(lambda x: 'min_'+x if x!='orderid' else x)

group_max = group.max().reset_index()
group_max.columns = group_max.columns.map(lambda x: 'max_'+x if x!='orderid' else x)


group2 = train[['orderid','basicroomid','room_30days_ordnumratio','room_30days_realratio']].groupby(['orderid','basicroomid'])

group2_min = group2.min().reset_index().rename(columns={'room_30days_ordnumratio':'min_room_30days_ordnumratio','room_30days_realratio':'min_room_30days_realratio'})
group2_max = group2.max().reset_index().rename(columns={'room_30days_ordnumratio':'max_room_30days_ordnumratio','room_30days_realratio':'max_room_30days_realratio'})

train = pd.merge(train,group_min,how='left',on='orderid')
train = pd.merge(train,group_max,how='left',on='orderid')
train = pd.merge(train,group2_min,how='left',on=['orderid','basicroomid'])
train = pd.merge(train,group2_max,how='left',on=['orderid','basicroomid'])

train['price_diff_order_min'] = train['price_deduct']-train['min_price_deduct']
train['price_diff_user_avg_1week'] = train['price_deduct']-train['user_avgprice_1week']
train['price_diff_user_max_1week'] = train['price_deduct']-train['user_maxprice_1week']
train['price_diff_user_min_1week'] = train['price_deduct']-train['user_minprice_1week']
train['price_diff_user_med_1week'] = train['price_deduct']-train['user_medprice_1week']
train['price_diff_user_avg_1month'] = train['price_deduct']-train['user_avgprice_1month']
train['price_diff_user_max_1month'] = train['price_deduct']-train['user_maxprice_1month']
train['price_diff_user_min_1month'] = train['price_deduct']-train['user_minprice_1month']
train['price_diff_user_med_1month'] = train['price_deduct']-train['user_medprice_1month']
train['price_diff_user_avg_3month'] = train['price_deduct']-train['user_avgprice_3month']
train['price_diff_user_max_3month'] = train['price_deduct']-train['user_maxprice_3month']
train['price_diff_user_min_3month'] = train['price_deduct']-train['user_minprice_3month']
train['price_diff_user_med_3month'] = train['price_deduct']-train['user_medprice_3month']

train['price_diff_user_up2std'] = train['price_deduct']-train['user_avgprice']-2*train['user_stdprice']
train['price_diff_user_down2std'] = train['price_deduct']-train['user_avgprice']+2*train['user_stdprice']


train=train.drop(all_colname,axis=1)
train=train.drop(['user_roomservice_4_1ratio_3month','user_roomservice_4_1ratio_1month','user_roomservice_4_1ratio_1week'],axis=1)
#print train.shape

File_Name = "train_feature_add4_1.csv"
train.to_csv('data/newfeature-6-22/'+File_Name,index=None)