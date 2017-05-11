set( TEST_LIBRARIES strophe ${CONAN_LIBS} ${GNUTLS_LIBRARIES} -lresolv)

add_executable( testCheckParser check_parser.c )
target_link_libraries( testCheckParser ${TEST_LIBRARIES} )

add_executable( testCtx test_ctx.c )
target_link_libraries( testCtx ${TEST_LIBRARIES})

add_executable( testBase64 test_base64.c test.c )
target_link_libraries( testBase64 ${TEST_LIBRARIES})

add_executable( testJid test_jid.c )
target_link_libraries( testJid ${TEST_LIBRARIES})

add_executable( testResolver test_resolver.c )
target_link_libraries( testResolver ${TEST_LIBRARIES})

add_executable( testRand test_rand.c test.c )
target_link_libraries( testRand ${TEST_LIBRARIES})

add_executable( testScram test_scram.c test.c )
target_link_libraries( testScram ${TEST_LIBRARIES})

add_executable( testSha1 test_sha1.c )
target_link_libraries( testSha1 ${TEST_LIBRARIES})

add_executable( testMd5 test_md5.c test.c )
target_link_libraries( testMd5 ${TEST_LIBRARIES})

add_executable( testSnprintf test_snprintf.c )
target_link_libraries( testSnprintf ${TEST_LIBRARIES})

add_executable( testString test_string.c )
target_link_libraries( testString ${TEST_LIBRARIES})


add_test( NAME CheckParser COMMAND $<TARGET_FILE:testCheckParser>)
add_test( NAME Ctx COMMAND $<TARGET_FILE:testCtx>)
add_test( NAME Base64 COMMAND $<TARGET_FILE:testBase64>)
add_test( NAME Jid COMMAND $<TARGET_FILE:testJid>)
add_test( NAME Resolver COMMAND $<TARGET_FILE:testResolver>)
add_test( NAME Rand COMMAND $<TARGET_FILE:testRand>)
add_test( NAME Scram COMMAND $<TARGET_FILE:testScram>)
add_test( NAME Sha1 COMMAND $<TARGET_FILE:testSha1>)
add_test( NAME Md5 COMMAND $<TARGET_FILE:testMd5>)
add_test( NAME Snprintf COMMAND $<TARGET_FILE:testSnprintf>)
add_test( NAME TString COMMAND $<TARGET_FILE:testString>)
