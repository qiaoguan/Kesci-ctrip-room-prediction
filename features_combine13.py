import pandas as pd

#nrows = 10000  #测试代码用
nrows = None
train = pd.read_csv('dataset/competition_train.txt',sep='\t',nrows=nrows,usecols=['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                                                                            'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'])
group = train[['basicroomid','orderdate','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio']].groupby(['basicroomid','orderdate']).mean()
grouped = group.reset_index().groupby('basicroomid')
grouped_mean = grouped.mean().reset_index()
grouped_mean.columns = grouped_mean.columns.map(lambda x: x+'_mean' if x!='basicroomid' else x)
grouped_min = grouped.min().reset_index()
grouped_min.columns = grouped_min.columns.map(lambda x: x+'_min' if x!='basicroomid' else x)
grouped_max = grouped.max().reset_index()
grouped_max.columns = grouped_max.columns.map(lambda x: x+'_max' if x!='basicroomid' else x)
grouped_std = grouped.std().reset_index()
grouped_std.columns = grouped_std.columns.map(lambda x: x+'_std' if x!='basicroomid' else x)
group2 = train[['roomid','orderdate','room_30days_ordnumratio','room_30days_realratio']].groupby(['roomid','orderdate']).mean()
group2ed = group2.reset_index().groupby('roomid')
group2ed_mean = group2ed.mean().reset_index()
group2ed_mean.columns = group2ed_mean.columns.map(lambda x: x+'_mean' if x!='roomid' else x)
group2ed_min = group2ed.min().reset_index()
group2ed_min.columns = group2ed_min.columns.map(lambda x: x+'_min' if x!='roomid' else x)
group2ed_max = group2ed.max().reset_index()
group2ed_max.columns = group2ed_max.columns.map(lambda x: x+'_max' if x!='roomid' else x)
group2ed_std = group2ed.std().reset_index()
group2ed_std.columns = group2ed_std.columns.map(lambda x: x+'_std' if x!='roomid' else x)

train.drop(['orderdate','hotelid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio','basic_comment_ratio',
            'basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'],axis=1,inplace=True)
train = pd.merge(train,grouped_mean,how='left',on='basicroomid')
train = pd.merge(train,grouped_min,how='left',on='basicroomid')
train = pd.merge(train,grouped_max,how='left',on='basicroomid')
train = pd.merge(train,grouped_std,how='left',on='basicroomid')
train = pd.merge(train,group2ed_mean,how='left',on='roomid')
train = pd.merge(train,group2ed_min,how='left',on='roomid')
train = pd.merge(train,group2ed_max,how='left',on='roomid')
train = pd.merge(train,group2ed_std,how='left',on='roomid')

col = ['basic_week_ordernum_ratio_mean','basic_recent3_ordernum_ratio_mean','basic_comment_ratio_mean','basic_30days_ordnumratio_mean',
       'basic_30days_realratio_mean','basic_week_ordernum_ratio_min','basic_recent3_ordernum_ratio_min', 'basic_comment_ratio_min',
       'basic_30days_ordnumratio_min','basic_30days_realratio_min','basic_week_ordernum_ratio_max','basic_recent3_ordernum_ratio_max',
       'basic_comment_ratio_max','basic_30days_ordnumratio_max', 'basic_30days_realratio_max','basic_week_ordernum_ratio_std',
       'basic_recent3_ordernum_ratio_std','basic_comment_ratio_std', 'basic_30days_ordnumratio_std','basic_30days_realratio_std',
       'room_30days_ordnumratio_mean','room_30days_realratio_mean','room_30days_ordnumratio_min', 'room_30days_realratio_min',
       'room_30days_ordnumratio_max','room_30days_realratio_max', 'room_30days_ordnumratio_std','room_30days_realratio_std']

train[col].to_csv('data/add_train13.csv',index=False)


##############################################################################################################
test = pd.read_csv('dataset/competition_test.txt',sep='\t',nrows=nrows,usecols=['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                                                                            'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'])
group = test[['basicroomid','orderdate','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio']].groupby(['basicroomid','orderdate']).mean()
grouped = group.reset_index().groupby('basicroomid')
grouped_mean = grouped.mean().reset_index()
grouped_mean.columns = grouped_mean.columns.map(lambda x: x+'_mean' if x!='basicroomid' else x)
grouped_min = grouped.min().reset_index()
grouped_min.columns = grouped_min.columns.map(lambda x: x+'_min' if x!='basicroomid' else x)
grouped_max = grouped.max().reset_index()
grouped_max.columns = grouped_max.columns.map(lambda x: x+'_max' if x!='basicroomid' else x)
grouped_std = grouped.std().reset_index()
grouped_std.columns = grouped_std.columns.map(lambda x: x+'_std' if x!='basicroomid' else x)
group2 = test[['roomid','orderdate','room_30days_ordnumratio','room_30days_realratio']].groupby(['roomid','orderdate']).mean()
group2ed = group2.reset_index().groupby('roomid')
group2ed_mean = group2ed.mean().reset_index()
group2ed_mean.columns = group2ed_mean.columns.map(lambda x: x+'_mean' if x!='roomid' else x)
group2ed_min = group2ed.min().reset_index()
group2ed_min.columns = group2ed_min.columns.map(lambda x: x+'_min' if x!='roomid' else x)
group2ed_max = group2ed.max().reset_index()
group2ed_max.columns = group2ed_max.columns.map(lambda x: x+'_max' if x!='roomid' else x)
group2ed_std = group2ed.std().reset_index()
group2ed_std.columns = group2ed_std.columns.map(lambda x: x+'_std' if x!='roomid' else x)

test.drop(['orderdate','hotelid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio','basic_comment_ratio',
            'basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'],axis=1,inplace=True)
test = pd.merge(test,grouped_mean,how='left',on='basicroomid')
test = pd.merge(test,grouped_min,how='left',on='basicroomid')
test = pd.merge(test,grouped_max,how='left',on='basicroomid')
test = pd.merge(test,grouped_std,how='left',on='basicroomid')
test = pd.merge(test,group2ed_mean,how='left',on='roomid')
test = pd.merge(test,group2ed_min,how='left',on='roomid')
test = pd.merge(test,group2ed_max,how='left',on='roomid')
test = pd.merge(test,group2ed_std,how='left',on='roomid')

col = ['basic_week_ordernum_ratio_mean','basic_recent3_ordernum_ratio_mean','basic_comment_ratio_mean','basic_30days_ordnumratio_mean',
       'basic_30days_realratio_mean','basic_week_ordernum_ratio_min','basic_recent3_ordernum_ratio_min', 'basic_comment_ratio_min',
       'basic_30days_ordnumratio_min','basic_30days_realratio_min','basic_week_ordernum_ratio_max','basic_recent3_ordernum_ratio_max',
       'basic_comment_ratio_max','basic_30days_ordnumratio_max', 'basic_30days_realratio_max','basic_week_ordernum_ratio_std',
       'basic_recent3_ordernum_ratio_std','basic_comment_ratio_std', 'basic_30days_ordnumratio_std','basic_30days_realratio_std',
       'room_30days_ordnumratio_mean','room_30days_realratio_mean','room_30days_ordnumratio_min', 'room_30days_realratio_min',
       'room_30days_ordnumratio_max','room_30days_realratio_max', 'room_30days_ordnumratio_std','room_30days_realratio_std']

test[col].to_csv('data/add_test13.csv',index=False)

#'''
#train = pd.read_csv('../csv/new_train12.csv',nrows=None)
#addtrain = pd.read_csv('../csv/add_train13.csv',nrows=None,usecols=['basic_week_ordernum_ratio_mean','basic_recent3_ordernum_ratio_mean','basic_comment_ratio_mean','basic_30days_ordnumratio_mean',
#                                                                    'basic_30days_realratio_mean','basic_week_ordernum_ratio_min','basic_recent3_ordernum_ratio_min', 'basic_comment_ratio_min',
#                                                                    'basic_30days_ordnumratio_min','basic_30days_realratio_min','basic_week_ordernum_ratio_max','basic_recent3_ordernum_ratio_max',
#                                                                    'basic_comment_ratio_max','basic_30days_ordnumratio_max', 'basic_30days_realratio_max','basic_week_ordernum_ratio_std',
#                                                                    'basic_recent3_ordernum_ratio_std','basic_comment_ratio_std', 'basic_30days_ordnumratio_std','basic_30days_realratio_std',
#                                                                    'room_30days_ordnumratio_mean','room_30days_realratio_mean','room_30days_ordnumratio_min', 'room_30days_realratio_min',
#                                                                    'room_30days_ordnumratio_max','room_30days_realratio_max', 'room_30days_ordnumratio_std','room_30days_realratio_std'])
#train = pd.concat([train,addtrain],axis=1)
#train.to_csv('../csv/new_train13.csv',index=False)
#
#'''
#test = pd.read_csv('../csv/new_test12.csv',nrows=None)
#addtest = pd.read_csv('../csv/add_test13.csv',nrows=None,usecols=['basic_week_ordernum_ratio_mean','basic_recent3_ordernum_ratio_mean','basic_comment_ratio_mean','basic_30days_ordnumratio_mean',
#                                                                    'basic_30days_realratio_mean','basic_week_ordernum_ratio_min','basic_recent3_ordernum_ratio_min', 'basic_comment_ratio_min',
#                                                                    'basic_30days_ordnumratio_min','basic_30days_realratio_min','basic_week_ordernum_ratio_max','basic_recent3_ordernum_ratio_max',
#                                                                    'basic_comment_ratio_max','basic_30days_ordnumratio_max', 'basic_30days_realratio_max','basic_week_ordernum_ratio_std',
#                                                                    'basic_recent3_ordernum_ratio_std','basic_comment_ratio_std', 'basic_30days_ordnumratio_std','basic_30days_realratio_std',
#                                                                    'room_30days_ordnumratio_mean','room_30days_realratio_mean','room_30days_ordnumratio_min', 'room_30days_realratio_min',
#                                                                    'room_30days_ordnumratio_max','room_30days_realratio_max', 'room_30days_ordnumratio_std','room_30days_realratio_std'])
#test = pd.concat([test,addtest],axis=1)
#test.to_csv('../csv/new_test13.csv',index=False)

