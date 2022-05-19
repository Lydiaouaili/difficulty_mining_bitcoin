
import hashlib
import time

max_nonce = 2 ** 32 # 4 billion
def proof_of_work(start, header, difficulty_bits):
    iteer = 0
    target = 2 ** (256 - difficulty_bits)
    for nonce in range(start,max_nonce,1):
        iteer = iteer + 1
        hash_result = hashlib.sha256((str(header) + str(nonce)).encode('utf-8')).hexdigest()
        if  int(hash_result, 16) < target:
            print ("Success with nonce %d" % nonce)
            print ("Hash is %s" % hash_result)
            print ("Number of iterations is %s" % iteer)
            return (start, hash_result, nonce, iteer)
    print ("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':
    nonce = 0
    hash_result = ''
    L = []
    start=0
    #32 bit normalement
    for difficulty_bits in range(30):
        C = []
        difficulty = 2 ** difficulty_bits
        print( "")
        print ("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print ("Starting search...")
        start_time = time.time()
        new_block = 'test block with transactions'
        for start in [0,10000,250000]:
            (start, hash_result, nonce,iteer) = proof_of_work(start,new_block, difficulty_bits)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print ("Elapsed time: %.4f seconds" % elapsed_time)
            print ("Start nonce: %.4f " % start)
            if elapsed_time > 0: 
                hash_power = float(int(nonce)/elapsed_time)
                C = [(difficulty, start, iteer)]
                L= L + C
            print ("Hashing power: %ld hashes per second" % hash_power)

C1=[L[i] for i in range(0,len(L),3)]
x1 = [C1[i][2]for i in range(len(C1))]
y1 = [C1[i][0]for i in range(len(C1))]
# plotting the line 1 points
plt.plot(y1, x1, label = " Elapsed time vs difficulty")
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

C2=[L[i] for i in range(1,len(L),3)]

x1 = [C2[i][2]for i in range(len(C2))]
y1 = [C2[i][0]for i in range(len(C2))]
# plotting the line 1 points
plt.plot(y1, x1, label = " Elapsed time vs difficulty")
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.plot(y1, x1)
# naming the y axis
plt.xlabel('difficulty level (Logarithmic Axes)')
 # naming the x axis
plt.ylabel('Numbers of terations of PoW (Logarithmic Axes)')

 
# giving a title to my graph
plt.title('iteration vs difficulty')
 
# function to show the plot
plt.show()
C3=[L[i] for i in range(2,len(L),3)]

x1 = [C3[i][2]for i in range(len(C3))]
y1 = [C3[i][0]for i in range(len(C3))]
# plotting the line 1 points
plt.plot(y1, x1, label = " Elapsed time vs difficulty")
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.plot(y1, x1)
 
    # naming the y axis
plt.xlabel('difficulty level (Logarithmic Axes)')
# naming the x axis
plt.ylabel('Numbers of terations of PoW (Logarithmic Axes)')
# naming the y axis
 
# giving a title to my graph
plt.title('iteration vs difficulty')
 
# function to show the plot
plt.show()