# Raise_TW
## 環境
1. ``pip3 install chartify``
2. ``pip3 install chromedriver``
3. ``sudo cp chromedriver/ /usr/local/bin #失敗``
4. ``pip3 install pandas``
5. ``git clone'https://github.com/Kevin8701111/Raise_TW_chartify.git'``
## 如何更改參數 
### 1. scatter
ch = chartify.Chart(blank_labels = True, x_axis_type = 'datetime')
ch.plot.scatter(data_frame = 你load進來的資料變數, x_column = '資料欄位', y_column = '資料欄位')
### 2. line
ch = chartify.Chart(blank_labels=True, x_axis_type='datetime')
 ch.plot.line(data_frame = 你load進來的資料變數, x_column = '資料欄位', y_column = '資料欄位', color_column='fruit')
### 3. area
ch = chartify.Chart(blank_labels=True, x_axis_type='datetime')
ch.plot.area(data_frame = 你load進來的資料變數, x_column = '資料欄位', y_column = '資料欄位', color_column = 'fruit', stacked = True)

### 4. area + line
ch = chartify.Chart(blank_labels=True, x_axis_type='datetime')
ch.plot.area(data_frame = 你load進來的資料變數, x_column = '資料欄位', y_column = '資料欄位', second_y_column = '資料欄位')
ch.style.color_palette.reset_palette_order()
ch.plot.line(data_frame = 你load進來的資料變數, x_column = '資料欄位', y_column = '資料欄位')

### 5. bar
ch = chartify.Chart(blank_labels=True, x_axis_type='categorical')
ch.plot.bar(data_frame = 你load進來的資料變數, categorical_columns = '資料欄位', numeric_column = '資料欄位')

### 6. 未實做完～～ 後續圖表只須看code 並調整自己的資料 帶參數即可

## 使用方式
1. 進入：https://github.com/spotify/chartify/blob/master/examples/Examples.ipynb
並依照自己的資料選取適當的呈現方式 , 並複製包含ch = chartify.Chart...ch.show('png')
##### 但是由於前面環境 chromedriver加入path問題未解決所以先把'png'先刪除
2. 資料形式(tidy)：
##### 須符合首列為欄 , 其餘為值的格式
