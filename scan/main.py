from scan.lib import GetTarget
from scan.lib import database
from scan import scan_httpbasic

if __name__ == "__main__":
    g = GetTarget.GetTarget()
    g.gen_target()
    d = database.DataBase(g.target+'.db')
    s = scan_httpbasic.ScanHTTPBasic(d.get_data()[1])
    s.search_target()