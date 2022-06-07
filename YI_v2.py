# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:44:30 2022

@author: sheng
"""

import os
import time
import random
import hashlib

def listen(question: str):
    md = hashlib.md5()
    md.update(question.encode('utf-8'))
    return int(md.hexdigest(), 16)

def yao(q: int, n: int):
    random.seed(q + int(time.strftime('%Y%m%d%H%M%S'), 10))
    for i in range(3):
        c = 0
        for j in range(n):
            c = c + random.randint(0, 1)
        left = c - 1
        right = n - c
        leftl = left % 4
        rightl = right % 4
        if (leftl == 0) & (int(left/4) != 0):
            leftl = 4
        if (rightl == 0) & (int(right/4) != 0):
            rightl = 4
        n = n - leftl - rightl -1
    return int(n/4)

def draw(Y: list, total: int):
    f = open('YI_log.txt', 'a', encoding=('utf-8'))
    print("本卦卦象为：")
    f.write("本卦卦象为：" + '\n')
    ch = 0
    num = 0
    change_i =  abs((1-int((54-total)/6)%2)*5 - ((54-total)%6))
    for i in range(6):
        y = Y[5-i]
        if y == 9:
            out = ' --- *'
            ch = ch + 1
            num = num + 2**(5-i)
        elif y == 8:
            out = ' - -  '
        elif y == 7:
            out = ' ---  '
            num = num + 2**(5-i)
        elif y == 6:
            out = ' - - *'
            ch = ch + 1
        if i == change_i:
            print(out + ' x')
            f.write(out + 'x' + '\n')
        else:
            print(out)
            f.write(out + '\n')
    print("本卦为" + order[num] + "卦")
    f.write("本卦为" + order[num] + '\n')
    print("宜变之爻为（从下往上）第" + str(6-change_i) + "爻")
    f.write("宜变之爻为（从下往上）第" + str(6-change_i) + "爻" + '\n')
    if ch >= 3:
        num = 0
        print('----------')
        f.write('----------' + '\n')
        print("变爻多于二爻，变卦卦象为：")
        f.write("变爻多于二爻，变卦卦象为：" + '\n')
        for i in range(6):
            y = Y[5-i]
            if y == 9:
                out = ' - - *'
            elif y == 8:
                out = ' - - '
            elif y == 7:
                out = ' ---  '
                num = num + 2**(5-i)
            elif y == 6:
                out = ' --- *'
                num = num + 2**(5-i)
            if i == change_i:
                print(out + ' x')
                f.write(out + ' x' + '\n')
            else:
                print(out)
                f.write(out + '\n')
        print("变卦为" + order[num] + "卦")
        f.write("变卦为" + order[num] + "卦" + '\n')
    print('\n'*2)
    f.write('\n'*2)
    f.close()
    return 0

def main(string: str):
    Y = []
    total = 0
    q = listen(string)
    for i in range(6):
        print("\r占第 " + str(i) + " 爻", end=' ')
        y = yao(q, 49)
        Y.append(y)
        total = total + y
        time.sleep(1)
    print('\r==========')
    f = open('YI_log.txt', 'a', encoding=('utf-8'))
    f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n')
    f.write("占问：" + string + '\n')
    f.close()
    draw(Y, total)
    

if __name__ == "__main__":
    order = ['坤','复','师','临','谦','明夷','升','泰',
             '豫','震','解','归妹','小过','丰','恒','大壮',
             '比','屯','坎','节','蹇','既济','井','需',
             '萃','随','困','兑','咸','革','大过','夬',
             '剥','颐','蒙','损','艮','贲','蛊','大畜',
             '晋','噬嗑','未济','睽','旅','离','鼎','大有',
             '观','益','涣','中孚','渐','家人','巽','小畜',
             '否','无妄','讼','履','遁','同人','姤','乾',
             ]#以阴爻为0，阳爻为1，从下到上依次为低位到高位，如坤为000000，复为000001，师为000010
    while(True):
        string = input("请说出占问之事：")
        if string == "再见":
            break
        main(string)
        print("=输入“再见”以结束=")
    