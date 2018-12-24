from scan.lib import GetTarget
from scan import generic_scan
from scan.lib import database
import threading
from time import sleep

if __name__ == "__main__":

    g = GetTarget.GetTarget()
    g.gen_target()
    threads = []

    def execute():

        d = database.DataBase(g.target + '.db')
        while d.get_data()[0]:
            target_range = d.get_data()
            d.update_data(target_range)
            s = generic_scan.ScanHTTPBasic(target_range)
            s.search_web_server()

    for i in range(5):
        t = threading.Thread(target=execute)
        threads.append(t)
        t.start()
        sleep(5)

    for t in threads:
        t.join()