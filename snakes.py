import re
import sys

followers = ''
following = ''
followerList = []
followingList = []


with open("SnakeFinder/following.html", "r", encoding='utf-8') as f:
    following = str(f.read())

with open("SnakeFinder/followers.html", "r", encoding='utf-8') as f:
    followers = str(f.read())


def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)


partiallyRefinedFollowers = ([(i, followers[i:i+44])
                              for i in findall('instagram.com/', followers)])
partiallyRefinedFollowing = ([(i, following[i:i+44])
                              for i in findall('instagram.com/', following)])


for follower in partiallyRefinedFollowers:
    s = str(follower)
    result = re.search('/(.*)"', s)
    followerList.append(result.group(1))

for follow in partiallyRefinedFollowing:
    s = str(follow)
    result = re.search('/(.*)"', s)
    followingList.append(result.group(1))

# Find who follows back
followBack = []

for follow in followingList:
    for follower in followerList:
        if follow == follower:
            # print(f"{follower} follows back! <3")
            followBack.append(follow)
# Weed out the snakes
snakes = []

for follow in followingList:
    if follow not in followerList:
        snakes.append(follow)


def Choice(action):
    match action:
        case 1:
            alphabetizedSnakes = sorted(snakes)
            for snake in alphabetizedSnakes:
                print(snake)
        case 2:
            directory = input(
                "Please provide a path to the directory you would like to export the report to: ")
            with open(f"{directory}/snakes.txt", 'w') as f:
                for item in snakes:
                    f.write(f"{item}\n")
        case 3:
            print("bye")
            sys.exit()
        case _:
            print("Not sure what you entered. ")


while True:
    print(f"You have {len(followBack)} followers that follow you back")
    print(f"You have {len(snakes)} snakes")

    action = int(input(
        "Press 1 to list your snakes. Press 2 to export a detailed report. type 3 to quit: "))
    Choice(action)
