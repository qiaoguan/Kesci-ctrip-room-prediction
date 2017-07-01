import pandas as pd

def f(x):
    if pd.isnull(x.user_roomservice_2_1ratio) or pd.isnull(x.roomservice_2):
        ismaintype_rs2 = None
    else:
        if x.user_roomservice_2_1ratio>=0.5:
            maintype_rs2 = 1
        else:
            maintype_rs2 = 0
        if x.roomservice_2==maintype_rs2:
            ismaintype_rs2 = 1
        else:
            ismaintype_rs2 = 0
    return ismaintype_rs2

def g(x):
    if pd.isnull(x.user_roomservice_3_123ratio) or pd.isnull(x.roomservice_3):
        ismaintype_rs3 = None
    else:
        if (x.user_roomservice_3_123ratio>=0.5) & (x.roomservice_3 in (1,2,3)):
            ismaintype_rs3 = 1
        elif (x.user_roomservice_3_123ratio<0.5) & (x.roomservice_3==0):
            ismaintype_rs3 = 1
        else:
            ismaintype_rs3 = 0
    return ismaintype_rs3

def h(x):
    label_maintype_rs4 = x[['user_roomservice_4_0ratio','user_roomservice_4_1ratio','user_roomservice_4_2ratio',
                            'user_roomservice_4_3ratio','user_roomservice_4_4ratio','user_roomservice_4_5ratio']].argmax()
    if pd.isnull(label_maintype_rs4):
        ismaintype_rs4 = None
    else:
        maintype_rs4 = int(label_maintype_rs4[19:20])
        if x.roomservice_4==maintype_rs4:
            ismaintype_rs4 = 1
        else:
            ismaintype_rs4 = 0
    return ismaintype_rs4

def i(x):
    if pd.isnull(x.user_roomservice_5_1ratio) or pd.isnull(x.roomservice_5):
        ismaintype_rs5 = None
    else:
        if x.user_roomservice_5_1ratio>=0.5:
            maintype_rs5 = 1
        else:
            maintype_rs5 = 0
        if x.roomservice_5==maintype_rs5:
            ismaintype_rs5 = 1
        else:
            ismaintype_rs5 = 0
    return ismaintype_rs5

def j(x):
    label_maintype_rs6 = x[['user_roomservice_6_0ratio','user_roomservice_6_1ratio','user_roomservice_6_2ratio']].argmax()
    if pd.isnull(label_maintype_rs6):
        ismaintype_rs6 = None
    else:
        maintype_rs6 = int(label_maintype_rs6[19:20])
        if x.roomservice_6==maintype_rs6:
            ismaintype_rs6 = 1
        else:
            ismaintype_rs6 = 0
    return ismaintype_rs6

def k(x):
    if pd.isnull(x.user_roomservice_7_0ratio) or pd.isnull(x.roomservice_7):
        ismaintype_rs7 = None
    else:
        if x.user_roomservice_7_0ratio>=0.5:
            maintype_rs7 = 0
        else:
            maintype_rs7 = 1
        if x.roomservice_7==maintype_rs7:
            ismaintype_rs7 = 1
        else:
            ismaintype_rs7 = 0
    return ismaintype_rs7

def l(x):
    label_maintype_rs8 = x[['user_roomservice_8_1ratio','user_roomservice_8_2ratio','user_roomservice_8_345ratio']].argmax()
    if pd.isnull(label_maintype_rs8):
        ismaintype_rs8 = None
    else:
        maintype_rs8 = int(label_maintype_rs8[19:20])
        if (x.roomservice_8 in (3,4,5)) & (maintype_rs8==3):
            ismaintype_rs8 = 1
        else:
            if x.roomservice_8==maintype_rs8:
                ismaintype_rs8 = 1
            else:
                ismaintype_rs8 = 0
    return ismaintype_rs8

'''训练集特征生成'''
use_colname = ['roomservice_2','roomservice_3','roomservice_4','roomservice_5','roomservice_6','roomservice_7','roomservice_8',
               'user_roomservice_4_0ratio', 'user_roomservice_4_2ratio', 'user_roomservice_4_3ratio', 'user_roomservice_4_4ratio', 'user_roomservice_4_1ratio', 'user_roomservice_4_5ratio',
               'user_roomservice_3_123ratio', 'user_roomservice_6_2ratio', 'user_roomservice_6_1ratio', 'user_roomservice_6_0ratio', 'user_roomservice_5_1ratio', 'user_roomservice_7_0ratio',
               'user_roomservice_2_1ratio', 'user_roomservice_8_1ratio', 'user_rank_ratio', 'user_roomservice_5_345ratio']

#nrows = 10000  #测试代码用
nrows = None
train = pd.read_csv('dataset/competition_train.txt',sep='\t',nrows=nrows,usecols=use_colname); print('finish reading...')
train.rename(columns={'user_roomservice_5_345ratio':'user_roomservice_8_345ratio'},inplace=True)
use_colname.remove('user_roomservice_5_345ratio')
use_colname.append('user_roomservice_8_345ratio')

'''
train['star_diff'] = train['star']-train['user_avgstar']; print('finish generating star_diff...')
train['rank_diff'] = train['rank']-train['user_rank_ratio']; print('finish generating rank_diff...')
train['returnvalue_diff'] = train['returnvalue']-train['user_avgpromotion']; print('finish generating returnvalue_diff...')
train['price_diff'] = train['price_deduct']-train['user_avgprice']; print('finish generating price_diff...')
'''
train['ismaintype_rs2'] = train.apply(f,axis=1); print('finish generating ismaintype_rs2...')
train['ismaintype_rs3'] = train.apply(g,axis=1); print('finish generating ismaintype_rs3...')
train['ismaintype_rs4'] = train.apply(h,axis=1); print('finish generating ismaintype_rs4...')
train['ismaintype_rs5'] = train.apply(i,axis=1); print('finish generating ismaintype_rs5...')
train['ismaintype_rs6'] = train.apply(j,axis=1); print('finish generating ismaintype_rs6...')
train['ismaintype_rs7'] = train.apply(k,axis=1); print('finish generating ismaintype_rs7...')
train['user_roomservice_8_2ratio'] = 1-train['user_roomservice_8_1ratio']-train['user_roomservice_8_345ratio']
train['ismaintype_rs8'] = train.apply(l,axis=1); print('finish generating ismaintype_rs8...')

train.drop(use_colname,axis=1,inplace=True)
train[['ismaintype_rs2','ismaintype_rs3','ismaintype_rs4','ismaintype_rs5','ismaintype_rs6','ismaintype_rs7','ismaintype_rs8']].to_csv('data/features6-18/train_ismaintype.csv',index=False)


'''测试集特征生成'''
use_colname = ['roomservice_2','roomservice_3','roomservice_4','roomservice_5','roomservice_6','roomservice_7','roomservice_8',
               'user_roomservice_4_0ratio', 'user_roomservice_4_2ratio', 'user_roomservice_4_3ratio', 'user_roomservice_4_4ratio', 'user_roomservice_4_1ratio', 'user_roomservice_4_5ratio',
               'user_roomservice_3_123ratio', 'user_roomservice_6_2ratio', 'user_roomservice_6_1ratio', 'user_roomservice_6_0ratio', 'user_roomservice_5_1ratio', 'user_roomservice_7_0ratio',
               'user_roomservice_2_1ratio', 'user_roomservice_8_1ratio', 'user_rank_ratio', 'user_roomservice_5_345ratio']

test = pd.read_csv('dataset/competition_test.txt',sep='\t',nrows=nrows,usecols=use_colname); print('finish reading...')
test.rename(columns={'user_roomservice_5_345ratio':'user_roomservice_8_345ratio'},inplace=True)
use_colname.remove('user_roomservice_5_345ratio')
use_colname.append('user_roomservice_8_345ratio')

'''
train['star_diff'] = train['star']-train['user_avgstar']; print('finish generating star_diff...')
train['rank_diff'] = train['rank']-train['user_rank_ratio']; print('finish generating rank_diff...')
train['returnvalue_diff'] = train['returnvalue']-train['user_avgpromotion']; print('finish generating returnvalue_diff...')
train['price_diff'] = train['price_deduct']-train['user_avgprice']; print('finish generating price_diff...')
'''
test['ismaintype_rs2'] = test.apply(f,axis=1); print('finish generating ismaintype_rs2...')
test['ismaintype_rs3'] = test.apply(g,axis=1); print('finish generating ismaintype_rs3...')
test['ismaintype_rs4'] = test.apply(h,axis=1); print('finish generating ismaintype_rs4...')
test['ismaintype_rs5'] = test.apply(i,axis=1); print('finish generating ismaintype_rs5...')
test['ismaintype_rs6'] = test.apply(j,axis=1); print('finish generating ismaintype_rs6...')
test['ismaintype_rs7'] = test.apply(k,axis=1); print('finish generating ismaintype_rs7...')
test['user_roomservice_8_2ratio'] = 1-test['user_roomservice_8_1ratio']-test['user_roomservice_8_345ratio']
test['ismaintype_rs8'] = test.apply(l,axis=1); print('finish generating ismaintype_rs8...')

test.drop(use_colname,axis=1,inplace=True)
test[['ismaintype_rs2','ismaintype_rs3','ismaintype_rs4','ismaintype_rs5','ismaintype_rs6','ismaintype_rs7','ismaintype_rs8']].to_csv('data/features6-18/test_ismaintype.csv',index=False)











