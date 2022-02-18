# ProjectOwlSecurity

submissionScript.py:
Usage: python3 submissionScript.py

The script will prompt you if you would like to submit messages, or if you would just like to retrieve data from the DMS. 

For submitting messages, specify the number of clients to send at every message, the number of messages each client will send, and the ID for each client (or enter for default). The ID MUST be to specifications found within the portal, otherwise unpredictable behavior will occur. The script will then send off all messages (waiting between each "round" of messages by a time specified by you) and save a file (default "expected.out") in the program location.

If you would like to retrieve data from the DMS without sending messages, you must specify the time frame in which you would like data (in UTC). If you already sent messages, the time frame will be the time taken to send the messages, plus the time you specified to wait after sending data. The program will prompt you for user credentials for the DMS, then retrieve any data received. After getting the raw data, it will parse it for only messages, and save all messages in the same format as the submit in a file (default "DMSData.out")

Diff the two files and tadah you can see what you sent, versus what the server received. 
To actually figure out where packets are being lost or dropped, further investigation is nescessary.
