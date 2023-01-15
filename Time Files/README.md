# Time Files

For this task, we were given a corrupted .png file that had been sent through a time machine. To solve this task, we have to open the corrupted file in some hex editor to view the hex dump of flag.png. From there, immediately you can tell that the header is completely wrong as seen here

where the correct header should be 89504E470D0A1A0A (read more about what these values mean here). Once you fix this, the file is not yet fixed and we have to take another look at the hex dump in order to see what's wrong. In the first line there is a hint where we can see that IHDR (a chunk specification for .png files), is reversed to become RDHI. If we look at the next line in the above picture, we can also see that if we reverse blocks of 4 bytes at a time, we can create another chunk specification IDAT. From here we realize that every block of four bytes (a word) is in reverse order, and to fix this we can write a simple script to read the original png byte by byte and reverse each word. The end result is a viewable png file that contains the flag retroCTF{youfixedit}.

