#!/usr/bin/env python
'''
1. Use the split method to divide the following IPv6 address into
groups of 4 hex digits (i.e. split on the ":")
FE80:0000:0000:0000:0101:A3EF:EE1E:1719
2. Use the join method to reunite your split IPv6 address back to
its original value.
'''

ipv6_addr = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'

ipv6_sections = ipv6_addr.split(":")

print
print "IPv6 address split:"
print ipv6_sections
print

ipv6_new = ":".join(ipv6_sections)

print "IPv6 address re-joined:"
print ipv6_new
print
