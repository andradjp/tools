from scan.lib import GetTarget
from scan import scan_httpbasic
from scan.lib import database
import _thread

if __name__ == "__main__":
    g = GetTarget.GetTarget()
    g.gen_target()
    d = database.DataBase(g.target+'.db')
    target_range = d.get_data()
    d.update_data(target_range)
    s = scan_httpbasic.ScanHTTPBasic(target_range)
    s.search_web_server()
