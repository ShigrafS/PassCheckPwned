# PassCheckPwned
This python program uses api.pwnedpassword.com to check how many times a password has leaked online. 
The purpose of this program is to ensure privacy and user security of the users by ensuring the password will not be intercepted in any case.
The program works by first hashing the user password(SHA1).
The small part of the SHA1 version is then used to retrieve a list of all matching passwords and is then compared against the original password to know if the password has been ever leaked and how many times.
In this way, the user's password never leaves the device and the hashing ensures that the user's data will not be intercepted in any case.
