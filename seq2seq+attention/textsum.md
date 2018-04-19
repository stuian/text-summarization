## Generating News Headlines with Recurrent Neural Networks

好的笔记：[http://rsarxiv.github.io/2016/04/24/%E8%87%AA%E5%8A%A8%E6%96%87%E6%91%98%EF%BC%88%E4%BA%94%EF%BC%89/](http://rsarxiv.github.io/2016/04/24/%E8%87%AA%E5%8A%A8%E6%96%87%E6%91%98%EF%BC%88%E4%BA%94%EF%BC%89/)

> 由于giaword数据暂时得不到，于是选择用搜狗实验室2012年6-7月的新闻数据来做。对于这个数据，网上有使用seq2seq+attention进行处理的文章介绍。

> cnn/dailmail数据

## 一、seq2seq+attention和搜狗实验室2012年6-7月的新闻数据 ##

代码来源：[https://github.com/tensorflow/models/tree/master/research/textsum](https://github.com/tensorflow/models/tree/master/research/textsum)

REAMDE：

整个项目的结构框架：图片。

问题：
	
	$ bazel-bin/textsum/seq2seq_attention \
	--mode=train \
	--article_key=article \
	--abstract_key=abstract \
	--data_path=data/training-* \
	--vocab_path=data/vocab \
	--log_root=textsum/log_root \
	--train_dir=textsum/log_root/train

> log_root是什么？——checkpoints

> gbk，utf-8等编码是怎么回事

> tmp-放原文件数据集

### tensorflowAIP接口学习 ###

tf.Example:[https://blog.csdn.net/u010223750/article/details/70482498](https://blog.csdn.net/u010223750/article/details/70482498)

### python模块学习 ###

1、[glob](http://python.jobbole.com/81552/)

> 用它可以查找符合特定规则的文件路径名

查找文件只用到三个匹配符：”*”, “?”, “[]”。

- ”*”匹配0个或多个字符；
- ”?”匹配单个字符；
- ”[]”匹配指定范围内的字符，如：[0-9]匹配数字。

2、[random](https://docs.python.org/2/library/random.html)

3、[struct](https://docs.python.org/2/library/struct.html)

其他参考资料：[https://blog.csdn.net/djstavav/article/details/77950352](https://blog.csdn.net/djstavav/article/details/77950352)

> flush() 方法是用来刷新缓冲区的

4、[sys](https://www.cnblogs.com/Archie-s/p/6860301.html)

- sys.argv: 实现从程序外部向程序传递参数。
- sys.exit([arg]): 程序中间的退出，arg=0为正常退出。
- sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。
- sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）
- sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.
- sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
- sys.platform: 获取当前系统平台。
- sys.stdin,sys.stdout,sys.stderr: stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们

5、from collections import [namedtuple](https://blog.csdn.net/helei001/article/details/52692128)

> 同c语言的struct相似，给每个元素命名，并赋值。

6、[six.moves.queue](http://nullege.com/codes/search/six.moves.queue)

> queue——队列；Queue.Queue(QUEUE_NUM_BATCH * self._hps.batch_size)——设定队列的长度

7、range和xrange的区别

后者返回的是一个生成器，不需要像前者那样占用很大的内存空间，而且可以无限生成很多数。

8、线程：[threading](http://www.runoob.com/python/python-multithreading.html)

