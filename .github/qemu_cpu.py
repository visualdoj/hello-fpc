import sys

cpu = sys.argv[1] if len(sys.argv) > 1 else 'x86_64'

if cpu == 'powerpc':
    cpu = 'ppc'
elif cpu == 'powerpc64':
    cpu = 'ppc64'
elif cpu == 'i8086':
    cpu = 'i386'

print(cpu)
