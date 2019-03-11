# Raise_TW
## 環境
1. ``pip3 install chartify``
2. ``pip3 install chromedriver``
3. ``sudo cp chromedriver/ /usr/local/bin #失敗``
4. ``pip3 install pandas``
5. ``git clone'https://github.com/Kevin8701111/Raise_TW_chartify.git'``
## 如何更改參數 
ch.plot.scatter(data_frame=data,
        x_column='date',
        y_column='unit_price')

## 使用方式
1. 進入：https://github.com/spotify/chartify/blob/master/examples/Examples.ipynb
##### 並依照自己的資料選取適當的呈現方式 , 並複製包含ch = chartify.Chart...ch.show('png')
##### 但是由於前面環境 chromedriver加入path問題未解決所以先把'png'先刪除
