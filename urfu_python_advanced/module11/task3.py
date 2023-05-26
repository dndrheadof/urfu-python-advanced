import logging
import random
import threading
import time

TOTAL_TICKETS = 10
SEATS_LEFT = 44

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info("Seller started work")

    def run(self):
        global TOTAL_TICKETS
        global SEATS_LEFT
        is_running = True
        while is_running:
            self.random_sleep()
            if SEATS_LEFT != 0 and TOTAL_TICKETS <= 4:
                continue
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f"{self.getName()} sold one;  {TOTAL_TICKETS} left")

        logger.info(f"Seller {self.getName()} sold {self.tickets_sold} tickets")

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_printed = 0
        logger.info("Director started work")

    def run(self):
        global TOTAL_TICKETS
        global SEATS_LEFT
        is_running = True
        while is_running:
            if TOTAL_TICKETS <= 4:
                with self.sem:
                    tickets_to_print = min(10 - TOTAL_TICKETS, SEATS_LEFT)
                    TOTAL_TICKETS += tickets_to_print
                    SEATS_LEFT -= tickets_to_print
                    self.tickets_printed += tickets_to_print
                    logger.info(
                        f"Director added {tickets_to_print} tickets; {SEATS_LEFT} left"
                    )
                    if SEATS_LEFT == 0:
                        is_running = False

        logger.info(f"Director printed {self.tickets_printed} tickets")


def main():
    semaphore = threading.Semaphore()
    staff = []

    director = Director(semaphore)
    director.start()

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        staff.append(seller)
    staff.append(director)

    for seller in staff:
        seller.join()


if __name__ == "__main__":
    main()
