import datetime, send_data

cefmapping = {"ip-src": "src", "ip-dst": "dst", "hostname": "dhost", "domain": "dhost",
              "md5": "fileHash", "sha1": "fileHash", "sha256": "fileHash",
              "url": "request"}

mispattributes = {'input': list(cefmapping.keys())}
outputFileExtension = "cef"
responseType = "application/txt"


def export_data(request=False):
    if request is False:
        return False
    if "config" in request:
        config = request["config"]
    else:
        config = {"Default_Severity": 1, "Device_Vendor": "MISP", "Device_Product": "MISP", "Device_Version": 1,
                  'custom1':'deviceCustomDate1'}
        if request["type"] in cefmapping:
            send_data.send("{} host CEF:0|{}|{}|{}|{}|{}|{}|{}={} {}={}\n".format(
                datetime.datetime.now().strftime("%b %d %H:%M:%S"),
                config["Device_Vendor"],
                config["Device_Product"],
                config["Device_Version"],
                request["category"],
                request["category"],
                config["Default_Severity"],
                cefmapping[request["type"]],
                request["value"],
                config["custom1"],
                datetime.datetime.fromtimestamp(int(request["timestamp"])).strftime("%b %d %H:%M:%S"),
            ))
