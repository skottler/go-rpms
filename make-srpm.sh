#!/usr/bin/env bash
spectool -g -A go.spec

rpmbuild --define "_sourcedir ." \
         --define "_rpmdir ." \
         --define "_buildir ." \
         --define "_srcrpmdir ." \
         --define "_speccdir ." \
         -bs \
         go.spec
rm -v go*.src.tar.gz
echo "Now build the SRPM in mock."
echo "Example: mock -r fedora-rawhide-x86_64 $(find -name go*.src.rpm -print)"
