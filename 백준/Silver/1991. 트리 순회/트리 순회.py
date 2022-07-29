tree = {} # Dictionary (Tree)
cnt = int(input())

for i in range(cnt):
    tmp = str(input()).split(' ')
    if tmp[0] not in tree.keys():
        tree[tmp[0]] = ['.', '.']
    tree[tmp[0]][0] = tmp[1]
    tree[tmp[0]][1] = tmp[2]

def preorder(root):
    if root == '.':
        return;
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.':
        return;
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
    if root == '.':
        return;
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')