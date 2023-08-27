"""
九九乘法表:
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
...
1*9=9 2*9=18 3*9=27... 9*9=81

分析：
1：共有9层
2：每一层的被乘数是和层有关系的
3：每一层的乘数是依次加1的
"""

ceng=1
while ceng<=9:
    count=1
    while count<=ceng:
      print(f'{count}*{ceng}={count*ceng}',end='')
      count+=1
    print()
    ceng+=1

