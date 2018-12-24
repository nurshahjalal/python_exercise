
#192.168.1.108
ipAddress: str = input("please enter your ip address")

print("Total character is used in IP Address is  {0}".format(len(ipAddress)))

num = ""
segment = 1
segmentLength = 0

for i in range(len(ipAddress)):

    if len(ipAddress) != 13:
        print("Your Ip Address is not valid, you entered {0} Character, it should be 13 Character"
              .format(len(ipAddress)))
        break
    elif ipAddress[0] == ".":
        print("You entered an Invalid Ip Address {0}, IP address cannot begin with a dot".format(ipAddress))
        break
    elif ipAddress[len(ipAddress)-1] == ".":
        print("You entered an Invalid Ip Address {0}, IP address cannot End with a dot".format(ipAddress))
        break
    elif ipAddress[i] not in "0123456789.":
        print("You entered an Invalid Ip Address {0}, IP address cannot Cannot have a character".format(ipAddress))
        break
    else:
        for character in ipAddress:
            if character == ".":
                print("Segment {0} contains {1} character".format(segment, segmentLength))
                if (segment == 1 or 2 or 4) & (segmentLength != 3):
                    print("You entered an Invalid Ip Address Segment length {} in segment {}"
                          "".format(segmentLength, segment))
                elif segment == 1 & segmentLength != 1:
                    print("You entered an Invalid Ip Address {0}, IP address have wrong segment length of "
                          "character in Segment {} ".format(ipAddress), segment)

                segment += 1
                segmentLength = 0
            else:
                segmentLength += 1
        num += ipAddress[i]


print(num)




