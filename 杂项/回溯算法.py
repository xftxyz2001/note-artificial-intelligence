class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


# 创建结点
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')
L = Node('L')
M = Node('M')
N = Node('N')
O = Node('O')
P = Node('P')
Q = Node('Q')
R = Node('R')

# 构建树
A.children = [B, C, D]
B.children = [E, F, G]
C.children = [G]
D.children = [H, I]
E.children = [J, K, L]
F.children = [L, A]
G.children = [M, N, H]
H.children = [O, P, A]
I.children = [P, R]


# 状态变量
SL = [A]
NSL = [A]
DE = []
CS = A

counter = -1


def list_print(l):
    print('[' + ', '.join([str(i) for i in l]) + ']', end='\t\t\t')


def status_print():
    global counter
    counter += 1
    global SL, NSL, DE, CS
    print(counter, '\t', CS, end='\t')
    list_print(SL)
    list_print(NSL)
    list_print(DE)
    print()


status_print()
while NSL:
    # goal
    cscs = []  # CS.children not in DE, SL, NSL
    for csc in CS.children:
        if csc not in DE and csc not in SL and csc not in NSL:
            cscs.append(csc)
    if not cscs:
        while SL and CS == SL[0]:
            DE.insert(0, CS)
            SL.pop(0)
            NSL.pop(0)
            CS = NSL[0]
        SL.insert(0, CS)
    else:
        NSL = cscs + NSL
        CS = NSL[0]
        SL.insert(0, CS)
    status_print()
