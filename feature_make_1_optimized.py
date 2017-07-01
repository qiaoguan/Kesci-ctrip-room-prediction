import pandas as pd

use_colname = ['roomservice_2', 'roomservice_3', 'roomservice_4', 'roomservice_5', 'roomservice_6', 'roomservice_7', 'roomservice_8',
               'user_roomservice_4_0ratio', 'user_roomservice_4_2ratio', 'user_roomservice_4_3ratio', 'user_roomservice_4_4ratio', 'user_roomservice_4_1ratio', 'user_roomservice_4_5ratio',
               'user_roomservice_3_123ratio', 'user_roomservice_6_2ratio', 'user_roomservice_6_1ratio', 'user_roomservice_6_0ratio', 'user_roomservice_5_1ratio', 'user_roomservice_7_0ratio',
               'user_roomservice_2_1ratio', 'user_roomservice_8_1ratio',  'user_roomservice_5_345ratio']

#nrows = 10000  #测试代码用
nrows = None
train = pd.read_csv('dataset/competition_train.txt',sep='\t',nrows=nrows,usecols=use_colname); print('finish reading...')

train['user_roomservice_2_0ratio'] = 1-train['user_roomservice_2_1ratio']
train['user_roomservice_3_0ratio'] = 1-train['user_roomservice_3_123ratio']
train['user_roomservice_5_0ratio'] = 1-train['user_roomservice_5_1ratio']
train['user_roomservice_7_1ratio'] = 1-train['user_roomservice_7_0ratio']
train['user_roomservice_8_2ratio'] = 1-train['user_roomservice_8_1ratio']-train['user_roomservice_5_345ratio']

train['idxmax_rs2'] = train[['user_roomservice_2_0ratio','user_roomservice_2_1ratio']].idxmax(axis=1)
train['idxmax_rs3'] = train[['user_roomservice_3_0ratio','user_roomservice_3_123ratio']].idxmax(axis=1)
train['idxmax_rs4'] = train[['user_roomservice_4_0ratio','user_roomservice_4_1ratio','user_roomservice_4_2ratio','user_roomservice_4_3ratio',
                             'user_roomservice_4_4ratio','user_roomservice_4_5ratio']].idxmax(axis=1)
train['idxmax_rs5'] = train[['user_roomservice_5_0ratio','user_roomservice_5_1ratio']].idxmax(axis=1)
train['idxmax_rs6'] = train[['user_roomservice_6_0ratio','user_roomservice_6_1ratio','user_roomservice_6_2ratio']].idxmax(axis=1)
train['idxmax_rs7'] = train[['user_roomservice_7_0ratio','user_roomservice_7_1ratio']].idxmax(axis=1)
train['idxmax_rs8'] = train[['user_roomservice_8_1ratio','user_roomservice_8_2ratio','user_roomservice_5_345ratio']].idxmax(axis=1)

train['maintype_rs2'] = train['idxmax_rs2'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs3'] = train['idxmax_rs3'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs4'] = train['idxmax_rs4'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs5'] = train['idxmax_rs5'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs6'] = train['idxmax_rs6'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs7'] = train['idxmax_rs7'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
train['maintype_rs8'] = train['idxmax_rs8'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)

train['ismaintype_rs2'] = (train['roomservice_2']-train['maintype_rs2']).map({0:1,-1:0,1:0})
train['roomservice_3'] = train['roomservice_3'].map({0:0,1:1,2:1,3:1})
train['ismaintype_rs3'] = (train['roomservice_3']-train['maintype_rs3']).map({0:1,-1:0,1:0})
train['ismaintype_rs4'] = (train['roomservice_4']-train['maintype_rs4']).map({0:1,-1:0,1:0,-2:0,2:0,-3:0,3:0,-4:0,4:0,-5:0,5:0})
train['ismaintype_rs5'] = (train['roomservice_5']-train['maintype_rs5']).map({0:1,-1:0,1:0})
train['ismaintype_rs6'] = (train['roomservice_6']-train['maintype_rs6']).map({0:1,-1:0,1:0,-2:0,2:0})
train['ismaintype_rs7'] = (train['roomservice_7']-train['maintype_rs7']).map({0:1,-1:0,1:0})
train['roomservice_8'] = train['roomservice_8'].map({1:1,2:2,3:3,4:3,5:3})
train['ismaintype_rs8'] = (train['roomservice_8']-train['maintype_rs8']).map({0:1,-1:0,1:0,-2:0,2:0})

train[['ismaintype_rs2','ismaintype_rs3','ismaintype_rs4','ismaintype_rs5','ismaintype_rs6','ismaintype_rs7','ismaintype_rs8']].to_csv('data/features6-18/train_ismaintype.csv',index=False)




test = pd.read_csv('dataset/competition_test.txt',sep='\t',nrows=nrows,usecols=use_colname); print('finish reading...')

test['user_roomservice_2_0ratio'] = 1-test['user_roomservice_2_1ratio']
test['user_roomservice_3_0ratio'] = 1-test['user_roomservice_3_123ratio']
test['user_roomservice_5_0ratio'] = 1-test['user_roomservice_5_1ratio']
test['user_roomservice_7_1ratio'] = 1-test['user_roomservice_7_0ratio']
test['user_roomservice_8_2ratio'] = 1-test['user_roomservice_8_1ratio']-test['user_roomservice_5_345ratio']

test['idxmax_rs2'] = test[['user_roomservice_2_0ratio','user_roomservice_2_1ratio']].idxmax(axis=1)
test['idxmax_rs3'] = test[['user_roomservice_3_0ratio','user_roomservice_3_123ratio']].idxmax(axis=1)
test['idxmax_rs4'] = test[['user_roomservice_4_0ratio','user_roomservice_4_1ratio','user_roomservice_4_2ratio','user_roomservice_4_3ratio',
                             'user_roomservice_4_4ratio','user_roomservice_4_5ratio']].idxmax(axis=1)
test['idxmax_rs5'] = test[['user_roomservice_5_0ratio','user_roomservice_5_1ratio']].idxmax(axis=1)
test['idxmax_rs6'] = test[['user_roomservice_6_0ratio','user_roomservice_6_1ratio','user_roomservice_6_2ratio']].idxmax(axis=1)
test['idxmax_rs7'] = test[['user_roomservice_7_0ratio','user_roomservice_7_1ratio']].idxmax(axis=1)
test['idxmax_rs8'] = test[['user_roomservice_8_1ratio','user_roomservice_8_2ratio','user_roomservice_5_345ratio']].idxmax(axis=1)

test['maintype_rs2'] = test['idxmax_rs2'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs3'] = test['idxmax_rs3'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs4'] = test['idxmax_rs4'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs5'] = test['idxmax_rs5'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs6'] = test['idxmax_rs6'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs7'] = test['idxmax_rs7'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)
test['maintype_rs8'] = test['idxmax_rs8'].apply(lambda x: int(x[19:20]) if pd.notnull(x) else x)

test['ismaintype_rs2'] = (test['roomservice_2']-test['maintype_rs2']).map({0:1,-1:0,1:0})
test['roomservice_3'] = test['roomservice_3'].map({0:0,1:1,2:1,3:1})
test['ismaintype_rs3'] = (test['roomservice_3']-test['maintype_rs3']).map({0:1,-1:0,1:0})
test['ismaintype_rs4'] = (test['roomservice_4']-test['maintype_rs4']).map({0:1,-1:0,1:0,-2:0,2:0,-3:0,3:0,-4:0,4:0,-5:0,5:0})
test['ismaintype_rs5'] = (test['roomservice_5']-test['maintype_rs5']).map({0:1,-1:0,1:0})
test['ismaintype_rs6'] = (test['roomservice_6']-test['maintype_rs6']).map({0:1,-1:0,1:0,-2:0,2:0})
test['ismaintype_rs7'] = (test['roomservice_7']-test['maintype_rs7']).map({0:1,-1:0,1:0})
test['roomservice_8'] = test['roomservice_8'].map({1:1,2:2,3:3,4:3,5:3})
test['ismaintype_rs8'] = (test['roomservice_8']-test['maintype_rs8']).map({0:1,-1:0,1:0,-2:0,2:0})

test[['ismaintype_rs2','ismaintype_rs3','ismaintype_rs4','ismaintype_rs5','ismaintype_rs6','ismaintype_rs7','ismaintype_rs8']].to_csv('data/features6-18/test_ismaintype.csv',index=False)













