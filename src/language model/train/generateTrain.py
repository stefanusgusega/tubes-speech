lookup = ['matikan', 'batalkan']
set = ['pasang']
object = ['alarm']
at = ['pukul']
number = ['satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas','duabelas']
time = ['pagi','siang','sore','malam']

count_num = 0

with open('train.txt', 'w') as f:
    for lu in lookup:
        for obj in object :
            f.writelines('<s> ' + lu.upper() + ' ' + obj.upper() + ' </s>\n')
    for s in set : 
        for obj in object : 
            for a in at : 
                for num in number : 
                    count_num += 1
                    count_time = 0
                    for t in time : 
                        f.writelines('<s> ' + s.upper() + ' ' + obj.upper() + ' ' + a.upper() + ' ' + num.upper()+ ' ' + t.upper() + ' </s>')
                        count_time += 1
                        if not(count_num == len(number) and count_time == len(time)) :
                            f.write('\n')
                        