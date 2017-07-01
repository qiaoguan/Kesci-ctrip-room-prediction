       Kesci--携程用户预订售卖房型概率预测   代码目录

运行环境：python2.7

生成训练集特征的代码：
gen_trainfeature1.py   --生成train_related_feature1.csv放在目录data下
gen_trainfeature2.py   --生成train_feature1.csv放在data目录下
gen_trainfeature3.py   --生成train_feature_add3.csv,  
gen_trainfeature4.py   --生成train_feature_add4_1.csv放在data/new-feature-6-22/目录下

生成测试集特征的代码（相应的测试集特征）：
gen_testfeature1.py    --生成
gen_testfeature2.py    --生成
gen_testfeature3.py    --生成
gen_testfeature4.py    --生成

生成训练集和测试集特征
feature_combine13.py   --生成add_train13和add_test13存放在data目录下
feature_combine15.py   --生成train_newfeatures43.csv  和 test_newfeatures43.csv存放在data/features6-18里面   
gen_feature5.py        --生成add_train5.csv和add_test5.csv放在目录  data/newfeature-5下
feature_make_1.py（feature_make_1_optimized.py）  --生成train_ismaintype.csv、test_ismaintype.csv存放在data/features6-18里面
注：feature_make_1.py 这部分代码写的时候没考虑到优化的问题，其中包含了大量的条件判断，导致需要运行很长时间。比赛结束后我们对这部分代码进行了优化，
命名成为feature_make_1_optimized.py，实际使用时推荐运行此文件代替。
                              
###########################################################
特征数据生成，代码运行顺序：
gen_trainfeature1.py   gen_testfeature1.py    
gen_trainfeature2.py   gen_testfeature2.py  
feature_combine13.py    
feature_combine15.py   
gen_trainfeature3.py   gen_testfeature3.py    
gen_trainfeature4.py   gen_testfeature4.py    
gen_feature5.py
feature_make_1.py
###########################################################

模型训练代码和生成预测结果：
train_lgb.py
train_xgb.py

模型融合代码：
linear_fusion.py   线性融合（最好成绩）
multiply_fusion.py  相乘融合

dataset目录下存放训练集和测试集数据
data目录下存放所有生成的 训练集和测试集特征
fusion_data目录下存放进行模型融合前  xgboost和lightGBM生成的所有房型预测的概率
最高得分结果文件为：linear_submission_0.2_0.8.csv 存放在fusion_data目录下


