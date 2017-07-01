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

p=0.2
q=0.8

data['linear_fusion_score']=p*data.xgb_score+q*data.lgb_score
data=data[['orderid','roomid','linear_fusion_score']]

t=data[['orderid']].drop_duplicates()
#print t.shape

result=data.loc[data.groupby('orderid').apply(lambda x:x['linear_fusion_score'].argmax())][['orderid','roomid']]
result.rename(columns={'roomid':'predict_roomid'},inplace=True)
result.to_csv('fusion_data/linear_submission.csv',index=None)
#print result.shape