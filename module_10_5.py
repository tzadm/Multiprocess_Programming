import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            all_data.append(file.readline().strip())
            if not file.readline():
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    read_info(filenames[0])
    read_info(filenames[1])
    read_info(filenames[2])
    read_info(filenames[3])
    finish = datetime.datetime.now()
    print(finish - start)


    start_ = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish_ = datetime.datetime.now()
    print(finish_ - start_)