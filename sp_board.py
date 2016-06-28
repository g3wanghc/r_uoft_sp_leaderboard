import praw
import sys
from datetime import datetime
from s_stat import S_Stat

subreddit = 'uoft'

r = praw.Reddit('SP-Score Leaderboard')

r_uoft = r.get_subreddit('uoft')
posts = r_uoft.get_top_from_month(limit=None)

s_board = dict()

for p in posts:
	if p.link_flair_text != None:
		if p.link_flair_text == 'Shitpost':
			if p.author.name in s_board:
				p_s_stat = s_board[p.author.name]
				p_s_stat.posts_count += 1
				p_s_stat.score += p.score
			else:
				s_board[p.author.name] = S_Stat(p.author.name, 1, p.score,)

print ("S-Score Leaderboard:", datetime.now().strftime("%B, %Y"))
for user_s_stat in sorted(s_board.values(), key=lambda p_s_stat: p_s_stat.score, reverse=True):
	print(user_s_stat)
	sys.stdout.flush()
