Remote Packet Capture with tcpdump and Wireshark
#################################################

:date: 2010-01-17 19:52:43
:modified: 2015-12-27 08:30
:tags: command line
:category: short tips
:slug: remote-packet-capture-with-tcpdump-and-wireshark
:authors: Jon Moore


Had a need to capture some traffic on the remote machine and analyze it in Real Time (tm).  Found to solutions to this.  The first, involved just sending the output of tcpdump across the ssh session.
::

	ssh host.example.org tcpump - eth0 -w - > capture.pcap


The other method, picked up from the [wireshark wiki](http://wiki.wireshark.org/CaptureSetup/Pipes) allows for the captured traffic to be viewed as it's being captured in wireshark.  This is done using a combination of ssh and a fifo pipe.  The exact command can very slightly, and I suggest reading the relevant man pages, but something similar to the following (taken from their wiki) should do the trick.

::

	mkfifo /tmp/pipe
	ssh user@remote-host "tshark -w - not port 22" > /tmp/pipe
	wireshark -k -i /tmp/pipe

