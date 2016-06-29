from string import Template


class S_Stat:
    def __init__(self, user_name, posts_count=0, score=0):
        self.user_name = user_name
        self.posts_count = posts_count
        self.score = score

    def __str__(self):
        s = Template(
            '--------------------------------- \n' +
            'Username: \t $user \n' +
            'S-Posts Count: \t $posts_count \n' +
            'Score: \t\t $score'
            )
        return s.substitute(user=self.user_name,
                            posts_count=self.posts_count, score=self.score)
