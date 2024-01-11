# 数値型

value = 1
# print(value)
# value = -2
# print(value)
# value = value + 4 #2
# print(value)
# print(value * 4) # 8
# print(value / 3) # 0.6666
# value = 10
# print(value // 3) # 3
# print(value % 3) # 1

value += 3 # value = value + 3
# value -= 2 # value = value -2 * /

# print(value)
# print(value ** 3) #64

# 浮動小数点数
height = 175.5

print(height)
print(type(height))
print(height + 10) #175.5 + 10.0

value = 8 # 1000 => 0010
print(value >> 2)
print(value << 3) # 1000 => 1000000
""" 
上記のコードでは、value という変数に8を代入しています。8は2進数で 1000 と表されます。

- value >> 2 は右シフト演算を行います。つまり、value のビット列を右に2ビット移動させます。
この結果、1000 (8) は 10 (2) になります。したがって、print(value >> 2) の出力は 2 になります。

- value << 3 は左シフト演算を行います。つまり、value のビット列を左に3ビット移動させます。
この結果、1000 (8) は 1000000 (64) になります。したがって、print(value << 3) の出力は 64 になります。

これらのシフト演算は、主に低レベルのプログラミングやパフォーマンスが重要な場合に使用されます。
"""

print(12 & 21) # 01100 and 10101 = 00100 => 4
print(12 | 21) # 01100 or 10101 = 11101 => 29

value = 12
value &= 21 # value = value & 21
print(value)