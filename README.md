UWB三點定位算法
===
### 製作時間：高一
## 前言
當初因為國中對高職的幻想就是要做專題，但實際進來才發現原來專題是高三才要做有點小失望，我就想說來報個專題創意組好了，剛好當時因為小米手機放上UWB晶片及蘋果的 [AirTag](https://www.apple.com/tw/airtag/ "蘋果官網") 話題蠻熱門的所以想說用UWB技術來做個自動跟隨購物車好了，因為像是當時熱門的跟隨行李箱都是用視覺辨識的方式，容易因爲衣服花色相似或遮擋而造成跟錯人或跟丟，如果將UWB做成手環掛在手上則沒這個問題，但經過初步可行信評估發現當時UWB技術剛起步所以每片UWB晶片都1000元出頭，如果要三點定位的話總共要4片，再加上購物車及馬達的錢應該會上看8000元，這對於一個高一生來說是一個天文數字了，不過我還是抱持著以後有錢會做的原則先做了三點定位求目標在三維空間中相對距離的算法。
## 原理
年代久遠忘記了🥲
## 心得
雖然到現在還沒接觸到UWB技術但當初做的過程也是超級燒腦有趣，為了驗證我的算法求出來的數字正不正確，我還使用 [Minecraft](https://www.minecraft.net/zh-hant "Minecraft官網") 這款遊戲來幫助推理、測試，並在遊戲中透過堆疊方塊來驗證算法正確性，本來以為可以直接有公式算出座標，但經過我高中程度的數學及網路搜尋好像都沒找到方法，所以最後就用迴圈暴力破解了，現在來看或許可以用二元搜尋法等等演算法增加效率，期待之後有朝一日真的接觸到UWB晶片把跟隨車具現化出來。

---
UWB : 超寬頻無載波通訊技術，可用來測距離，誤差10cm

AirTag : 蘋果公司推出的防丟器

Minecraft : 微軟旗下沙盒式創造遊戲