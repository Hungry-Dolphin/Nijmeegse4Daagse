from time import sleep
from worker import Worker
import threading


class TicketGetter:
    worker_list = list()
    tickets = threading.Event()

    def __init__(self, url: str, amount_of_workers: int):
        self.__BASE_URL = url

        # Init the workers
        for x in range(amount_of_workers):
            worker = Worker(x+1, url, self.tickets)
            self.worker_list.append(worker)


    def main(self):
        # Start all workers
        for worker in self.worker_list:
            worker.start()
            # Stagger worker start for more refresh coverage
            sleep(1)



if __name__ == '__main__':
    TicketGetter('https://atleta.cc/e/zRLhtOq7pOcB/resale', 5).main()
