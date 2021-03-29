# request

## 發送一個請求

### HTTP Get

```py
import requests
response = requests.get('https://api.github.com/events')
```

```py
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload
```

### HTTP Post

```py
import requests
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
```

## Response

```py
response.text
response.status_code
```

### JSON Response

```py
import requests
response = requests.get('https://api.github.com/events')
response.json()
```

## 參考文獻

- [Quickstart | Python 官方文件](https://docs.python-requests.org/en/master/user/quickstart/)
