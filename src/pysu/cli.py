import argparse
import os
import pwd
import grp

try:
    from os import getgrouplist
except ImportError:
    def getgrouplist(name, gid):
        return [grp.getgrnam(gr.gr_name).gr_gid for gr in grp.getgrall() if name in gr.gr_mem]


parser = argparse.ArgumentParser(description='Change user and exec command.')
parser.add_argument('user')
parser.add_argument('command')


def main():
    opts, args = parser.parse_known_args()
    if ':' in opts.user:
        user, group = opts.user.split(':', 1)
    else:
        user, group = opts.user, None

    if user.isdigit():
        uid = int(user)
        try:
            pw = pwd.getpwuid(uid)
        except KeyError:
            pw = None
    else:
        try:
            pw = pwd.getpwnam(user)
        except KeyError:
            parser.error("Unknown user name %r." % user)
        else:
            uid = pw.pw_uid

    if pw:
        home = pw.pw_dir
        name = pw.pw_name
    else:
        home = '/'
        name = user

    if group:
        if group.isdigit():
            gid = int(group)
        else:
            try:
                gr = grp.getgrnam(group)
            except KeyError:
                parser.error("Unknown group name %r." % user)
            else:
                gid = gr.gr_gid
    elif pw:
        gid = pw.pw_gid
    else:
        gid = uid

    if group:
        os.setgroups([gid])
    else:
        gl = getgrouplist(name, gid)
        os.setgroups(gl)

    os.setgid(gid)
    os.setuid(uid)
    os.environ['USER'] = name
    os.environ['HOME'] = home
    os.environ['UID'] = str(uid)
    os.execvp(opts.command, [opts.command] + args)


if __name__ == '__main__':
    main()

