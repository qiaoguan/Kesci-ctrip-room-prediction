import pandas as pd

#nrows = 10000  #测试代码用
nrows = None
train = pd.read_csv('dataset/competition_train.txt',sep='\t',nrows=nrows,usecols=['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                                                                            'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'])
group = train[['basicroomid','orderdate','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio']].groupby(['basicroomid','orderdate']).mean()
grouped = group.reset_index().groupby('basicroomid')
grouped_sum = grouped.sum().reset_index()
grouped_sum.columns = grouped_sum.columns.map(lambda x: x+'_sum' if x!='basicroomid' else x)
grouped_median = grouped.median().reset_index()
grouped_median.columns = grouped_median.columns.map(lambda x: x+'_median' if x!='basicroomid' else x)
grouped_mad = grouped.mad().reset_index()
grouped_mad.columns = grouped_mad.columns.map(lambda x: x+'_mad' if x!='basicroomid' else x)
grouped_var = grouped.var().reset_index()
grouped_var.columns = grouped_var.columns.map(lambda x: x+'_var' if x!='basicroomid' else x)
group2 = train[['roomid','orderdate','room_30days_ordnumratio','room_30days_realratio']].groupby(['roomid','orderdate']).mean()
group2ed = group2.reset_index().groupby('roomid')
group2ed_sum = group2ed.sum().reset_index()
group2ed_sum.columns = group2ed_sum.columns.map(lambda x: x+'_sum' if x!='roomid' else x)
group2ed_median = group2ed.median().reset_index()
group2ed_median.columns = group2ed_median.columns.map(lambda x: x+'_median' if x!='roomid' else x)
group2ed_mad = group2ed.mad().reset_index()
group2ed_mad.columns = group2ed_mad.columns.map(lambda x: x+'_mad' if x!='roomid' else x)
group2ed_var = group2ed.var().reset_index()
group2ed_var.columns = group2ed_var.columns.map(lambda x: x+'_var' if x!='roomid' else x)

train = pd.merge(train,grouped_sum,how='left',on='basicroomid')
train = pd.merge(train,grouped_median,how='left',on='basicroomid')
train = pd.merge(train,grouped_mad,how='left',on='basicroomid')
train = pd.merge(train,grouped_var,how='left',on='basicroomid')
train = pd.merge(train,group2ed_sum,how='left',on='roomid')
train = pd.merge(train,group2ed_median,how='left',on='roomid')
train = pd.merge(train,group2ed_mad,how='left',on='roomid')
train = pd.merge(train,group2ed_var,how='left',on='roomid')

train.drop(['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio','basic_comment_ratio',
            'basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'],axis=1,inplace=True)
#print train.shape
train.to_csv('data/newfeature-5/add_train5.csv',index=False)


##################################################################################
test = pd.read_csv('dataset/competition_test.txt',sep='\t',nrows=nrows,usecols=['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                                                                            'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'])
group = test[['basicroomid','orderdate','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio',
                'basic_comment_ratio','basic_30days_ordnumratio','basic_30days_realratio']].groupby(['basicroomid','orderdate']).mean()
grouped = group.reset_index().groupby('basicroomid')
grouped_sum = grouped.sum().reset_index()
grouped_sum.columns = grouped_sum.columns.map(lambda x: x+'_sum' if x!='basicroomid' else x)
grouped_median = grouped.median().reset_index()
grouped_median.columns = grouped_median.columns.map(lambda x: x+'_median' if x!='basicroomid' else x)
grouped_mad = grouped.mad().reset_index()
grouped_mad.columns = grouped_mad.columns.map(lambda x: x+'_mad' if x!='basicroomid' else x)
grouped_var = grouped.var().reset_index()
grouped_var.columns = grouped_var.columns.map(lambda x: x+'_var' if x!='basicroomid' else x)
group2 = test[['roomid','orderdate','room_30days_ordnumratio','room_30days_realratio']].groupby(['roomid','orderdate']).mean()
group2ed = group2.reset_index().groupby('roomid')
group2ed_sum = group2ed.sum().reset_index()
group2ed_sum.columns = group2ed_sum.columns.map(lambda x: x+'_sum' if x!='roomid' else x)
group2ed_median = group2ed.median().reset_index()
group2ed_median.columns = group2ed_median.columns.map(lambda x: x+'_median' if x!='roomid' else x)
group2ed_mad = group2ed.mad().reset_index()
group2ed_mad.columns = group2ed_mad.columns.map(lambda x: x+'_mad' if x!='roomid' else x)
group2ed_var = group2ed.var().reset_index()
group2ed_var.columns = group2ed_var.columns.map(lambda x: x+'_var' if x!='roomid' else x)

test = pd.merge(test,grouped_sum,how='left',on='basicroomid')
test = pd.merge(test,grouped_median,how='left',on='basicroomid')
test = pd.merge(test,grouped_mad,how='left',on='basicroomid')
test = pd.merge(test,grouped_var,how='left',on='basicroomid')
test = pd.merge(test,group2ed_sum,how='left',on='roomid')
test = pd.merge(test,group2ed_median,how='left',on='roomid')
test = pd.merge(test,group2ed_mad,how='left',on='roomid')
test = pd.merge(test,group2ed_var,how='left',on='roomid')

test.drop(['orderid','orderdate','hotelid','basicroomid','roomid','basic_week_ordernum_ratio','basic_recent3_ordernum_ratio','basic_comment_ratio',
            'basic_30days_ordnumratio','basic_30days_realratio','room_30days_ordnumratio','room_30days_realratio'],axis=1,inplace=True)
#print test.shape
test.to_csv('data/newfeature-5/add_test5.csv',index=False)

'''
train = pd.read_csv('../csv/new_train13.csv',nrows=None)
addtrain = pd.read_csv('../csv/add_train15.csv',nrows=None)
train = pd.concat([train,addtrain],axis=1)
train.to_csv('../csv/new_train15.csv',index=False)



test = pd.read_csv('../csv/new_test13.csv',nrows=None)
addtest = pd.read_csv('../csv/add_test15.csv',nrows=None)
test = pd.concat([test,addtest],axis=1)
test.to_csv('../csv/new_test15.csv',index=False)

'''