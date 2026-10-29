# GitHub Actions 招生說明會示範專案

兩個 3 分鐘內能演完的 GitHub Actions 範例，用公開 repo 時，GitHub 託管的標準 runner 免費。

| 範例 | 觸發方式 | 觀眾看到什麼 |
|---|---|---|
| A. 說明會留言牆（`wall.yml`） | 有人開 Issue | 機器人幾秒內自動回覆，約 1 分鐘後大螢幕留言牆出現他的名字 |
| B. 九宮格平行測試（`ci.yml`） | push 或 Pull Request | 3 種作業系統 × 3 個 Python 版本，9 個測試同時跑；改壞程式就 9 格一起變紅、不能合併 |

## 說明會前一天的設定（約 10 分鐘）

1. 在 GitHub 建立一個**公開** repo（例如 `gh-demo`），把這個資料夾的內容全部推上去。
2. **Settings → Pages → Build and deployment → Source** 選 **GitHub Actions**。
3. **Actions** 分頁 → 選「說明會留言牆」→ **Run workflow** 先跑一次，確認網址 `https://wolfytw.github.io/gh-demo/` 能開。
4. **Settings → Branches → Add branch protection rule**（或 Rulesets）：
   - Branch name pattern：`main`
   - 勾選 **Require a pull request before merging**
   - 勾選 **Require status checks to pass**，加入 9 個「九宮格平行測試」的檢查（要先跑過一次才選得到）
5. 把 `https://github.com/wolfytw/gh-demo/issues/new` 做成 QR code，放進簡報 Demo A 那一頁。
6. 先開好兩個分頁：留言牆網址、repo 的 Actions 分頁。

## 現場操作腳本

### 範例 A：留言牆
1. 大螢幕開留言牆，請有 GitHub 帳號的觀眾掃 QR code 開 Issue：標題寫名字、內文寫一句「我想學 GitHub 的原因」。
2. 切到 Issue 頁面，等 5–10 秒，機器人回覆就出現。
3. 切到 Actions 分頁看 workflow 在跑。
4. 約 1 分鐘後切回留言牆（每 20 秒自動重新整理），名字出現。
5. 沒有觀眾有帳號時，講師自己用手機開 Issue 示範。

### 範例 B：九宮格
1. 在 GitHub 網頁上直接編輯 `src/calc.py`，把 `h * h` 改成 `h * 2`。
2. 選 **Create a new branch and start a pull request**。
3. PR 頁面下方出現 9 個檢查同時在跑；切到 Actions 分頁看 3×3 矩陣圖。
4. 約 1 分鐘後 9 格全紅，**Merge 按鈕被擋住**。
5. 把程式改回來再 commit 一次 → 9 格轉綠 → 可以合併。

## 檔案

```
.github/workflows/wall.yml   範例 A
.github/workflows/ci.yml     範例 B
scripts/build_wall.py        把 Issues 轉成留言牆網頁（會跳脫 HTML，避免注入）
src/calc.py                  範例 B 的小程式（BMI 計算）
tests/test_calc.py           範例 B 的測試
```

## 注意

- 留言牆會公開顯示 Issue 標題與內容，事前提醒觀眾不要寫個資。說明會結束後可關閉 Issue 或把 repo 設為私人。
- macOS runner 排隊時間偶爾較長，演示前先跑一次暖身；真的卡住時可只演 Ubuntu／Windows 的 6 格。
