from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=2)              # start 4 worker processes
    #result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    result = pool.map(f, range(20))          # prints "[0, 1, 4,..., 81]"
    
    print result
    
    