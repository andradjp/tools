from scan.lib import GetTarget
from scan import scan_httpbasic

if __name__ == "__main__":
    g = GetTarget.GetTarget()
    g.gen_target()
    f = open('ipv4_{}'.format(g.target), 'r')
    target_range = f.readlines()
    s = scan_httpbasic.ScanHTTPBasic(target_range[0].strip())
    s.search_web_server()