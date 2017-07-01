import pandas as pd

xgb_data=pd.read_csv('fusion_data/full_xgb_submission.csv')
#data.rename(columns={'rank':'rank1'},inplace=True)
xgb_data.rename(columns={'label':'xgb_score'},inplace=True)
#print xgb_data.shape

lgb_data=pd.read_csv('fusion_data/full_lgb_submission.csv')
lgb_data.rename(columns={'label':'lgb_score'},inplace=True)
#print lgb_data.shape

#print 'data loaded...'
data=pd.concat([xgb_data[['orderid','roomid','xgb_score']],lgb_data[['lgb_score']]],axis=1)
#print data.shape

p=1.2
q=1

data['multiply_fusion_score']=(data.xgb_score**p)*(data.lgb_score**q)
data=data[['orderid','roomid','multiply_fusion_score']]
#print data[0:100]

result=data.loc[data.groupby('orderid').apply(lambda x:x['multiply_fusion_score'].argmax())][['orderid','roomid']]
result.rename(columns={'roomid':'predict_roomid'},inplace=True)
result.to_csv('fusion_data/multiply_submission.csv',index=None)
#print result.shape