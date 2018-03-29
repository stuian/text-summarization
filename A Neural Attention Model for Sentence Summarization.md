## A Neural Attention Model for Sentence Summarization ##

前馈神经网络语言模型

![](http://7te9qt.com1.z0.glb.clouddn.com/1.gif)

y=b+Wx+Utanh(d+Hx)

### beam-search ###

整个算法的核心参数是词表V和集束宽度K，而整个算法的过程可以具体为如下所述：

- 假设词表V大小为3，内容是a,b,c.而集束宽度为2（每一步计算过后保留的节点数量）.
- 解码时的步骤为：
	- 生成第一个词时，先根据启发代价对节点进行排序，选择概率最大的两个，假设是a,b,那么当前序列就是a,b
	- 生成第二个词的时候，我们将当前词与词表中的所有词进行组合，得到新的6个序列，aa,ab,ac,ba,bb,bc,再选概率最大的两个作为当前序列，例如是aa,ab
	- 重复步骤2，直到遇到结束符，概率最高的2个序列就是输出。
	
> 集束宽度可以是预先定好的，也可以是变动的，可以先按照一个最小的集束宽度进行搜索，如果没有找到合适的解，再扩大集束宽度再找一遍。

### neural machine translation ###

方老师的ppt

#### 文本摘要传统方法 ####

在本论文发表之前，对于生成式自动摘要的实现主要利用的是语言激励限制(linguistically-inspired constraints)和输入文本的句法变换(syntactic transformations of the input text)的方法，而本论文所实现的系统是一种完全数据驱动的、将神经语言模型与编码器相结合的生成式摘要系统。

中文博客参考连接：

1、[http://m.blog.csdn.net/John159151/article/details/72856477](http://m.blog.csdn.net/John159151/article/details/72856477)

2、[https://zhuanlan.zhihu.com/p/26906764](https://zhuanlan.zhihu.com/p/26906764)

![](https://pic2.zhimg.com/50/v2-19ecfd0af4f89f80afa969519f947275_hd.jpg)

### 神经网络语言模型+decoder ###

输入对象是一个句子(x)

- 目标是通过y(c)预测后一个词语y(i+1)；
- 先对x与y(c)进行encode成H*1的向量；
-  将y(c)embedding,U乘，经过非线性变换，得到h(H*1)向量
-  继续非线性变换，得到V*1的向量，代表下一个词的概率；

![](https://pic2.zhimg.com/50/v2-989fcfe96f57cc25c2683d6567ef523d_hd.jpg)

### encode的三种三种方式 ###

①enc1：Bag-of-Words Encoder 

> 词袋模型(bag-of-words)编码器不能反映出词与词之间的语义关系与顺序

②enc2：Convolutional Encoder 

CNN通过结合word embedding将句子表示成一个matrix，通过不同尺寸的卷积核来filter出句子中的feature。 

![](http://img.blog.csdn.net/20170604004211269?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvSm9objE1OTE1MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![](http://img.blog.csdn.net/20170604004220298?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvSm9objE1OTE1MQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



