import sys

def convert_to_excel(row, col):
   s = ""
   while col:
      m = (col - 1) % 26

      col = (col - 1) // 26

      s = chr(65 + m) + s
   return s + str(row)

def convert_from_excel(s):
    r = 0
    for i in s:
       r = r * 26 + ord(i) - 64

    return r

def solve():
   n_str = sys.stdin.readline()
   if not n_str:
      return
   n = int(n_str)

   for _ in range(n):
      s = sys.stdin.readline().strip()

      is_rc = False
      if s[0] ==  'R' and s[1].isdigit():
         try:
            c_index = s.index('C', 2)
            if s[c_index + 1].isdigit():
               is_rc = True
         except ValueError:
            pass

      if is_rc:
         r_str = ""
         c_str = ""
         i = 1
         while i < len(s) and s[i].isdigit():
            r_str += s[i]
            i += 1

         c_str = s[i + 1:]

         row = int(r_str)
         col = int(c_str)
         print(convert_to_excel(row, col))
      else:
         col_str = ""
         row_str = ""
         i = 0
         while i < len(s) and not s[i].isdigit():
            col_str += s[i]
            i += 1
         row_str = s[i:]

         col = convert_from_excel(col_str)
         row = int(row_str)
         print(f"R{row}C{col}")

if __name__ == "__main__":
   solve()