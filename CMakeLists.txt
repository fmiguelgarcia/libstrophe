cmake_minimum_required( VERSION 3.5)
project( strophe)

option( WITH_TESTS "Build tests" OFF)
option( WITH_EXAMPLES "Build examples" OFF)

# Include conan.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
include_directories( 
	${CMAKE_SOURCE_DIR} ${CMAKE_SOURCE_DIR}/src
)

# Source
set( strophe_MAYOR_VERSION 0)
set( strophe_MINOR_VERSION 9)
set( strophe_BUILD_VERSION 1)

set( strophe_SRCS
	src/common.h
	src/ostypes.h
	src/parser.h
	src/auth.c 
	src/conn.c 
	src/crypto.c 
	src/ctx.c 
	src/event.c 
	src/handler.c
	src/hash.c src/hash.h 
	src/jid.c 
	src/md5.c src/md5.h
	src/parser_expat.c
	src/rand.c src/rand.h
	src/resolver.c src/resolver.h
	src/sasl.c src/sasl.h
	src/scram.c src/scram.h
	src/sha1.c src/sha1.h
	src/snprintf.c src/snprintf.h
	src/sock.c src/sock.h
	src/tls.h
	src/stanza.c
	src/tls_openssl.c
	src/util.c src/util.h
	src/uuid.c
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
if(MSVC)
	target_link_libraries( strophe winmm.lib ${CONAN_LIBS})
else()
	target_link_libraries( strophe ${CONAN_LIBS})
endif()
set_target_properties( strophe PROPERTIES 
	VERSION ${strophe_MAYOR_VERSION}.${strophe_MINOR_VERSION}.${strophe_BUILD_VERSION}
	SOVERSION ${strophe_MAYOR_VERSION})
