import multiprocessing
import datetime


def read_info(name):
    all_data = []
    for name_ in name:
        with open(name_) as file_:
            while True:
                all_data.append(file_.readline().strip())
                if not file_.readline():
                    break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    read_info(filenames)
    end = datetime.datetime.now()
    print(end - start)

    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, (filenames,))

    end = datetime.datetime.now()
    print(end - start)
