import time

class eightPazzuleKanri():


    nokoritesu=100

    zikan=0
    set=0
    stop=0

    modeNo=0#0:横並び(デフォルト) 1:縦並び

    besttime=''#テキストファイルの文字入れる変数

    #ベストタイム初期値格納
    f=open('besttime.txt','r',encoding='utf-8')
    besttime=f.read()#ベストタイム
    f.close()

    yousobango=0 #memori配列の空の最初の要素番号
    memori=[]#一手ずつ場所を格納していく（二次元配列)



    def setTime(self):#初めの時間を保存
        # 処理前の時刻
        self.set = time.time() 

        
    def stopTime(self):#終わりの時間を保存して、経過時間返す
        
        # 処理後の時刻
        self.stop = time.time()
        
        # 経過時間を表示

        
        self.zikan += int(self.stop-self.set)#経過時間更新

        #print(f"経過時間：{int(self.stop-self.set)}")
        #print(str(int(self.zikan)),'秒')
    
    def setbesttime(self):#ベストタイム更新したらTrue,なにもなかったらFalseを返す

        if self.zikan<self.suuchtoridasi(self.besttime) or 0==self.suuchtoridasi(self.besttime) :
            f=open('besttime.txt','w',encoding='utf-8')#上書き
            f.write(str(self.zikan)+'秒')
            f.close()
            self.besttime=str(self.zikan)+'秒'
            print(self.besttime)
            return True#更新
        
        return False

    def suuchtoridasi(self,moziretu):#文字列にある数字を取り出す

        strnum=['0','1','2','3','4','5','6','7','8','9']

        num=[0,1,2,3,4,5,6,7,8,9]
        suji=int(0)

        for i in moziretu:
            
            print(i)
            
            for j in range(len(strnum)):

                if i==strnum[j]:

                    suji*=10
                    suji+=num[j]
        
        return suji

    def tarnkousin(self,modorunum):

        self.memori.append(modorunum)#変える数字を保存

        print('格納します')

        print(self.memori)

        self.yousobango+=1

    def getmae(self):#一手前に戻るときの状態を返す


        #memoriを取り消す分消す
        self.yousobango-=1
        print(self.memori)
        return self.memori.pop(self.yousobango)


a=eightPazzuleKanri()









