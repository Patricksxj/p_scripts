
text1 ="""
Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. 
Unqualified, the word football is understood to refer to whichever form of football is the most popular 
in the regional context in which the word appears. Sports commonly called football in certain places 
include association football (known as soccer in some countries); gridiron football (specifically American 
football or Canadian football); Australian rules football; rugby football (either rugby league or rugby union); 
and Gaelic football. These different variations of football are known as football codes.
"""

text2 = """
Basketball is a team sport in which two teams of five players, opposing one another on a rectangular court, 
compete with the primary objective of shooting a basketball (approximately 9.4 inches (24 cm) in diameter) 
through the defender's hoop (a basket 18 inches (46 cm) in diameter mounted 10 feet (3.048 m) high to a backboard 
at each end of the court) while preventing the opposing team from shooting through their own hoop. A field goal is 
worth two points, unless made from behind the three-point line, when it is worth three. After a foul, timed play stops 
and the player fouled or designated to shoot a technical foul is given one or more one-point free throws. The team with 
the most points at the end of the game wins, but if regulation play expires with the score tied, an additional period 
of play (overtime) is mandated.
"""

text3 = """
Volleyball, game played by two teams, usually of six players on a side, in which the players use their hands to bat a 
ball back and forth over a high net, trying to make the ball touch the court within the opponents’ playing area before 
it can be returned. To prevent this a player on the opposing team bats the ball up and toward a teammate before it touches 
the court surface—that teammate may then volley it back across the net or bat it to a third teammate who volleys it across 
the net. A team is allowed only three touches of the ball before it must be returned over the net.
"""

import nltk
import string
from collections import Counter

# 文本预处理
# 函数：text文件分句，分词，并去掉标点
def get_tokens(text):
    text = text.replace('\n', '')
    sents = nltk.sent_tokenize(text)  # 分句
    print("sents:",sents)
    tokens = []
    for sent in sents:
        for word in nltk.word_tokenize(sent):  # 分词
            if word not in string.punctuation: # 去掉标点
                tokens.append(word)
    return tokens

from nltk.corpus import stopwords     #停用词

# 对原始的text文件去掉停用词
# 生成count字典，即每个单词的出现次数
def make_count(text):
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]    #去掉停用词
    count = Counter(filtered)
    return count

