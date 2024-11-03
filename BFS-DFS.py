from collections import deque

def is_seller(name, jobs):
    if (jobs[name]=='mango'):
        return True
    else:
        return False

def breadth_first_search(name, friends_graph, jobs):
    search_queue = deque()
    search_queue += friends_graph[name]
    searched_friends = set()
    while (search_queue):
        person = search_queue.popleft()
        if (not person in searched_friends):
            if(is_seller(person, jobs)):
                return f'{person} is a mango seller, congrats ya basha'
            else:
                search_queue += friends_graph[person]
                searched_friends.add(person)
    return 'no mango sellers. hahaha, why dont you try lemons'

def depth_first_search(name, friends_graph, jobs):
    search_stack = deque()
    search_stack += friends_graph[name]
    searched_friends = set()
    while (search_stack):
        person = search_stack.pop()
        if (not person in searched_friends):
            if(is_seller(person, jobs)):
                return f'{person} is a mango seller, congrats ya basha'
            else:
                search_stack += friends_graph[person]
                searched_friends.add(person)
    return 'no mango sellers. hahaha, why dont you try lemons'


name='me/you'
friends_graph = {
    'me/you':['alice','bob','claire'],
    'alice':['peggy','moha'],
    'bob':['anuj','peggy','a7mos'],
    'claire':['thom','jonny'],
    'peggy':[], 'moha':[], 'anuj':[], 'a7mos':[], 'thom':[], 'jonny':[]
}
jobs = {
   'alice':'aa', 'bob':'bb', 'claire':'cc', 'peggy':'dd', 'moha':'ee', 'anuj':'ff', 'a7mos':'mango', 'thom':'hh', 'jonny':'mango'
}

print(breadth_first_search(name, friends_graph, jobs))
print(depth_first_search(name, friends_graph, jobs))