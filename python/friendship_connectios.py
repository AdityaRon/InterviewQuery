#How Many Friends
# You are given a list of lists where each group represents a friendship.

# For example, given the list:

# list = [[2,3],[3,4],[5]]
# Person 2 is friends with person 3, person 3 is friends with person 4, etc. 

# Write a function to find how many friends each person has. 

def how_many_friends(test_input: list[list]):
    friendships_dict = {}
    # friendships_count = {}
    # for friendship_pairs in test_input:
    #     if len(friendship_pairs) == 1:
    #         friendships_dict[friendship_pairs[0]] = 0
    #     else:
    #         friendships_dict[friendship_pairs[0]] = friendship_pairs[1]
    # for i in friendships_dict.keys():
    #     if friendships_dict[i] != 0:
    #         friendships_count[i] = 1
    #     else:
    #          friendships_count[i] = 0
    # for j in friendships_dict.values():
    #     if j !=0:
    #         friendships_count[j] =  friendships_count.get(j,0) + 1
    # return tuple(friendships_count.items())
    for friendships in test_input:
        for friend in friendships:
            if friend not in friendships_dict:
                print(set(friendships), set([friend]))
                friendships_dict[friend] = set(friendships) - set([friend])
            else:
                friendships_dict[friend].update(set(friendships) - set([friend]))
    print(friendships_dict)
    return tuple([(key, len(value)) for key, value in friendships_dict.items()])
