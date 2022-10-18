import tensorflow as tf
x = tf.random.normal(shape=(3,784))   # 假設 3張圖片 ，每張圖片總畫素共28x28=784個畫素
tf.Tensor(
[[ 0.51171166  1.6902593   1.0871     ...  0.25590673  0.61627156
  -1.3195912 ]
 [ 2.151131   -1.2189074   0.27053183 ... -0.6083903  -0.14731756
   0.6107628 ]
 [ 0.44352484 -0.21213555  1.7377648  ... -1.5042872   2.075452
  -1.1409923 ]], shape=(3, 784), dtype=float32)
  # 假如，(1,784)的一維張量→784個特徵→轉換成輸出10個特徵(1,10)→需要(784,10)的矩陣做相乘=W → X(Input)*W(weight)=O(Output)
# 設定權重 (先隨便給，之後訓練用)
# Variable:可變換的張量 (一般張量裡面的數值不可變換)
w1 = tf.Variable(tf.random.normal([784,10],stddev=0.1))
# 設定偏置 (先隨便給，之後訓練用)→每個Neuron的偏置Bias值不一樣→每個結果篩選的標準不一→ex : 第一個output特徵:房價
b1 = tf.Variable(tf.zeros(shape=(1,10)))
# 一般矩陣乘法(非單純各個元素相乘)
o1 = tf.matmul(x,w1)+b1
o1 = tf.nn.relu(o1)

print(o1.shape)
print(o1)
