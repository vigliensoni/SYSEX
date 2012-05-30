from optparse import OptionParser
import os

def main(folder, convert_to):
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            if f.startswith("."):
                continue
            elif f.split('.')[-1] == 'txt':
                print f
                txt_file = open(f)
                reader = txt_file.readlines()
                bytes = reader[0].split(' ')
                print bytes


if __name__ == "__main__":
    usage = "usage: %prog [options] input_folder convert_to"
    opts = OptionParser(usage)
    (options, args) = opts.parse_args()

    if not args:
        opts.error("You must supply arguments to this script.")
    if not args[0]:
        opts.error("You must supply a folder")
    if not args[1]:
        opts.error("You must supply a convert to format")

    main(args[0], args[1])