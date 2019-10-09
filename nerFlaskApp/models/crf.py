from sklearn_crfsuite import CRF

from .util import sent2features


class CRFModel(object):
    def __init__(self,
                 algorithm='lbfgs',
                 c1=0.1,
                 c2=0.1,
                 max_iterations=100,
                 all_possible_transitions=False
                 ):
        self.model = CRF(algorithm=algorithm,
                         c1=c1,
                         c2=c2,
                         max_iterations=max_iterations,
                         all_possible_transitions=all_possible_transitions)

    def train(self, sentences, tag_lists):
        features = [sent2features(s) for s in sentences]
        self.model.fit(features, tag_lists)

    def test(self, sentences):
        features = [sent2features(s) for s in sentences]
        pred_tag_lists = self.model.predict(features)
        return pred_tag_lists


""""
团：一个图的子集，任意两节点之间都有边连接。
极大团：一个加入任何一节点之后都无法再构成团的团（团+一个节点≠团）
势函数：

CRF模型
马尔科夫随机场是随机场的特例，它假设随机场中某一个位置的赋值
仅仅与和它相邻的位置的赋值有关，和与其不相邻的位置的赋值无关。

随机场：随机场是由若干个位置组成的整体，
当给每一个位置中按照某种分布随机赋予一个值之后，其全体就叫做随机场。

马尔可夫随机场:马尔科夫随机场是随机场的特例，它假设随机场中某一个位置的赋值
仅仅与和它相邻的位置的赋值有关，和与其不相邻的位置的赋值无关。

条件随机场：已知状态序列（词性）X和观测序列（实际文字序列）Y
X（x1,x2,x3...x）
Y（y1,y2,y3...yn）
若随机变量Y构成的是一个马尔科夫随机场，则称条件概率分布P(Y|X)是条件随机场。
通常情况下我们所说的条件随机场是一个线性链条件随机场，也就是X序列和Y序列长度相同。

线性链条件随机场：
特殊的条件随机场表示为


"""
