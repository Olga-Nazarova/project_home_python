str = "ываабв лповап абвцукв алоабвабв ываываыв"
res = str.split()
f = 'абв'
new_res = []
i = 0
while i < len(res):
    if res[i].find(f) < 0:
        new_res.append(res[i])
    i+=1
print(new_res)