# 經驗談

- 不要嘗試在 e2e 測試所有的事。
  - 別忘了我們還有 unit test 和 integrate test。
- 若舊的 App 沒有單元測試，那 e2e 測試有用嗎？
- 為什麼用錄製和回放的方式，不可行？
  - 自動化測試很容易陷入陷阱，認為只要你撰寫一次自動化測試，然後讓它自己運行，就沒事了。
  - 然而，事實是自動化測試並不是和我們想的那樣，後續維護也很重要。
