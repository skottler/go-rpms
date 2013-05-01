# It's build time, baby!

### Setup
* hg clone -u release https://go.googlecode.com/hg/ go
* tar -zcvf `cat go/VERSION`.tar.gz go
* Update the version number from go/VERSION in go.spec

### Build
* rpmbuild -bs --nodeps --define "_sourcedir ." --define "_srcrpmdir ." go.spec
* sudo mock [the SRPM you built]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

## License and Authors

* Sam Kottler <shk@linux.com>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
