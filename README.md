# YI
纯属消遣娱乐。根据蓍草占卜法的原理编写的一个小工具。

Just for fun. Inspired from "shi cao zhan bu fa", a kind of yarrow stalks divination.


0 使用方法

输入想要占问的问题，等待结果。三短杠代表阳爻，两短杠夹一空格代表阴爻，变爻在其后以星号标记。解卦方式不一，可以自行查询相关介绍。后面我会介绍两种解卦的基本方法（1.2）。


0 Usage

Only thing needed is to type what you want to ask, then the result will come later. The line '---' represents "yang yao" (solid or positive) and the line '- -' represents "yin yao" (broken or negitive). The star sign means the line is a 'bian yao' (moving line). There are multiple ways to interpret the 'gua' (hexagram), you can find them in the Internet. I give two basic ways below.


1 介绍

1.1 蓍草成卦法

该法需要50根蓍草，实际用到49根（一说每次用到49或48或47或6根不等[1]）。将这些蓍草一分为二，从代表“天”的那一堆（哪个是天哪个是地，说法不一，可以自行查资料）取出1根放中间，然后将两堆蓍草分别不断地取出4根，直到每边剩下的蓍草都小于或等于4根。拿走剩下的这些蓍草以及之前取出放中间的蓍草，余下的蓍草重复从一分为二开始的步骤，总共操作三次。将最后一次余下的蓍草数量除以4，记录下得数，9代表老阳，即变化的阳爻，8代表老阴，即不变的阴爻，7代表少阳，即不变的阳爻，6代表少阴，即变化的阳爻，这样就得到了第一爻，记录在最底下。然后重新用49根蓍草重复以上的步骤，得到第二、第三……直到第六爻，分别从下到上排列。这样就得到了整个卦。


1 Introduction

1.1 Yarrow stalks divination

(I'm too lazy to explain the process in English.) That website introduces the process of this kind of divination: https://www.ichi-ng.com/divination/divination-yarrow-stalks/




1.2 解卦法

这里介绍一种主流的解法和一种较冷门的解法[2]。

a) 如果得到的卦象中，没有任何一个变爻，则参考本卦的卦象；存在一个变爻，则参考本卦该爻的爻辞；存在两个变爻，参考本卦这两个爻的爻辞，以上面的变爻爻辞为主；存在三个变爻，则将变爻的阳变阴，阴变阳，得到变卦（之卦），以本卦和之卦的卦辞为参考；存在四个变爻，同样的方法得到之卦，以不变的两爻在之卦中对应的爻辞为参考，以上面的不变爻爻辞为主；存在五个变爻，以不变爻在之卦中对应的爻辞为参考；存在六个变爻，如果是乾或坤两卦，则以“用九”或“用六”之辞为参考，其他卦象则以之卦卦辞为参考。

b) 将六个爻对应的数字（9，8，7，6）全部相加，用55减去这个和，得到一个差值。从下往上数爻，数到头后再重新从上往下数，不断地数到等于差值为止，数到的那一爻为宜变之爻。如果宜变之爻刚好就是变爻，则用方法a的步骤寻找需要参考的爻辞；如果宜变之爻不是变爻，若变爻数量少于3，则以本卦的卦辞为参考，若变爻数量大于3，则以之卦卦辞为参考，若变爻数量等于三，则两卦卦象均为参考。


1.2 Interpretation of the "gua" (hexagram)

Here I introduce one mainstream method to interpret and a less used one.

a) If there is no changing line in the hexagram, read the text of the hexagram itself;

   If there is one changing line in the hexagram, read the text of this line of the hexagram;
   
   If there are two changing lines, read the text of this two lines of the hexagram and the upper line's text has the prioriry.
   
   If there are three chaning lines, change all the changing line from solid to broken or from broken to solid, then you have the changed hexagram, read the text of the original hexagram itself and the changed hexagram itself;
   
   If there are four chaging lines, change the hexagram in the same way above, read the text of tow static lines of the changed hexagram and the upper lines's text has the priority;
   
   If there are five changing lines, change the hexagram, read the text of the static line of the changed hexagram.
   
   If both six lines changes, change the hexagram ,read the text of the changed hexagram itself. In this case, if the original hexagram is "qian" (heaven) or "kun" (earth), read the text named "yong jiu" (in "qian") or "yong liu" (in "kun") rather than the text of changed hexagram.
   
b) Add up all the numbers of the six lines (9, 8, 7, 6), use 55 to minus the sum, count the lines from buttom to top and then from top to bottom, repeat untill the number equals to the difference. The line where you stop is the line that could be changed. If this line is a changing line, follow the method a. If this line is not a changing line, count the changing line(s). If the number less than 3, read the text of the hexagram itself. If the number larger than 3, change the hexagram and read the text of the changed hexagram itself. If the number equals to 3, read text of both the original and changed hexagram themselves.




2 算法

我用md5算法将输入的问题转化为哈希值，用十进制记录。然后将年月日时分秒按顺序写成一个整数。将十进制哈希值与这个整数相加，作为随机函数的种子。随机分布使用（0，1）分布，将重复n次随机试验后将所有结果相加，得到的值作为被分开的一堆蓍草的数量，另一堆的数量也可以相应的到，然后再根据蓍草成卦法的规则重复操作、计算获得的爻和卦。


2 Algorithm

I use md5 to transform the question to hash value, record it in decimal. Then transform the time to a integer number in the order of YYYYmmddHHMMSS. The two number are added up and used as the random seed. I choose the 0-1 distrobution and repeat the test n times. The sum of those tests is considered as the number of yarrows in one side. Then followed the rule of Yarrow stalks divination, the lines and hexagram are found.


参考文献

[1] 王晓刚, 李德才. 《周易》筮法溯源初探[J]. 内蒙古民族大学学报(自然科学版), 2021, 36(02): 103-108. DOI: 10.14045/j.cnki.15-1220.2021.02.003.
[2] 高亨. 周易筮法新考 高亨著作集林[第一卷][M]. 董治安. 清华大学出版社. 北京, 2004:164.
