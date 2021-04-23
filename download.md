# 檔案下載

- 可以先點擊下載，然後強制等個數秒，然後驗證檔案是否真的存在於本機，例如 `os.path.exists()`。
- 下載檔案的位置，預設會是在：
  - Win XP `C:\Documents and Settings\你的帳號名稱\Downloads`
  - Win 7/8/10 `C:\Users\你的帳號名稱\Downloads`
  - Mac `/Users/你的帳號名稱/Downloads`

```py
import os.path
from os import path

def main():
   print ("File exists:"+ str(path.exists('demo.txt')))

if __name__== "__main__":
   main()
```

### 參考文獻

- <https://www.browserstack.com/docs/automate/selenium/test-file-download>
- <https://www.guru99.com/python-check-if-file-exists.html>
