from collections import OrderedDict

from pyexcel_xls import get_data
from pyexcel_xls import save_data
import sys
import os
import os.path


def read_xls_file():
    xls_data = get_data(r"/home/ubuntu/Desktop/1.xlsx")
    logfile = open("/home/ubuntu/Desktop/1test.txt", "w")


    for sheet_n in xls_data.keys():
        try:
            for k,v in xls_data[sheet_n]:
                try:
                    print "\""+k+"\""+"=\""+v+"\";"
                    log="\""+k+"\""+"=\""+v+"\";\n"
                    logfile.write(log.encode('utf8'))
                except Exception,e:
                    print e
                    pass
        except Exception,e:
            print e
            pass
    logfile.close()

if __name__ == '__main__':
    read_xls_file()




 # for iOS
# from collections import OrderedDict
#
# from pyexcel_xls import get_data
# from pyexcel_xls import save_data
# import sys
# import os
# import os.path
#
#
# def read_xls_file():
#     xls_data = get_data(r"/home/ubuntu/Desktop/1.xlsx")
#     logfile = open("/home/ubuntu/Desktop/1test.txt", "w")
#
#
#     for sheet_n in xls_data.keys():
#         try:
#             for k,v in xls_data[sheet_n]:
#                 try:
#                     print "\""+k+"\""+"=\""+v+"\";"
#                     log="\""+k+"\""+"=\""+v+"\";\n"
#                     logfile.write(log.encode('utf8'))
#                 except Exception,e:
#                     print e
#                     pass
#         except Exception,e:
#             print e
#             pass
#     logfile.close()
#
# if __name__ == '__main__':
#     read_xls_file()