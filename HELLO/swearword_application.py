import sys
print('total arguments:' , len(sys.argv))
print('the argument values are:', str(sys.argv))

in_file =sys.argv[1]
out_file=sys.argv[2]
with open("out.txt", "w") as out_file:
    with open("in.txt", "r") as file:
        file_list = file.readline()
        for x in file_list:
            out_file.write(filter.swearwords(x))





