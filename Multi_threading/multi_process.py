import multiprocessing
import time 

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'square : {i*i}',flush=True) # flush mean python write the outpuut immediatly without creatng any buffer 


def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'cube :{i**3}',flush=True)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_number)
    t  = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time()-t 
    print(finished_time)
