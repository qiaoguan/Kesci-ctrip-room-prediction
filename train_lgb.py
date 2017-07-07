import pandas as pd
import numpy as np
import gc
import lightgbm as lgb
from sklearn.cross_validation import train_test_split
#nrows = 10000  #测试代码用
nrows = None
train_feature1=pd.read_csv('data/train_feature1.csv', nrows=nrows) 
#train_feature1=pd.read_csv('data/train_feature1_7724875_252.csv')
train_related_feature1=pd.read_csv('data/train_related_feature1.csv', nrows=nrows) 
train_related_feature1=train_related_feature1.drop(['orderid','roomid'],axis=1)
train_ismaintype=pd.read_csv('data/features6-18/train_ismaintype.csv', nrows=nrows) 
train_newFeature=pd.read_csv('data/features6-18/train_newFeatures43.csv', nrows=nrows) 
train_feature3=pd.read_csv('data/train_feature_add3.csv', nrows=nrows) 
train_feature4=pd.read_csv('data/newfeature-6-22/train_feature_add4_1.csv', nrows=nrows) 
train_feature5=pd.read_csv('data/newfeature-5/add_train5.csv', nrows=nrows) 

trainset=pd.concat([train_feature1,train_related_feature1,train_ismaintype,train_newFeature,train_feature3,train_feature4,train_feature5],axis=1)
#trainset=trainset.drop(['user_roomservice_4_1ratio_3month','user_roomservice_4_1ratio_1month','user_roomservice_4_1ratio_1week',\
#	                'user_roomservice_2_other_ratio'],axis=1)
print(trainset.shape)

del train_feature1,train_related_feature1,train_ismaintype,train_newFeature,train_feature3,train_feature4,train_feature5
gc.collect()

trainset=trainset[(trainset.orderdate_lastord<=trainset.orderdate)&(trainset.user_avgadvanceddate>=0)]#filter some unnormal data  (filter 22037 samples, 688 of which label are 1)
#trainset=trainset[(trainset.user_confirmtime<=0)]

user=trainset[['uid']].drop_duplicates()
#print user.shape
#user,testuser=train_test_split(user,test_size=0.5,random_state=0)   # select 50% user for training and testing
trainuser,testuser=train_test_split(user,test_size=0.2,random_state=0)   # split trainset according to user
#print trainuser.shape
#print testuser.shape

train=trainset[trainset.uid.isin(trainuser.uid)]
val=trainset[trainset.uid.isin(testuser.uid)]

print(train.shape)
print(val.shape)

del trainset,trainuser,testuser,user
gc.collect()

train_y=train.orderlabel
train_x=train.drop(['orderid','uid','hotelid','basicroomid','roomid','orderlabel','orderid_lastord','hotelid_lastord',\
	                'roomid_lastord','basicroomid_lastord'],axis=1)
val_y=val.orderlabel
val_x=val.drop(['orderid','uid','hotelid','basicroomid','roomid','orderlabel','orderid_lastord','hotelid_lastord',\
	            'roomid_lastord','basicroomid_lastord'],axis=1)
del train
del val
gc.collect()
print('---------------------------------')
print(train_x.shape)
print(train_y.shape)
print(val_x.shape)
print(val_y.shape)

col = train_x.columns #由于会出现训练和预测的feature_names mismatch所以通过colname控制
lgb_train=lgb.Dataset(train_x,train_y)
del train_x,train_y
gc.collect()

lgb_val=lgb.Dataset(val_x,val_y)
del val_x,val_y
gc.collect()

params={'boosting_type':'gbdt',
	    'objective': 'binary',
	    'metric':'auc',
	    'max_depth':6,
	    'num_leaves':80,
	    'lambda_l2':1,
	    'subsample':0.7,
	    'learning_rate': 0.03,
	    'feature_fraction':0.7,
	    'bagging_fraction':0.8,
	    'bagging_freq':10,
	    'num_threads':25
	    }
bst = lgb.train(params,lgb_train,num_boost_round=8000,valid_sets=lgb_val,early_stopping_rounds=200,
	            categorical_feature=['roomservice_8','roomservice_4','roomservice_3','roomtag_1','this_last_roomservice_8_gap'])
bst.save_model('lgb.txt')  #save model

del lgb_train, lgb_val
gc.collect()

#==============================================================================
# # save feature score
# f_score={}
# feature_name=bst.feature_name()
# feature_importance=bst.feature_importance()
# for i in range(len(feature_name)):
# 	f_score[feature_name[i]]=feature_importance[i]
# lgb_fscore=sorted(f_score.iteritems(),key=lambda x:x[1],reverse=True)
# fs=[]
# for (key,value) in lgb_fscore:
# 	fs.append('{0},{1}\n'.format(key,value))
# with open('lgb_fscore.csv','w') as f:
# 	f.writelines('feature,score\n')
# 	f.writelines(fs)
#==============================================================================


test_feature1=pd.read_csv('data/test_feature1.csv', nrows=nrows) 
#test_feature1=pd.read_csv('data/test_feature1_7448647_251.csv')
test_related_feature1=pd.read_csv('data/test_related_feature1.csv', nrows=nrows) 
test_related_feature1=test_related_feature1.drop(['orderid','roomid'],axis=1)
test_ismaintype=pd.read_csv('data/features6-18/test_ismaintype.csv', nrows=nrows) 
test_newFeature=pd.read_csv('data/features6-18/test_newFeatures43.csv', nrows=nrows) 
test_feature3=pd.read_csv('data/test_feature_add3.csv', nrows=nrows) 
test_feature4=pd.read_csv('data/newfeature-6-22/test_feature_add4_1.csv', nrows=nrows) 
test_feature5=pd.read_csv('data/newfeature-5/add_test5.csv', nrows=nrows) 

reader=pd.concat([test_feature1,test_related_feature1,test_ismaintype,test_newFeature,test_feature3,test_feature4,test_feature5],axis=1)
print(reader.shape)

#reader=reader.drop(['user_roomservice_4_1ratio_3month','user_roomservice_4_1ratio_1month','user_roomservice_4_1ratio_1week',\
#	                'user_roomservice_2_other_ratio'],axis=1)
#print reader.shape
del test_feature1,test_related_feature1,test_ismaintype,test_newFeature,test_feature3,test_feature4,test_feature5
gc.collect()

#reader=pd.read_csv('data/testset.csv',chunksize=200000)
flag=0
testset_preds=[]
for i in range(38):
	testset=reader[i*200000:(i+1)*200000]
	if flag==0:
		testset_preds1=testset[['orderid','roomid']]
		testset_x=testset.drop(['orderid','uid','hotelid','basicroomid','roomid','orderid_lastord','hotelid_lastord',\
	            'roomid_lastord','basicroomid_lastord'],axis=1)
		testset_preds1['label'] = bst.predict(testset_x[col],num_iteration=bst.best_iteration)
		testset_preds=testset_preds1
		flag=1
	else:
		testset_preds1=testset[['orderid','roomid']]
		testset_x=testset.drop(['orderid','uid','hotelid','basicroomid','roomid','orderid_lastord','hotelid_lastord',\
	            'roomid_lastord','basicroomid_lastord'],axis=1)
		testset_preds1['label'] = bst.predict(testset_x[col],num_iteration=bst.best_iteration)
		testset_preds=pd.concat([testset_preds,testset_preds1],axis=0)
del reader
gc.collect()
#testset_preds['label'] = bst.predict(testset_x,num_iteration=bst.best_iteration)
testset_preds.sort_values(by=['orderid','label'],inplace=True)
testset_preds['ranks']=testset_preds.groupby('orderid')['label'].rank(ascending=False)
testset_preds.to_csv('fusion_data/full_lgb_submission.csv',index=None)
testset_preds=testset_preds[testset_preds.ranks==1]
testset_preds[['orderid','roomid']].rename(columns={'roomid':'predict_roomid'}).to_csv('lgb_submission.csv',index=None)
#print testset_preds.shape
