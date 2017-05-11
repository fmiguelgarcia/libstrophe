cmake_minimum_required( VERSION 3.5)
project( strophe)

find_package( GnuTLS REQUIRED)
option( WITH_TESTS "Build tests" ON)
option( WITH_EXAMPLES "Build examples" ON)

# Include conan.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
include_directories( 
	${CMAKE_SOURCE_DIR} ${CMAKE_SOURCE_DIR}/src
	${GNUTLS_INCLUDE_DIR}
)

# Source
set( strophe_MAYOR_VERSION 0)
set( strophe_MINOR_VERSION 9)
set( strophe_BUILD_VERSION 1)

set( strophe_SRCS
	src/auth.c src/conn.c src/crypto.c src/ctx.c src/event.c src/handler.c
	src/hash.c src/jid.c src/md5.c
	src/parser_expat.c
	src/rand.c
	src/resolver.c
	src/sasl.c
	src/scram.c
	src/sha1.c
	src/snprintf.c
	src/sock.c
	src/stanza.c
	src/thread.c
	src/tls_gnutls.c
	src/util.c
	src/uuid.c

	src/oocontext.cpp
	src/oostanza.cpp
)

# Test and examples
if( ${WITH_TESTS})
	enable_testing()
	add_subdirectory( tests)
endif()

if( ${WITH_EXAMPLES}) 
	add_subdirectory( examples)
endif()


# Link
add_definitions()
add_library( strophe SHARED ${strophe_SRCS})
target_link_libraries( strophe 
	${GNUTLS_LIBRARIES}
	${CONAN_LIBS}) 
set_target_properties( strophe PROPERTIES 
	VERSION ${strophe_MAYOR_VERSION}.${strophe_MINOR_VERSION}.${strophe_BUILD_VERSION}
	SOVERSION ${strophe_MAYOR_VERSION})
