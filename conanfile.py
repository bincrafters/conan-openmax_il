from conans import ConanFile, tools


class OpenMAXILConan(ConanFile):
    name = "openmax_il"
    version = "1.1.2"
    url = "https://github.com/bincrafters/conan-openmax_il"
    description = "OpenMAX™ IL is a royalty-free API that allows accelerated multimedia applications to be " \
                  "developed and deployed across multiple operating systems and platforms"
    no_copy_source = True
    license = "Khronos"
    exports = ["LICENSE.md"]

    def source(self):
        tools.get('https://www.khronos.org/registry/OpenMAX-IL/api/1.1.2/OpenMAX_IL_1_1_2_Header.zip')

    def package(self):
        self.copy(pattern="*.h", dst="include")

    def package_id(self):
        self.info.header_only()
