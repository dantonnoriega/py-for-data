"""Files and the operating system"""
cd ~/GitHub/pyfordata/appendix/

# opening files
path = '/Users/dnoriega/GitHub/pydata-book/ch13/segismundo.txt'
f = open(path) # open creates a buffer. defaults "read mode", 'r'

for line in f:
    pass

lines = [x.rstrip() for x in open(path)]
lines

# option 'w' would have created a file
path = '/Users/dnoriega/GitHub/pyfordata/appendix/segismundo2.txt'
f = open(path, 'w')

"""
r   # Read-only mode
w   # Write-only mode. Creates a new file (deleting any file with the same name)
a   # Append to existing file (create it if it does not exist)
r+  # Read and write
b   # Add to mode for binary files, that is 'rb' or 'wb'
U   # Use universal newline mode. Pass by itself 'U' or appended to one of the read modes like 'rU'
"""

# to write text to a file, you can use `write` or `writelines`
path = '/Users/dnoriega/GitHub/pydata-book/ch13/segismundo.txt'
with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)

open('tmp.txt').readlines()


# Table A-6. Important Python file methods or attributes (pg. 432)
"""
# Return data from file as a string, with optional size argument indicating the number of bytes
to read
    read([size])

# Return list of lines in the file, with optional size argument
    readlines([size])

# Return list of lines (as strings) in the file
    readlines([size])

# Write passed string to file.
    write(str)

# Write passed sequence of strings to the file.
    writelines(strings)

# Close the handle
    close()

# Flush the internal I/O buffer to disk
    flush()

# Move to indicated file position (integer).
    seek(pos)

# Return current file position as integer.
    tell()

# True is the file is closed.
    closed
"""

