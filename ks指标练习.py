from sklearn.metrics import roc_curve,auc
import pandas as pd


def ks_cal_auc(data,score_col,class_col):
    fpr,tpr,threshold=roc_curve(1-data[class_col[0]].ravel(),data[score_col[0]].ravel())
    ks=max(tpr-fpr)
    return ks,fpr,tpr,threshold

# y30是预测值，a是预测分数
data_test_1={'y30':[1,1,1,1,1,1,0,0,0,0,0,0],'a':[1,2,0,2,2,7,4,5,4,0,4,18]}
data_test_2=pd.DataFrame(data_test_1)

ks_auc,fpr_auc,tpr_auc,threshold_auc=ks_cal_auc(data_test_2,['a'],['y30'])

print(ks_auc)
print('tpr：',tpr_auc)
print('fpr：',fpr_auc)
print('threshold：',threshold_auc)
data_test_2.to_excel('20210131_ks计算数据导出.xls')