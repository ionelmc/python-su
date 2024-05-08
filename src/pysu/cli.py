import argparse
import grp
import os
import pwd
import sys

parser = argparse.ArgumentParser(description="Change user and exec command.")
parser.add_argument("user")
parser.add_argument("command")


def main(argv=None):
    opts, args = parser.parse_known_args(args=argv)
    if ":" in opts.user:
        user, group = opts.user.split(":", 1)
    else:
        user, group = opts.user, None

    if user.isdigit():
        uid = int(user)
        try:
            pw = pwd.getpwuid(uid)
        except KeyError:
            pw = None
    elif user:
        try:
            pw = pwd.getpwnam(user)
        except KeyError:
            print(f"pysu: error: unknown user name {user!r}.", file=sys.stderr)
            return 1
        else:
            uid = pw.pw_uid
    else:
        uid = os.getuid()
        try:
            pw = pwd.getpwuid(uid)
        except KeyError:
            pw = None

    if pw:
        home = pw.pw_dir
        name = pw.pw_name
    else:
        home = "/"
        name = user

    if group:
        if group.isdigit():
            gid = int(group)
        else:
            try:
                gr = grp.getgrnam(group)
            except KeyError:
                print(f"pysu: error: unknown group name {group!r}.", file=sys.stderr)
                return 2
            else:
                gid = gr.gr_gid
    elif pw:
        gid = pw.pw_gid
    else:
        gid = os.getgid()
        print(f"pysu: warning: could not figure our a group id for {user!r}, defaulting to current {gid=}.", file=sys.stderr)

    current_gid = os.getgid()
    current_uid = os.getuid()
    current_gl = set(os.getgroups())

    if group:
        gl = {gid}
    else:
        gl = set(os.getgrouplist(name, gid))

    if current_gl != gl:
        try:
            os.setgroups(list(gl))
        except PermissionError:
            print(
                f"pysu: error: could not set supplemental group ids to {gl} (current uid={current_uid} gid={current_gid}).", file=sys.stderr
            )
            return 3
    else:
        print(f"pysu: warning: requested supplemental group ids {gl} are identical to the current ones.", file=sys.stderr)

    if current_gid == gid:
        print(f"pysu: warning: requested gid {gid} is identical to the current one.", file=sys.stderr)

    try:
        os.setgid(gid)
    except PermissionError:
        print(f"pysu: error: could not set gid to {gid} (current uid={current_uid} gid={current_gid}).", file=sys.stderr)
        return 3

    if current_uid == uid:
        print(f"pysu: warning: requested uid {uid} is identical to the current one.", file=sys.stderr)

    try:
        os.setuid(uid)
    except PermissionError:
        print(f"pysu: error: could not set uid to {uid} (current uid={current_uid} gid={current_gid}).", file=sys.stderr)
        return 4

    os.environ["USER"] = name
    os.environ["HOME"] = home
    os.environ["UID"] = str(uid)

    os.execvp(opts.command, [opts.command, *args])  # noqa: S606


if __name__ == "__main__":
    main()
