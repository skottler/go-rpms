# It's build time, baby!

### Setup
* hg clone -u release https://go.googlecode.com/hg/ go
* tar -zcvf go-`cat go/VERSION`.tar.gz go
* Update the version number from go/VERSION in go.spec

###
* rpmbuild -bs --nodeps --define "_sourcedir ." --define "_srcrpmdir ." go.spec
* sudo mock <the SRPM you built>
