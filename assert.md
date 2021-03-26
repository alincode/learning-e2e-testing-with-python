# 斷言檢查 (assert)

### 定義與使用方式

assert 關鍵字可以測試，判斷條件回傳的是否為 `True`，如果回傳 `False` 的話，就會拋出一個 `AssertionError`。

### 常見使用情境

- 前置條件：在每個容易出錯的行為前面一個步驟做事前檢查，並提供出錯時的友善錯誤提示。
- 後置條件：檢查下一步測試行為的必要條件

### 語法

```
assert_stmt ::=  "assert" expression ["," expression]
```

### 語法範例

```py
amount = -1
assert amount > 0, '必須是大於 0 的正數'
```

```py
assert "your website tile" in driver.title
```
