import random

'''
player玩家手上有的牌
'''
player_a=[1,2,3,4,5,6,7,8,9,10,11,12]
player_b=[1,2,3,4,5,6,7,8,9,10,11,12]
player_c=[1,2,3,4,5,6,7,8,9,10,11,12]
player_d=[1,2,3,4,5,6,7,8,9,10,11,12]

'''
size玩家累積數字大小
'''
size_a=0
size_b=0
size_c=0
size_d=0

'''
point玩家點數
'''
points_a=0
points_b=0
points_c=0
points_d=0

for j in range(3):
    for i in range(3):
    
        '''
        你當首領
        '''
        print("你是首領")
        print("你的牌庫",player_a)
        card_a=int(input("請出牌"))
        print("********")
        player_a.remove(card_a)
        print("你出了"+str(card_a))
    
        card_b=random.choice(player_b)
        player_b.remove(card_b)
        print("玩家2出了"+str(card_b))
    
        card_c=random.choice(player_c)
        player_c.remove(card_c)
        print("玩家3出了"+str(card_c))
    
        card_d=random.choice(player_d)
        player_d.remove(card_d)
        print("玩家4出了"+str(card_d))
        print("---------")
        
        if card_a==card_b or card_a==card_c or card_a==card_d:
            size_a=size_a-card_a
            print("你扣"+str(card_a)+"分")
            if card_b>card_a:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b==card_a:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            elif card_b<card_a:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
                
            if card_c>card_a:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c==card_a:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            elif card_c<card_a:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            
            if card_d>card_a:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d==card_a:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
            elif card_d<card_a:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
                
        elif card_a!=card_b and card_a!=card_c and card_a!=card_d:
            size_a=size_a+card_a
            print("你加"+str(card_a)+"分")
            if card_b>card_a:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b<card_a:
                size_b=size_b+card_a
                print("玩家2加"+str(card_b)+"分")
                
            if card_c>card_a:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c<card_a:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            
            if card_d>card_a:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d<card_a:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
        print("---------")
        
        '''
        玩家2當首領
        '''
        print("玩家2是首領")
        print("你的牌庫",player_a)
        card_a=int(input("請出牌"))
        print("********")
        player_a.remove(card_a)
        print("你出了"+str(card_a))
            
        card_b=random.choice(player_b)
        player_b.remove(card_b)
        print("玩家2出了"+str(card_b))
            
        card_c=random.choice(player_c)
        player_c.remove(card_c)
        print("玩家3出了"+str(card_c))
            
        card_d=random.choice(player_d)
        player_d.remove(card_d)
        print("玩家4出了"+str(card_d))
        print("---------")
            
        if card_b==card_a or card_b==card_c or card_b==card_d:
            size_b=size_b-card_b
            print("玩家2扣"+str(card_b)+"分")
            if card_a>card_b:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a==card_b:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
            elif card_a<card_b:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_c>card_b:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c==card_b:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            elif card_c<card_b:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            
            if card_d>card_b:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d==card_b:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
            elif card_d<card_b:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
        elif card_b!=card_a and card_b!=card_c and card_b!=card_d:
            size_b=size_b+card_b
            print("玩家2加"+str(card_b)+"分")
            if card_a>card_b:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a<card_b:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_c>card_b:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c<card_b:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            
            if card_d>card_b:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d<card_b:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
        print("---------")
        
        '''
        玩家3當首領
        '''
        print("玩家3是首領")
        print("你的牌庫",player_a)
        card_a=int(input("請出牌"))
        print("********")
        player_a.remove(card_a)
        print("你出了"+str(card_a))
            
        card_b=random.choice(player_b)
        player_b.remove(card_b)
        print("玩家2出了"+str(card_b))
            
        card_c=random.choice(player_c)
        player_c.remove(card_c)
        print("玩家3出了"+str(card_c))
            
        card_d=random.choice(player_d)
        player_d.remove(card_d)
        print("玩家4出了"+str(card_d))
        print("---------")
        
        if card_c==card_a or card_c==card_b or card_c==card_d:
            size_c=size_c-card_c
            print("玩家3扣"+str(card_c)+"分")
            if card_a>card_c:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a==card_c:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
            elif card_a<card_c:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_b>card_c:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b==card_c:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            elif card_b<card_c:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            
            if card_d>card_c:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d==card_c:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
            elif card_d<card_c:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
        elif card_c!=card_a and card_c!=card_b and card_c!=card_d:
            size_c=size_c+card_c
            print("玩家3加"+str(card_c)+"分")
            if card_a>card_c:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a<card_c:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_b>card_c:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b<card_c:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            
            if card_d>card_c:
                size_d=size_d-card_d
                print("玩家4扣"+str(card_d)+"分")
            elif card_d<card_c:
                size_d=size_d+card_d
                print("玩家4加"+str(card_d)+"分")
        print("---------")
        
        '''
        玩家4當首領
        '''
        print("玩家4是首領")
        print("你的牌庫",player_a)
        card_a=int(input("請出牌"))
        print("********")
        player_a.remove(card_a)
        print("你出了"+str(card_a))
            
        card_b=random.choice(player_b)
        player_b.remove(card_b)
        print("玩家2出了"+str(card_b))
            
        card_c=random.choice(player_c)
        player_c.remove(card_c)
        print("玩家3出了"+str(card_c))
            
        card_d=random.choice(player_d)
        player_d.remove(card_d)
        print("玩家4出了"+str(card_d))
        print("---------")
        
        if card_d==card_a or card_d==card_b or card_d==card_c:
            size_d=size_d-card_d
            print("玩家4扣"+str(card_d)+"分")
            if card_a>card_d:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a==card_d:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
            elif card_a<card_d:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_b>card_d:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b==card_d:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            elif card_b<card_d:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            
            if card_c>card_d:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c==card_d:
                size_d=size_d+card_d
                print("玩家3加"+str(card_c)+"分")
            elif card_c<card_d:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
        elif card_d!=card_a and card_d!=card_b and card_d!=card_c:
            size_d=size_d+card_d
            print("玩家4加"+str(card_d)+"分")
            if card_a>card_d:
                size_a=size_a-card_a
                print("你扣"+str(card_a)+"分")
            elif card_a<card_d:
                size_a=size_a+card_a
                print("你加"+str(card_a)+"分")
                
            if card_b>card_d:
                size_b=size_b-card_b
                print("玩家2扣"+str(card_b)+"分")
            elif card_b<card_d:
                size_b=size_b+card_b
                print("玩家2加"+str(card_b)+"分")
            
            if card_c>card_d:
                size_c=size_c-card_c
                print("玩家3扣"+str(card_c)+"分")
            elif card_c<card_d:
                size_c=size_c+card_c
                print("玩家3加"+str(card_c)+"分")
            print("---------")

    '''
    判斷分數高低
    '''
    if size_a>size_b and size_a>size_c and size_a>size_d:
        points_a=points_a+2
        print("你加2點")
        if size_b>size_c and size_b>size_d:
            points_b=points_b+1
            print("玩家2加1點")
        elif size_c>size_b and size_c>size_d:
            points_c=points_c+1
            print("玩家3加1點")
        elif size_d>size_b and size_d>size_c:
            points_d=points_d+1
            print("玩家4加1點")
    elif size_b>size_a and size_b>size_c and size_b>size_d:
        points_b=points_b+2
        print("玩家2加2點")
        if size_a>size_c and size_a>size_d:
            points_a=points_a+1
            print("你加1點")
        elif size_c>size_a and size_c>size_d:
            points_c=points_c+1
            print("玩家3加1點")
        elif size_d>size_a and size_d>size_c:
            points_d=points_d+1
            print("玩家4加1點")
    elif size_c>size_a and size_c>size_b and size_c>size_d:
        points_c=points_c+2
        print("玩家3加2點")
        if size_a>size_b and size_a>size_d:
            points_a=points_a+1
            print("你加1點")
        elif size_b>size_a and size_b>size_d:
            points_b=points_b+1
            print("玩家2加1點")
        elif size_d>size_a and size_d>size_b:
            points_d=points_d+1
            print("玩家4加1點")
    elif size_d>size_a and size_d>size_b and size_d>size_c:
        points_d=points_d+2
        print("玩家4加2點")
        if size_a>size_b and size_a>size_c:
            points_a=points_a+1
            print("你加1點")
        elif size_b>size_a and size_b>size_c:
            points_b=points_b+1
            print("玩家2加1點")
        elif size_c>size_a and size_c>size_b:
            points_c=points_c+1
            print("玩家3加1點")
    if size_a<size_b and size_a<size_c and size_a<size_d:
        points_a=points_a-1
        print("你扣1點")
    elif size_b<size_a and size_b<size_c and size_b<size_d:
        points_b=points_b-1
        print("玩家2扣1點")
    elif size_c<size_a and size_c<size_b and size_c<size_d:
        points_c=points_c-1
        print("玩家3扣1點")
    elif size_d<size_a and size_d<size_c and size_d<size_b:
        points_d=points_d-1
        print("玩家4扣1點")
        print("        ")
    player_a=[1,2,3,4,5,6,7,8,9,10,11,12]
    player_b=[1,2,3,4,5,6,7,8,9,10,11,12]
    player_c=[1,2,3,4,5,6,7,8,9,10,11,12]
    player_d=[1,2,3,4,5,6,7,8,9,10,11,12]
print("你的點數有"+str(points_a)+"點")
print("玩家2的點數有"+str(points_b)+"點")
print("玩家3的點數有"+str(points_c)+"點")
print("玩家4的點數有"+str(points_d)+"點")