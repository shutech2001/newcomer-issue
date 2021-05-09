# newcomer-issue

## 3-6

LGB : Best parameters

{'boosting_type': 'goss', 'num_leaves': 63, 'max_depth': 949, 'learning_rate': 0.02061442427834546, 'n_estimators': 382, 'min_child_weight': 9.93246483600419e-08, 'min_child_samples': 10, 'reg_lambda': 9.347509937659662e-08}

---------------------------------------

RMSE : 0.436286658988412

Q^2 : 0.8710211329150095  

---------------------------------------  
※default  
Q^2 : 0.8736131293047061  
下がっている。  

## 3-7-ECFP4

SVR : Best parameters

{'kernel': 'linear', 'gamma': 'auto', 'tol': 0.04452423351599806, 'C': 0.0008675341299462108, 'epsilon': 0.07707366424031765}

---------------------------------------

RMSE : 0.5465771516029059

Q^2 : 0.7975687122642893

---------------------------------------

## 3-7-3D

SVR : Best parameters

{'kernel': 'rbf', 'gamma': 'auto', 'tol': 1.165972163302293e-07, 'C': 6.357352836096048, 'epsilon': 0.6999527204922626}

---------------------------------------

RMSE : 0.9269053938263705

Q^2 : 0.41783577938021654

---------------------------------------

かなりQ^2-valueが小さい。

## 3-8  
真値と予測値の差が0.75を超えるものを外れているデータ，0.05以内のものを当たっているデータと定義した。  
膜透過係数の対数値
![papp1](newcomer3/papp/1.gif)

### 3-6の結果考察
|Assay ID|テストデータの数|外れているデータの数|当たっているデータの数|
|:---|:---|:---|:---| 
|CHEMBL3431937|47|6|5|
|CHEMBL905613|21|1|2|
|CHEMBL1034536|12|2|1| 
|CHEMBL3430218|6|1|0|
|Astellas|5|0|2|
|CHEMBL905612|3|0|0|  
|Enamine|1|0|0|

テストデータ数が少ないため一概には言えないが，Astellasの化合物は当たっているデータ数の割合が高い。

##### 各分子の構造  
外れているもの(真値よりも大きく予測)  
![1](newcomer3/newcomer3_6_out/1.png)
![2](newcomer3/newcomer3_6_out/2.png)
![3](newcomer3/newcomer3_6_out/3.png)
![5](newcomer3/newcomer3_6_out/5.png)
![6](newcomer3/newcomer3_6_out/6.png)
![8](newcomer3/newcomer3_6_out/8.png)
![9](newcomer3/newcomer3_6_out/9.png)  
外れているもの(真値よりも小さく予測)  
![4](newcomer3/newcomer3_6_out/4.png)
![7](newcomer3/newcomer3_6_out/7.png)
![10](newcomer3/newcomer3_6_out/10.png)

真値よりも小さく予測したものに共通する構造は以下に示す構造である。
![考察1](newcomer3/newcomer_inquiry/1.jpg)

当たっているもの  
![11](newcomer3/newcomer3_6_in/1.png)
![12](newcomer3/newcomer3_6_in/2.png)
![13](newcomer3/newcomer3_6_in/3.png)
![14](newcomer3/newcomer3_6_in/4.png)
![15](newcomer3/newcomer3_6_in/5.png)
![16](newcomer3/newcomer3_6_in/6.png)
![17](newcomer3/newcomer3_6_in/7.png)
![18](newcomer3/newcomer3_6_in/8.png)
![19](newcomer3/newcomer3_6_in/9.png)
![20](newcomer3/newcomer3_6_in/10.png)

### 3-7-ECFP4の結果考察  
|Assay ID|テストデータの数|外れているデータの数|当たっているデータの数|
|:---|:---|:---|:---| 
|CHEMBL3431937|47|5|6|
|CHEMBL905613|21|7|0|
|CHEMBL1034536|12|2|1| 
|CHEMBL3430218|6|4|0|
|Astellas|5|0|1|
|CHEMBL905612|3|2|0|  
|Enamine|1|1|0|

CHEMBL905613, CHEMBL3430218, CHEMBL905612の化合物で外れている割合が高く，2D記述子同様Astellasの化合物は当たっている。

##### 各分子の構造  
外れているもの  
![21](newcomer3/newcomer3_7_ecfp4_out/1.png)
![22](newcomer3/newcomer3_7_ecfp4_out/2.png)
![23](newcomer3/newcomer3_7_ecfp4_out/3.png)
![24](newcomer3/newcomer3_7_ecfp4_out/4.png)
![25](newcomer3/newcomer3_7_ecfp4_out/5.png)
![26](newcomer3/newcomer3_7_ecfp4_out/6.png)
![27](newcomer3/newcomer3_7_ecfp4_out/7.png)
![28](newcomer3/newcomer3_7_ecfp4_out/8.png)
![29](newcomer3/newcomer3_7_ecfp4_out/9.png)
![30](newcomer3/newcomer3_7_ecfp4_out/10.png)
![31](newcomer3/newcomer3_7_ecfp4_out/10.png)
![32](newcomer3/newcomer3_7_ecfp4_out/11.png)
![33](newcomer3/newcomer3_7_ecfp4_out/12.png)
![34](newcomer3/newcomer3_7_ecfp4_out/13.png)
![35](newcomer3/newcomer3_7_ecfp4_out/14.png)
![36](newcomer3/newcomer3_7_ecfp4_out/15.png)
![37](newcomer3/newcomer3_7_ecfp4_out/16.png)
![38](newcomer3/newcomer3_7_ecfp4_out/17.png)
![39](newcomer3/newcomer3_7_ecfp4_out/18.png)
![40](newcomer3/newcomer3_7_ecfp4_out/19.png)
![41](newcomer3/newcomer3_7_ecfp4_out/21.png)



当たっているもの  
![51](newcomer3/newcomer3_7_ecfp4_in/1.png)
![52](newcomer3/newcomer3_7_ecfp4_in/2.png)
![53](newcomer3/newcomer3_7_ecfp4_in/3.png)
![54](newcomer3/newcomer3_7_ecfp4_in/4.png)
![55](newcomer3/newcomer3_7_ecfp4_in/5.png)
![56](newcomer3/newcomer3_7_ecfp4_in/6.png)
![57](newcomer3/newcomer3_7_ecfp4_in/7.png)
![58](newcomer3/newcomer3_7_ecfp4_in/8.png)

### 3-7-3dの結果考察
|Assay ID|テストデータの数|外れているデータの数|当たっているデータの数|
|:---|:---|:---|:---| 
|CHEMBL3431937|47|4|3|
|CHEMBL905613|21|6|1|
|CHEMBL1034536|12|1|1| 
|CHEMBL3430218|6|2|1|
|Astellas|5|0|1|
|CHEMBL905612|3|0|0|  
|Enamine|1|1|0|

CHEMBL905613の化合物で外れている割合が高く，2D記述子, ECFP4同様にAstellasの化合物は当たっている。

##### 各分子の構造  
外れているもの  
![61](newcomer3/newcomer3_7_3d_out/1.png)
![62](newcomer3/newcomer3_7_3d_out/2.png)
![63](newcomer3/newcomer3_7_3d_out/3.png)
![64](newcomer3/newcomer3_7_3d_out/4.png)
![65](newcomer3/newcomer3_7_3d_out/5.png)
![66](newcomer3/newcomer3_7_3d_out/6.png)
![67](newcomer3/newcomer3_7_3d_out/7.png)
![68](newcomer3/newcomer3_7_3d_out/8.png)
![69](newcomer3/newcomer3_7_3d_out/9.png)
![70](newcomer3/newcomer3_7_3d_out/10.png)
![71](newcomer3/newcomer3_7_3d_out/11.png)
![72](newcomer3/newcomer3_7_3d_out/12.png)
![73](newcomer3/newcomer3_7_3d_out/13.png)
![74](newcomer3/newcomer3_7_3d_out/14.png)



当たっているもの  
![81](newcomer3/newcomer3_7_3d_in/1.png)
![82](newcomer3/newcomer3_7_3d_in/2.png)
![83](newcomer3/newcomer3_7_3d_in/3.png)
![84](newcomer3/newcomer3_7_3d_in/4.png)
![85](newcomer3/newcomer3_7_3d_in/5.png)
![86](newcomer3/newcomer3_7_3d_in/6.png)
![87](newcomer3/newcomer3_7_3d_in/7.png)
















