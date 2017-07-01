import pandas as pd
#nrows = 10000  #测试代码用
nrows = None
train = pd.read_csv('data/train_feature1.csv',nrows=nrows,usecols=['orderid','basicroomid','price_deduct','returnvalue','true_value'])
group = train[['orderid','basicroomid','price_deduct','returnvalue','true_value']].groupby(['orderid','basicroomid'])
train = pd.merge(train,group.median().reset_index().rename(columns={'price_deduct':'price_deduct_basic_median',
                                                                  'returnvalue':'returnvalue_basic_median',
                                                                  'true_value':'true_value_basic_median'}),
                 on=['orderid','basicroomid'],how='left')
train = pd.merge(train,group.std().reset_index().rename(columns={'price_deduct':'price_deduct_basic_std',
                                                                  'returnvalue':'returnvalue_basic_std',
                                                                  'true_value':'true_value_basic_std'}),
                 on=['orderid','basicroomid'],how='left')
#################################################################################################
group = train[['orderid','basicroomid','price_deduct','returnvalue','true_value']].groupby(['orderid','basicroomid'])
train = pd.merge(train,group.sum().reset_index().rename(columns={'price_deduct':'price_deduct_basic_sum',
                                                                  'returnvalue':'returnvalue_basic_sum',
                                                                  'true_value':'true_value_basic_sum'}),
                 on=['orderid','basicroomid'],how='left')
train = pd.merge(train,group.min().reset_index().rename(columns={'price_deduct':'price_deduct_basic_min',
                                                                  'returnvalue':'returnvalue_basic_min',
                                                                  'true_value':'true_value_basic_min'}),
                 on=['orderid','basicroomid'],how='left')
train = pd.merge(train,group.max().reset_index().rename(columns={'price_deduct':'price_deduct_basic_max',
                                                                  'returnvalue':'returnvalue_basic_max',
                                                                  'true_value':'true_value_basic_max'}),
                 on=['orderid','basicroomid'],how='left')

train.drop(['orderid','basicroomid','price_deduct','returnvalue','true_value'],axis=1,inplace=True)
#train.to_csv('data/add_train11.csv',index=False)

'''组合feature_combine13.py feature_combine15.py特征'''
add_train13 = pd.read_csv('data/add_train13.csv', nrows=nrows)
train_newFeatures43 = pd.concat([train,add_train13], axis=1,)
train_newFeatures43.to_csv('data/features6-18/train_newFeatures43.csv',index=False)

#################################################################################################

test = pd.read_csv('data/test_feature1.csv',nrows=nrows,usecols=['orderid','basicroomid','price_deduct','returnvalue','true_value'])
group = test[['orderid','basicroomid','price_deduct','returnvalue','true_value']].groupby(['orderid','basicroomid'])
test = pd.merge(test,group.median().reset_index().rename(columns={'price_deduct':'price_deduct_basic_median',
                                                                  'returnvalue':'returnvalue_basic_median',
                                                                  'true_value':'true_value_basic_median'}),
                 on=['orderid','basicroomid'],how='left')
test = pd.merge(test,group.std().reset_index().rename(columns={'price_deduct':'price_deduct_basic_std',
                                                                  'returnvalue':'returnvalue_basic_std',
                                                                  'true_value':'true_value_basic_std'}),
                 on=['orderid','basicroomid'],how='left')

#################################################################################################
test = pd.merge(test,group.sum().reset_index().rename(columns={'price_deduct':'price_deduct_basic_sum',
                                                                  'returnvalue':'returnvalue_basic_sum',
                                                                  'true_value':'true_value_basic_sum'}),
                 on=['orderid','basicroomid'],how='left')
test = pd.merge(test,group.min().reset_index().rename(columns={'price_deduct':'price_deduct_basic_min',
                                                                  'returnvalue':'returnvalue_basic_min',
                                                                  'true_value':'true_value_basic_min'}),
                 on=['orderid','basicroomid'],how='left')
test = pd.merge(test,group.max().reset_index().rename(columns={'price_deduct':'price_deduct_basic_max',
                                                                  'returnvalue':'returnvalue_basic_max',
                                                                  'true_value':'true_value_basic_max'}),
                 on=['orderid','basicroomid'],how='left')

test.drop(['orderid','basicroomid','price_deduct','returnvalue','true_value'],axis=1,inplace=True)
#test.to_csv('data/add_test11.csv',index=False)

'''组合feature_combine13.py feature_combine15.py特征'''
add_test13 = pd.read_csv('data/add_test13.csv', nrows=nrows)
test_newFeatures43 = pd.concat([test,add_test13], axis=1,)
test_newFeatures43.to_csv('data/features6-18/test_newFeatures43.csv',index=False)

#'''
#train = pd.read_csv('../csv/new_train10.csv',nrows=None)
#addtrain = pd.read_csv('../csv/add_train11.csv',nrows=None)
#train[['price_deduct_basic_median','returnvalue_basic_median','true_value_basic_median',
#      'price_deduct_basic_std','returnvalue_basic_std','true_value_basic_std']] = addtrain[['price_deduct_basic_median','returnvalue_basic_median','true_value_basic_median',
#                                                                                            'price_deduct_basic_std','returnvalue_basic_std','true_value_basic_std']]
#train.to_csv('../csv/new_train11.csv',index=False)
#
#'''
#test = pd.read_csv('../csv/new_test10.csv',nrows=None)
#addtest = pd.read_csv('../csv/add_test11.csv',nrows=None)
#test[['price_deduct_basic_median','returnvalue_basic_median','true_value_basic_median',
#      'price_deduct_basic_std','returnvalue_basic_std','true_value_basic_std']] = addtest[['price_deduct_basic_median','returnvalue_basic_median','true_value_basic_median',
#                                                                                            'price_deduct_basic_std','returnvalue_basic_std','true_value_basic_std']]
#test.to_csv('../csv/new_test11.csv',index=False)


















































