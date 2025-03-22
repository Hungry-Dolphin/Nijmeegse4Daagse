from time import sleep
from worker import Worker
import threading


class TicketGetter:
    worker_list = list()
    tickets = threading.Event()

    def __init__(self, url: str, amount_of_workers: int):
        self.__BASE_URL = url

        # Init the workers
        for x in range(amount_of_workers+1):
            worker = Worker(f'Worker {x+1}', url, self.tickets)
            self.worker_list.append(worker)
            sleep(1)


    def main(self):
        # Start all workers
        for worker in self.worker_list:
            worker.start()
            sleep(1)



if __name__ == '__main__':
    TicketGetter('https://duckduckgo.com/?q=what+is+my+ip', 2).main()
    # TicketGetter('https://atleta.cc/e/zRLhtOq7pOcB/resale', 2).main()
