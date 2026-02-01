import sys
from collections import defaultdict

def solve():
   try:
      n = int(sys.stdin.readline())
   except:
      return

   rounds_data = []
   final_scores = defaultdict(int)

   for _ in range(n):
      line = sys.stdin.readline().split()
      if not line:
         continue
      name = line[0]
      score = int(line[1])
      rounds_data.append((name, score))

      final_scores[name] += score

   max_score = -float('inf')
   for score in final_scores.values():
      if score > max_score:
         max_score = score

   potential_winners = {name for name, score in final_scores.items() if score == max_score}

   current_scores = defaultdict(int)

   winner = ""

   for name, score in rounds_data:
      current_scores[name] += score
      if name in potential_winners and current_scores[name] >= max_score:
         winner = name
         break


   print(winner)


if __name__ == "__main__":
   solve()