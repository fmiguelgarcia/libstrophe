from conans import ConanFile, CMake 

class LibStropheConan(ConanFile):
    # Conan 
    name = "libStrophe"
    version = "0.9.1"
    description = "A simple, lightweight C library for writting XMPP clients"
    license = "MIT"
    url = "http://strophe.im/libstrophe"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "expat/2.2.0@dmious/stable", "OpenSSL/1.1.1b@conan/stable"
    exports_sources = "CMakeLists.txt", "src/*", "tests/*", "examples/*", "*.h", "strophe.def"
    options = { "with_tests": [True, False], "with_examples": [True, False]}
    default_options = "with_tests=False", "with_examples=False"

    def build(self):
        cmake = CMake( self)
        cmake.definitions[ "WITH_TESTS" ] = self.options.with_tests
        cmake.definitions[ "WITH_EXAMPLES" ] = self.options.with_examples
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy( pattern="strophe*.h", dst="include/", keep_path=True)
        self.copy( pattern="**/libstrophe.so*", dst="lib/", keep_path=False, symlinks=True)
        self.copy( pattern="**/strophe.so*", dst="lib/", keep_path=False, symlinks=True)
        self.copy( pattern="strophe.*", src="bin", dst="bin", keep_path=False, symlinks=True)
        self.copy( pattern="strophe.*", src="lib", dst="lib", keep_path=False, symlinks=True)

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs.extend(["strophe", "winmm"])
        else:
            self.cpp_info.libs.extend(["strophe", "resolv"])
