#import sherlock
from sherlock import main
from multiprocessing import Pool

tab = ["abc","abcd","abcd","abcdd"]

for usr in tab:
    main(usr)

"""
with Pool(8) as p:
    print(p.map(sherlock.main,tab))
"""
