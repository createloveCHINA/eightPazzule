import tkinter as tk
from tkinter import messagebox
import random
import eightPazzuleKanri

kanri=eightPazzuleKanri.eightPazzuleKanri()
#クリックイベントの定義
def clickPice(event):
    num=int(event.widget['text'])#クリックされた数字を取得
    changePice(num)

def close(event):#閉じるポップアップ処理
    messagebox.showinfo('完成',message='8パズルをクリアしました')#ポップアップ表示

    if kanri.setbesttime()==True:#ベストタイム更新した

        messagebox.showinfo('更新',message='ベストタイムを更新しました')#ポップアップ表示


    root.destroy()#ウィンドウを閉じる

def notclose():#閉じないポップアップ処理

    messagebox.showinfo('失敗',message='完成しませんでした')#ポップアップ表示

    #if kanri.setbesttime()==True:#ベストタイム更新した

        #messagebox.showinfo('更新',message='ベストタイムを更新しました')#ポップアップ表示
        #besttime2.configure(text=kanri.besttime)





def gameover(event):
    messagebox.showinfo('負け',message='完成しませんでした')#ポップアップ表示
    root.destroy()#ウィンドウを閉じる

def risetto():

    kanri.stopTime()
    kanri.set=0
    kanri.stop=0
    notclose()#完成しませんでした　ベストタイム更新

    #ランダム配置しなおす
    randomchange()
    #画像セットしなおす
    for idx in range(1,10):
        pice_label_dict[idx].configure(text=pice_dict[idx],image=pice_image[pice_dict[idx]])
    
    #一手戻れないようにする
    kanri.yousobango=0
    del kanri.memori[:]


    #残りて数の初期化
    kanri.nokoritesu=100
    tesu2.configure(text=kanri.nokoritesu)

    #経過時間の初期か
    kanri.zikan=0
    time2.configure(text=str(kanri.zikan)+'秒')



def modechange():#モード変更する

    if kanri.modeNo==0:
        kanri.modeNo=1
        setanswer()
        mode2.configure(text='縦並び')

    else:
        kanri.modeNo=0
        setanswer()
        mode2.configure(text='横並び')

def setanswer():#解答セット

    if kanri.modeNo==0:
        answer=[1,2,3,4,5,6,7,8,0]
        for idx in range(1,10):
            
            answer_dict[idx]=answer[idx-1]#横並びセット
        
    else:
        answer=[1,4,7,2,5,8,3,6,0]
        for idx in range(1,10):
            answer_dict[idx]=answer[idx-1]#縦並びセット

def modoru():
    
    if not kanri.yousobango==0:
        kanri.nokoritesu+=1#手数+１
        #表示する残り手数文字入れ替え
        tesu2.configure(text=kanri.nokoritesu)

        #一つ前の並びにセット
        modorunum=kanri.getmae() #変更する前のゼロの位置、入れ替える数の位置、入れ替える数

        print('配列ポップ')
        print(modorunum)

        #クリックされた数字の表示位置と、０の表示位置を特定する
        idx=searchPiceIndex(modorunum)
        zero_idx=searchPiceIndex(0)#0の場所探す

        #ピース位置管理の入替(SearchPiceIndexメソッドで位置検索に利用する辞書データ)
        pice_dict[idx]=0
        pice_dict[zero_idx]=modorunum

        #画像も
        pice_label_dict[idx].configure(image=pice_image[0])#空白ピースへ入替
        pice_label_dict[zero_idx].configure(image=pice_image[modorunum])#空白ピースへ入替

        #表示するピースの文字入替
        pice_label_dict[idx].configure(text=0)
        pice_label_dict[zero_idx].configure(text=modorunum)
        


#指定した数字のピースと、０のピースを入れ替える

def  changePice(num):

    if canSwapSpacePice(num)==True:

        
        kanri.nokoritesu-=1 
        #表示する残り手数文字入れ替え
        tesu2.configure(text=kanri.nokoritesu)


        #クリックされた数字の表示位置と、０の表示位置を特定する
        idx=searchPiceIndex(num)
        zero_idx=searchPiceIndex(0)#0の場所探す
        
        #入れ替える数
        kanri.tarnkousin(num)#今から変える前に、入れ替える数を保存
        

        #ピース位置管理の入替(SearchPiceIndexメソッドで位置検索に利用する辞書データ)
        pice_dict[idx]=0
        pice_dict[zero_idx]=num
        #画像も
        pice_label_dict[idx].configure(image=pice_image[0])#空白ピースへ入替
        pice_label_dict[zero_idx].configure(image=pice_image[num])#空白ピースへ入替

        #表示するピースの文字入替
        pice_label_dict[idx].configure(text=0)
        pice_label_dict[zero_idx].configure(text=num)

        #初めての1手の時間計測開始

        if kanri.nokoritesu==99:
            kanri.setTime()#この時点の時間から計測開始

        else:
            kanri.stopTime()#いったんこの時点の時間を更新
            time2.configure(text=str(kanri.zikan)+'秒')
            kanri.setTime()#この時点の時間から計測開始

    #並び変えた地所と解答が一致したらゲームを終了とする
    if pice_dict==answer_dict:
        close(True)
    elif kanri.nokoritesu==0:
        gameover(True)
    
def randomchange():#ランダムに並べ替える
    pice_numbers=[0,1,2,3,4,5,6,7,8]#表示する番号の種類
    #pice_numbers=[1,2,3,4,5,6,7,0,8]#表示する番号の種類
    random_pice_list=random.sample(pice_numbers,9)#表示する番号をランダムに並び替え
    #random_pice_list=pice_numbers
    for idx in range(1,10):
        pice_dict[idx]=random_pice_list[idx-1]#pice_dictにランダムな値をセット
    

    
#指定された番号が、どの位置に表示されているかを返却する
def searchPiceIndex(pice_num):
    for idx,num in pice_dict.items():
        if pice_num==num:
            return idx

def canSwapSpacePice(num):
    """
    指定した数字の上下左右に「０番」が隣接しているか判断し、
    隣接している場合はTrue,隣接していない場合はFalseを返す
    """

    zero_idx=searchPiceIndex(0)#0の場所探す
    idx=searchPiceIndex(num)#numの場所探す
    upper_idx=idx-3
    lower_idx=idx+3
    left_idx=idx-1
    right_idx=idx+1

    if(upper_idx==zero_idx):
        return True
    elif(lower_idx==zero_idx):
        return True
    elif(left_idx==zero_idx)and not (left_idx % 3==0):
        return True
    elif(right_idx==zero_idx )and not (right_idx % 3==1):
        return True
    else:
        return False
#ウィンドウ生成
root=tk.Tk()
root.title('8パズル')
root.geometry('600x400')

""" ラベル表示領域の設定 """ 

lbl_frm = tk.LabelFrame(root) # ラベルをまとめるフレーム

# 残り手数

tesu_frm = tk.LabelFrame(lbl_frm) 

tesu1 = tk.Label(tesu_frm, text='残り手数 :')
tesu1.pack()
tesu2 = tk.Label(tesu_frm, text=100)
tesu2.pack()

tesu_frm.pack(padx=5, pady=5)

#残り時間

time_frm = tk.LabelFrame(lbl_frm) 

time1 = tk.Label(time_frm, text='経過時間 :')
time1.pack()
time2 = tk.Label(time_frm, text=str(0)+'秒')
time2.pack()

time_frm.pack(padx=5, pady=5)


#モード

mode_frm = tk.LabelFrame(lbl_frm) 

mode1 = tk.Label(mode_frm, text='　モード :　')
mode1.pack()
mode2 = tk.Label(mode_frm, text='横並び')
mode2.pack()

mode_frm.pack(padx=5, pady=5)

#ベストタイム

besttime_frm = tk.LabelFrame(lbl_frm) 

besttime1 = tk.Label(besttime_frm, text='ベストタイム :')
besttime1.pack()
besttime2 = tk.Label(besttime_frm, text=kanri.besttime)
besttime2.pack()

besttime_frm.pack(padx=5, pady=5)




lbl_frm.pack( side='left',padx=30)


flm=tk.LabelFrame(root)#フレームの生成


#画像の生成
pice_image={}
pice_image[0]=tk.PhotoImage(file='./image/0.png')#1番のピースが造成性
pice_image[1]=tk.PhotoImage(file='./image/1.png')#2番のピースが造成性
pice_image[2]=tk.PhotoImage(file='./image/2.png')#3番のピースが造成性
pice_image[3]=tk.PhotoImage(file='./image/3.png')#4番のピースが造成性
pice_image[4]=tk.PhotoImage(file='./image/4.png')#5番のピースが造成性
pice_image[5]=tk.PhotoImage(file='./image/5.png')#6番のピースが造成性
pice_image[6]=tk.PhotoImage(file='./image/6.png')#7番のピースが造成性
pice_image[7]=tk.PhotoImage(file='./image/7.png')#8番のピースが造成性
pice_image[8]=tk.PhotoImage(file='./image/8.png')#9番のピースが造成性

#ピース配列の生成
pice_label_dict={}

#ピース位置管理
pice_dict={}#ピース位置管理（表示場所とピース番号)
answer_dict={}#解答

randomchange()#ピースセット
setanswer()#解答セット


    


#1番目ピースの生成

pice1=tk.Label(flm,text=pice_dict[1],image=pice_image[pice_dict[1]])
pice1.bind('<1>',clickPice)#<1>は左クリックを表す
pice1.grid(column=0,row=0)
pice_label_dict[1]=pice1



#2番目ピースの生成

pice2=tk.Label(flm,text=pice_dict[2],image=pice_image[pice_dict[2]])
pice2.bind('<1>',clickPice)#<1>は左クリックを表す
pice2.grid(column=1,row=0)
pice_label_dict[2]=pice2



#3番目ピースの生成

pice3=tk.Label(flm,text=pice_dict[3],image=pice_image[pice_dict[3]])
pice3.bind('<1>',clickPice)#<1>は左クリックを表す
pice3.grid(column=2,row=0)
pice_label_dict[3]=pice3



#4番目ピースの生成

pice4=tk.Label(flm,text=pice_dict[4],image=pice_image[pice_dict[4]])
pice4.bind('<1>',clickPice)#<1>は左クリックを表す
pice4.grid(column=0,row=1)
pice_label_dict[4]=pice4

#5番目ピースの生成

pice5=tk.Label(flm,text=pice_dict[5],image=pice_image[pice_dict[5]])
pice5.bind('<1>',clickPice)#<1>は左クリックを表す
pice5.grid(column=1,row=1)
pice_label_dict[5]=pice5

#6番目ピースの生成

pice6=tk.Label(flm,text=pice_dict[6],image=pice_image[pice_dict[6]])
pice6.bind('<1>',clickPice)#<1>は左クリックを表す
pice6.grid(column=2,row=1)
pice_label_dict[6]=pice6

#7番目ピースの生成

pice7=tk.Label(flm,text=pice_dict[7],image=pice_image[pice_dict[7]])
pice7.bind('<1>',clickPice)#<1>は左クリックを表す
pice7.grid(column=0,row=2)
pice_label_dict[7]=pice7

#8番目ピースの生成

pice8=tk.Label(flm,text=pice_dict[8],image=pice_image[pice_dict[8]])
pice8.bind('<1>',clickPice)#<1>は左クリックを表す
pice8.grid(column=1,row=2)
pice_label_dict[8]=pice8

#9番目ピースの生成

pice9=tk.Label(flm,text=pice_dict[9],image=pice_image[pice_dict[9]])
pice9.bind('<1>',clickPice)#<1>は左クリックを表す
pice9.grid(column=2,row=2)
pice_label_dict[9]=pice9




flm.pack(side='left',pady=40)#フレームの表示

""" ボタン表示領域の設定 """ 

btn_frm = tk.LabelFrame(root) # ボタンをひとまとめに表示するフレーム

modoru_btn = tk.Button(btn_frm, text='一手に戻る',command=modoru)
modoru_btn.pack(padx=5, pady=5)

risetto_btn = tk.Button(btn_frm, text='やり直す',command=risetto)
risetto_btn.pack(padx=5, pady=5)

mode_btn = tk.Button(btn_frm, text='モード変更',command=modechange)
mode_btn.pack(padx=5, pady=5)


btn_frm.pack( side='left',padx=30)


root.mainloop()