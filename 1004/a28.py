import sys

print("参数總長度：", len(sys.argv))
print("type:", type(sys.argv))
print("function name:", sys.argv[0])
try:
    print("第一個參數:", sys.argv[1])
    print("第二個參數:", sys.argv[2])
except Exception as e:
    print("Input Error:", e)