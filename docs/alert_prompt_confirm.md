# 訊息框

<https://www.selenium.dev/documentation/en/webdriver/js_alerts_prompts_and_confirmations/>

### 使用情境

- 跳離本站警告
- 動作前警告提示

## 警告訊息框 (Alert)

```py
alert = driver.switch_to.alert
alert.text
alert.accept()
expected_conditions.alert_is_present()
```

## 確認訊息框 (Confirm)

```py
alert = driver.switch_to.alert
alert.text
alert.accept()
alert.dismiss()
```

## 提示訊息對話 (Prompts)

```py
alert = driver.switch_to.alert
alert.send_keys("AILIN LIOU")
alert.text
alert.accept()
```
