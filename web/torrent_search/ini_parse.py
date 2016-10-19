from ConfigParser import *

conf=ConfigParser()
conf.read('torrents.ini')

print conf.sections()
print conf.defaults()

section='tfile.me'
if conf.has_section(section):
    print section+" exists"
    print conf.options(section)

    option='host'
    if conf.has_option(section,option):
        print conf.get(section,option)
    else:
        print "option ",option," in section ",section," no exists"
else:
    print section+" no exists"

if conf.has_option('DEFAULT','proxy'):
    print 'proxy='+conf.get('DEFAULT','proxy')


if conf.has_option('tfile.me','re'):
    print 're='+conf.get('tfile.me','re')
