RSI= int(input("Masukan besar RSI: "))
MACD= input("Masukan kondisi MACD: ")

if RSI >= 70 and MACD == "death-cross":
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")
elif RSI <= 30 and MACD == "golden-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")
elif RSI >= 70 and MACD == "golden-cross":
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, tunggu MACD sampai death-cross")
elif RSI <= 30 and MACD == "death-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, tunggu MACD sampai Golden-cross")
else:
    print("RSI berada di area 30 - 70, bukan saatnya membeli maupun menjual")

