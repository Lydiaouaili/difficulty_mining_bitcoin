
import hashlib
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


max_nonce = 2 ** 32 # 4 billion
def proof_of_work(header, difficulty_bits):
    iteer = 0
    target = 2 ** (256 - difficulty_bits)
    for nonce in range(max_nonce):
        iteer = iteer + 1
        hash_result = hashlib.sha256((str(header) + str(nonce)).encode('utf-8')).hexdigest()
        if  int(hash_result, 16) < target:
            print ("Success with nonce %d" % nonce)
            print ("Hash is %s" % hash_result)
            print ("Number of iterations is %s" % iteer)
            return (hash_result, nonce, iteer)
    print ("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':
    nonce = 0
    hash_result = ''
    L = []
    #32 bit normalement
    for difficulty_bits in range(26):
        C = []
        difficulty = 2 ** difficulty_bits
        print( "")
        print ("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print ("Starting search...")
        start_time = time.time()
        new_block = 'test block with transactions' + hash_result
        (hash_result, nonce,iteer) = proof_of_work(new_block, difficulty_bits)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print ("Elapsed time: %.4f seconds" % elapsed_time)
        if elapsed_time > 0: 
            hash_power = float(int(nonce)/elapsed_time)
            C = [(difficulty,iteer,elapsed_time, hash_power)]
            L= L + C
            print ("Hashing power: %ld hashes per second" % hash_power)


y1 = [L[i][1]for i in range(len(L))]
y1
x1=[L[i][0]for i in range(len(L))]
x1

x1 = [L[i][0]for i in range(len(L))]
y1 = [L[i][1]for i in range(len(L))]
# plotting the line 1 points
plt.plot(y1,x1, label = " Elapsed time vs difficulty")
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.plot(y1, x1)
 
# naming the x axis
plt.ylabel('Numbers of terations of PoW (Logarithmic Axes)')
# naming the y axis
plt.xlabel('difficulty level (Logarithmic Axes)')
 
# giving a title to my graph
plt.title('iteration vs difficulty')
 
# function to show the plot
plt.show()
