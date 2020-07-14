import argparse
def ArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--readFile', type=str, default="", help="the location of the data file")
    parser.add_argument('--writeFile', type=str, default="", help="the name of the generated figure")
    parser.add_argument('--begin', type=str, default="", help="Jul-10 14:27:08")
    parser.add_argument('--end', type=str, default="", help="Jul-10 14:27:08")
    parser.add_argument('--item', type=str, default="", help="the name of column which you want to analysis")
    return parser.parse_args()
