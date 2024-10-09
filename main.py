from indicators.sentiment import score_text_tb as tb, score_text_vader as vd

print(tb("I love you so much! I will be with you for ever and ever!!!!!"))
print(vd("I love you so much! I will be with you for ever and ever!!!!!"))