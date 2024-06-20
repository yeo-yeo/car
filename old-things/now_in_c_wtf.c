#include <stdio.h>
#include <stdlib.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>
#include <unistd.h>
#include <sys/socket.h>

int main(int argc, char **argv)
{
    struct sockaddr_rc addr = {0};
    int s, status;
    char dest[18] = "00:14:03:05:09:BF";
    char message[] = "F";

    // allocate a socket
    s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);

    // set the connection parameters
    addr.rc_family = AF_BLUETOOTH;
    addr.rc_channel = 1; // RFCOMM channel number

    str2ba(dest, &addr.rc_bdaddr);

    // connect to server
    status = connect(s, (struct sockaddr *)&addr, sizeof(addr));

    if (status == 0)
    {
        printf('sending');
        status = write(s, message, sizeof(message));
        printf('sent');
    }

    if (status < 0)
    {
        perror("Error connecting");
    }

    close(s);
    return 0;
}
