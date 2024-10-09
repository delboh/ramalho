# Example 2-1. Build a list of Unicode codepoints from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
     codes.append(ord(symbol))

print(codes)

# Example 2-2. Build a list of Unicode codepoints from a string using a list comprehension
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)