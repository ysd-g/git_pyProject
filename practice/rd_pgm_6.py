import sys  #例外処理、コマンドライン引数で必要
import datetime #日付チェックで必要
import os   #引数入力で必要
import glob

args = sys.argv
FILES = glob.glob('/home/yoshida/pyProject/data/DATAFL-*')   # ファイルの名前
DATA_DIR = '/home/yoshida/pyProject/data'              # dataディレクトリのPATH
RESULT_DIR = '/home/yoshida/pyProject/data/result'     # resultディレクトリのPATH

# 日付チェック
def checkDate(today):
    try:
        adp = datetime.datetime.strptime(args[1], "%Y%m%d") # 入力した日にち(str型)をdatetime型に変更
                                                            # 入力日がYYYYmmdd型であるかをチェック
                                                            # adp : 2019-04-14 00:00:00(datetime.datetime)
        adp = datetime.datetime.strftime(adp, "%Y%m%d")     # チェック済みの入力日をstr型へ変換
                                                            # adp : 20190414(str)
        return adp
    
    except IndexError:                                      # 何も入力されていない場合
        adp = today                                         # 今日の日付を自動入力
        return adp

    except ValueError:                                      # 無効な日付（20190441, 2019/03/03）
        print("無効な日付です。---入力例：20180929---")
        sys.exit()



# ディレクトリの存在チェック
def isDirectory(PATH):
    return os.path.exists(PATH)




# ファイルの存在チェック
def readProcedure(DATA_DIR, FILES, adp, i, j, lc, ini, fin):

    if(isDirectory(DATA_DIR)):
        total, count = getFileContents(FILES, adp, i, j, lc, ini, fin)

    else:
        print("読み出し用ディレクトリが存在しませんでした")
        sys.exit()

    return total, count




# ファイル内容の読み出し
def getFileContents(FILES, adp, i, j, lc, ini, fin):
    total = 0
    count = 0

    try:
        for FILE in FILES:                                  # 該当するファイル1個ずつ読み込んでいく
            epochTime = os.path.getmtime(FILE)              # ファイルの最終更新時刻を取得
                                                            # epochTimeは、UNIX(float型)
            updateTime = datetime.date.fromtimestamp(epochTime).strftime("%Y%m%d")
                                                            # 20190414(str)

            # updateTime = datetime.date.fromtimestamp(epochTime) なら、datetime.date型
            if adp == updateTime:                           # strとstrの比較
                count = count + 1
                f = open(FILE, 'r')
                line = f.readline().strip()                 # strip()は空白詰め
                while line:
                    if line[i:j] == lc:
                        print(line[ini:fin])
                        total = total + int(line[ini:fin])  # 特定箇所の数字を取得する
                    line = f.readline().strip()
                f.close()

    except:
        print("ファイル内容の読み出しで、エラーが発生しました")

    finally:
        return total, count



# 結果をファイルに書き込む
def writeProcedure(RESULT_DIR, today, adp, total, count):

    if(isDirectory(RESULT_DIR)):
        writeResult(RESULT_DIR, today, adp, total, count)

    else:
        print("書き込み用ディレクトリが存在しませんでした")
        sys.exit()




# 結果をファイルに書き込む
def writeResult(RESULT_DIR, today, adp, total, count):
    try:
        #line = "対象日："+ adp +" 更新日："+ today +"\n"+"読み込みファイル："+ str(count) +"件 合計値："+ str(total)
        line = "対象日：{0:<10s} 更新日：{1:<10s} \n読み込みファイル: {2:<d}件 合計値：{3:<10d}".format(adp, today, count, total)

        print(line)
        fileName = RESULT_DIR + "/SUM_RESULT_" + adp
        print(fileName)
        f = open(fileName, mode='w')
        f.write(line)
        f.close()
    except:
        print("ファイル内容の書き込みで、エラーが発生しました")


if __name__ == '__main__':
    
    today = datetime.date.today().strftime('%Y%m%d')         # 今日の日付をYYYYmmdd型に変換
    adp = checkDate(today)                                   # 日付チェック
    total, count = readProcedure(DATA_DIR, FILES, adp, 0, 1, "8", 3, 10)
    print(total)
    writeProcedure(RESULT_DIR, today, adp, total, count)

    #try:
    #total = isFile(adp)




