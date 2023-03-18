import random
when = ['A few years ago', 'Daybefore yesterday', 'Last night', 'A long time ago','On 30th Dec']
who = ['a rabbit', 'an elephant', 'a mouse', 'a lion','a cat']
name = ['Asif', 'Miriam','David', 'Hoouk', 'Starwalker']
residence = ['China','India', 'Saudi Arabia', 'Afganistan', 'England']
went = ['cinema', 'university','webinar', 'class', 'zoo']
happened = ['made a lot of friends','Eats a pizza', 'found a secret key', 'solved a mystery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) +
 ', went into the ' + random.choice(went) + ' and ' + random.choice(happened))