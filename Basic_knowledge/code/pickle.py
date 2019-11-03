import pickle

a_dict = {'da': 111, 2: [23, 1, 3], '23': {1: 2, 'd': 'sad'}}

file = open(
    'd:/TOFU/Github/github_learn//VSCode_git_github/' +
    'Python/Basic_knowledge/pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# file = open(
#     'd:/TOFU/Github/github_learn//VSCode_git_github/' +
#     'Python/Basic_knowledge/pickle_example.pickle', 'rb')

# a_dict1 = pickle.load(file)
# file.close()

# 简化写法
# with open(
#     'd:/TOFU/Github/github_learn//VSCode_git_github/' +
#     'Python/Basic_knowledge/pickle_example.pickle', 'rb'
# ) as file:
#     a_dict1 = pickle.load(file)
# print(a_dict1)
# 输出结果 {'da': 111, 2: [23, 1, 3], '23': {1: 2, 'd': 'sad'}}
